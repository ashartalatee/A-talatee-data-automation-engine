## Day 4 – Desain Rule Missing Value & Duplikat (YAML)
**Tujuan:** Buat rule tersentralisasi supaya reusable & modular.  
**Langkah:**
- Buat `rules/missing_duplicates.yaml`
- Struktur YAML:
  - `missing_values`: list kolom + strategy (mean, median, mode, constant)
  - `duplicates`: subset kolom + keep (first, last, none)
- Contoh YAML lengkap
- Template Python `src/clean_missing.py` untuk baca YAML & apply rules
- Test CSV untuk melihat hasil
**Output Nyata:**
- `rules/missing_duplicates.yaml`
- `src/clean_missing.py` template
- Test run CSV
**Fokus:** Rule tersentralisasi → reusable, modular, extendable.