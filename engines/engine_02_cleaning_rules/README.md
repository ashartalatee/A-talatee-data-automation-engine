# Data Cleaning Rule Engine

Engine pembersihan data berbasis aturan (rule-based) yang dirancang untuk
menangani **dataset dunia nyata yang berantakan**, bukan data ideal.
Engine ini fokus pada **reusability, konsistensi, dan skalabilitas**.

---

## Gambaran Umum

Data Cleaning Rule Engine adalah sistem pembersihan data terstruktur
yang bekerja berdasarkan **aturan (rule) terpisah dari kode**.

Engine ini mampu:
- Membersihkan missing value
- Menghapus duplikat & menstandarkan kolom
- Memvalidasi format tanggal & numerik
- Menormalkan dan memetakan data teks (typo, variasi bahasa, case)

Seluruh logika pembersihan dapat dikonfigurasi melalui file **YAML**
tanpa perlu mengubah kode Python.

---

## Masalah yang Diselesaikan

Data klien di dunia nyata sering mengalami:
- Kolom tidak konsisten (spasi, huruf besar/kecil)
- Missing value tanpa pola jelas
- Data duplikat
- Format tanggal tidak valid
- Angka dengan simbol / format berbeda
- Data teks dengan variasi penulisan & bahasa

Pendekatan script satu kali pakai tidak scalable dan sulit dirawat.
Engine ini menyediakan **solusi sistematis & berulang**.

---

## Prinsip Desain

Engine ini dibangun dengan prinsip:

- **Rule-based** → logika dipisahkan dari kode
- **Modular** → tiap jenis pembersihan berdiri sendiri
- **Reusable** → bisa digunakan lintas klien
- **Maintainable** → mudah dirawat & dikembangkan
- **Engineer-oriented** → bukan sekadar script

---

## Arsitektur Engine

```text
Data Mentah (CSV / Excel)
        ↓
Konfigurasi Rule (YAML)
        ↓
Modul Cleaning Terpisah
        ↓
CleaningEngine (Orchestrator)
        ↓
Data Bersih + Log + Report

Struktur Folder
data_cleaning_rule_engine/
├── README.md
├── NOTE.md
├── configs/
│   └── client_rules.yaml
├── rules/
│   ├── missing_duplicates.yaml
│   ├── format_validation.yaml
│   └── text_mapping.yaml
├── src/
│   ├── __init__.py
│   ├── engine.py
│   ├── clean_missing.py
│   ├── clean_duplicates.py
│   ├── clean_format.py
│   ├── clean_text.py
│   └── utils.py
├── tests/
│   ├── test_missing.py
│   ├── test_duplicates.py
│   ├── test_format.py
│   └── test_text.py
└── sample_data/
    └── example_dataset.csv
