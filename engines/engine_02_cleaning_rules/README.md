# Data Cleaning Rule Engine

## Deskripsi
Engine ini dirancang untuk melakukan **data cleaning berbasis rule** yang reusable dan scalable.  
Cocok untuk berbagai klien dengan dataset yang berbeda-beda, siap digunakan di pipeline ETL atau integrasi automation.

## Fitur
- Cleaning missing values, duplikat, dan format tidak konsisten
- Modular: tiap rule dapat diaktifkan/matikan via config
- Reusable: bisa dipakai untuk banyak dataset berbeda
- Logging & reporting per rule
- Unit tests untuk tiap rule

## Struktur Folder
- `configs/` → konfigurasi rule per klien
- `rules/` → definisi rule (JSON/YAML)
- `src/` → kode engine & modul
- `tests/` → unit tests tiap rule
- `sample_data/` → contoh dataset untuk testing

## Cara Pakai
1. Install dependencies
```bash
pip install -r requirements.txt
