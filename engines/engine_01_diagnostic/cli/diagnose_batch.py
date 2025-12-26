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
from engine.logger import get_logger

logger = get_logger("CLI-BATCH")

SUPPORTED_EXT = {".csv", ".xlsx", ".xls"}

def run_single_file(file_path: Path, config: ConfigLoader, output_dir: Path):
    logger.info(f"Processing file: {file_path.name}")

    df = load_dataset(str(file_path))

    diagnostics = {
        "missing": detect_missing(df),
        "duplicate": detect_duplicate(df),
        "schema": check_schema(df),
        "encoding": detect_encoding(df)
    }

    summary = build_summary(diagnostics)
    scores = score_dataset(df, diagnostics, config)
    risk = scores["risk"]

    impact = BusinessImpactMapper(
        risk_level=risk["risk_level"]
    ).map()

    recommendations = RecommendationEngine(
        risk_level=risk["risk_level"]
    ).generate()

    report = FinalReportGenerator(
        dataset_name=file_path.name,
        summary=summary,
        scores=scores,
        risk=risk,
        business_impact=impact,
        recommendations=recommendations
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{file_path.stem}_report.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report.generate_markdown())

    logger.info(f"Finished file: {file_path.name}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Batch Raw Data Diagnostic Engine"
    )

    parser.add_argument(
        "--data-dir",
        required=True,
        help="Directory containing dataset files"
    )

    parser.add_argument(
        "--config",
        default="config/default.yaml",
        help="Path to config file"
    )

    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path("reports/markdown/batch")

    config = ConfigLoader(args.config)

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
            run_single_file(file_path, config, output_dir)
            success += 1
        except Exception as e:
            failed += 1
            logger.error(f"Failed processing {file_path.name}: {e}")

    print(f" Batch completed: {success} success, {failed} failed")
    logger.info(f"Batch finished: {success} success, {failed} failed")


if __name__ == "__main__":
    main()
