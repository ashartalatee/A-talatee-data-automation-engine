import argparse
from pathlib import Path

from engine.loader import load_dataset
from engine.diagnostics import (
    detect_missing,
    detect_duplicate,
    check_schema,
    detect_encoding,
    build_summary
)
from engine.scoring import score_dataset
from engine.business_impact import BusinessImpactMapper
from engine.recommendation import RecommendationEngine
from engine.report_generator import FinalReportGenerator
from engine.config_loader import ConfigLoader
from engine.output_writer import OutputWriter
from engine.logger import get_logger

logger = get_logger("CLI-BATCH")

SUPPORTED_EXT = {".csv", ".xlsx", ".xls"}


def run_single_file(
    file_path: Path,
    config: ConfigLoader,
    output_md_dir: Path,
    writer: OutputWriter
):
    logger.info(f"Processing file: {file_path.name}")

    # 1. Load dataset
    df = load_dataset(str(file_path))

    # 2. Diagnostics
    diagnostics = {
        "missing": detect_missing(df),
        "duplicate": detect_duplicate(df),
        "schema": check_schema(df),
        "encoding": detect_encoding(df)
    }

    summary = build_summary(diagnostics)

    # 3. Scoring & risk
    scores = score_dataset(df, diagnostics, config)
    risk = scores["risk"]

    # 4. Business impact & recommendation
    impact = BusinessImpactMapper(
        risk_level=risk["risk_level"]
    ).map()

    recommendations = RecommendationEngine(
        risk_level=risk["risk_level"]
    ).generate()

    # 5. Write CSV outputs (STANDARDIZED)
    writer.write_dataset_score(
        dataset_name=file_path.name,
        score=scores["dataset_score"],
        risk_level=risk["risk_level"],
        batch=True
    )

    writer.write_column_scores(
        dataset_name=file_path.name,
        column_scores=scores["column_scores"],
        batch=True
    )

    # 6. Generate Markdown report
    report = FinalReportGenerator(
        dataset_name=file_path.name,
        summary=summary,
        scores=scores,
        risk=risk,
        business_impact=impact,
        recommendations=recommendations
    )

    output_md_dir.mkdir(parents=True, exist_ok=True)
    output_md_path = output_md_dir / f"{file_path.stem}_report.md"

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(report.generate_markdown())

    logger.info(f"Finished file: {file_path.name}")
    return output_md_path


def main():
    parser = argparse.ArgumentParser(
        description="Batch Raw Data Diagnostic Engine"
    )

    parser.add_argument(
        "--data-dir",
        required=True,
        help="Directory containing dataset files (csv, xlsx)"
    )

    parser.add_argument(
        "--config",
        default="config/default.yaml",
        help="Path to config file"
    )

    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_md_dir = Path("reports/markdown/batch")

    config = ConfigLoader(args.config)
    writer = OutputWriter()

    files = [
        f for f in data_dir.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXT
    ]

    if not files:
        logger.warning("No supported data files found")
        print(" No dataset files found")
        return

    success, failed = 0, 0

    for file_path in files:
        try:
            run_single_file(
                file_path=file_path,
                config=config,
                output_md_dir=output_md_dir,
                writer=writer
            )
            success += 1
        except Exception as e:
            failed += 1
            logger.error(f"Failed processing {file_path.name}: {e}")

    print(f" Batch completed: {success} success, {failed} failed")
    logger.info(f"Batch finished: {success} success, {failed} failed")


if __name__ == "__main__":
    main()
