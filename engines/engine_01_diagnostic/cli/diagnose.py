import argparse
from pathlib import Path

from engine.loader import load_dataset
from engine.diagnostics import (
    detect_missing,
    detect_duplicate,
    detect_schema,
    detect_encoding,
    generate_summary
)
from engine.scoring import score_dataset
from engine.business_impact import BusinessImpactMapper
from engine.recommendation import RecommendationEngine
from engine.report_generator import FinalReportGenerator
from engine.config_loader import ConfigLoader
from engine.logger import get_logger
from engine.output_writer import OutputWriter

logger = get_logger("CLI")


def run_diagnostic(data_path: str, config_path: str):
    """
    Orkestrasi CLI:
    - Load data
    - Jalankan diagnostics
    - Scoring & risk
    - Output CSV & report markdown
    """

    logger.info(f"Starting diagnostic for {data_path}")

    # =============================
    # Load config & dataset
    # =============================
    config = ConfigLoader(config_path)
    df = load_dataset(data_path)

    # =============================
    # Run diagnostics (ENGINE CORE)
    # =============================
    diagnostics = {
        "missing": detect_missing(df),
        "duplicate": detect_duplicate(df),
        "schema": detect_schema(df),
        "encoding": detect_encoding(df)
    }

    summary = generate_summary(diagnostics)

    # =============================
    # Scoring & risk (FACADE)
    # =============================
    scores = score_dataset(df, diagnostics, config)
    risk_level = scores["risk"]  # STRING: LOW | MEDIUM | HIGH

    # =============================
    # Output CSV (DAY 20 CONTRACT)
    # =============================
    writer = OutputWriter()

    writer.write_dataset_score(
        dataset_name=Path(data_path).name,
        score=scores["dataset_score"],
        risk_level=risk_level
    )

    writer.write_column_scores(
        dataset_name=Path(data_path).name,
        column_scores=scores["column_scores"]
    )

    # =============================
    # Business Layer
    # =============================
    impact = BusinessImpactMapper(
        risk_level=risk_level
    ).map()

    recommendations = RecommendationEngine(
        risk_level=risk_level
    ).generate()

    # =============================
    # Final Report (Markdown)
    # =============================
    report = FinalReportGenerator(
        dataset_name=Path(data_path).name,
        summary=summary,
        scores=scores,
        risk=risk_level,
        business_impact=impact,
        recommendations=recommendations
    )

    output_path = Path("reports/markdown/final_report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report.generate_markdown())

    logger.info("Diagnostic completed successfully")
    print(f"✅ Report generated at: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Raw Data Diagnostic Engine"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Path to dataset file (CSV or Excel)"
    )

    parser.add_argument(
        "--config",
        default="config/default.yaml",
        help="Path to config file"
    )

    args = parser.parse_args()

    run_diagnostic(
        data_path=args.data,
        config_path=args.config
    )


if __name__ == "__main__":
    main()
