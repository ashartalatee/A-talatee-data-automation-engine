from engine.report_generator import FinalReportGenerator

def main():
    # 1. Anggap ini hasil dari engine hari-hari sebelumnya
    summary = {
        "overview": "Dataset memiliki missing value dan duplikasi ringan."
    }

    scores = {
        "dataset_score": 72,
        "column_scores": {
            "price": 65,
            "quantity": 80,
            "date": 90
        }
    }

    risk = {
        "risk_level": "RISK"
    }

    impact = {
        "business_impacts": [
            "Hasil analisis berpotensi bias",
            "Keputusan bisnis perlu validasi tambahan"
        ]
    }

    rec = {
        "recommendations": [
            "Lakukan validasi tambahan pada kolom bermasalah",
            "Diskusikan risiko dengan stakeholder"
        ]
    }

    # 2. Generate report
    report = FinalReportGenerator(
        dataset_name="sales_q1_2024.csv",
        summary=summary,
        scores=scores,
        risk=risk,
        business_impact=impact,
        recommendations=rec
    )

    markdown_report = report.generate_markdown()

    # 3. Simpan ke folder reports/
    output_path = "reports/markdown/final_report.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_report)

    print(f"Report berhasil dibuat: {output_path}")


if __name__ == "__main__":
    main()
