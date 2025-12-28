# NOTE.md — Data Cleaning Rule Engine (Day 1–21)

Dokumen ini adalah catatan alur berpikir & pembangunan engine,
bukan tutorial teknis.
Tujuannya: saat repo ini dibuka kembali di masa depan,
aku langsung paham *kenapa* dan *bagaimana* engine ini dibangun.

---

## DAY 1 — Dataset Diagnostic (Level Kesadaran)
Fokus:
- Melihat data klien apa adanya
- Identifikasi missing value, duplikat, format kacau

Mindset:
> Jangan coding sebelum paham masalah nyata.

Output:
- README analisis data
- Dataset contoh dengan masalah disorot

---

## DAY 2 — Anomaly Analysis (Detail Kerusakan)
Fokus:
- Numeric aneh
- Date tidak valid
- Text inkonsisten

Mindset:
> Semua tipe kerusakan harus terlihat dulu sebelum bikin rule.

Output:
- Dokumentasi anomaly lanjutan

---

## DAY 3 — Project Structure (Engineer Mindset)
Fokus:
- Folderisasi profesional
- Pisahkan rule, code, config, test

Mindset:
> Script mati. Engine hidup.

Output:
- Struktur folder standar engine

---

## DAY 4 — Rule Design: Missing & Duplicate
Fokus:
- Rule berbasis YAML
- Centralized & reusable

Mindset:
> Logic harus diwariskan, bukan ditanam di code.

Output:
- missing_duplicates.yaml

---

## DAY 5 — Rule Design: Date & Numeric
Fokus:
- Validasi format
- Modular rule per tipe data

Mindset:
> Setiap tipe data = concern terpisah.

Output:
- format_validation.yaml

---

## DAY 6 — Implement Missing Rule
Fokus:
- Implementasi cleaning pertama
- Output parsial sudah bersih

Mindset:
> Progress nyata lebih penting dari sempurna.

Output:
- clean_missing.py

---

## DAY 7 — Implement Duplicate Rule
Fokus:
- Remove duplicate
- Standardisasi kolom

Mindset:
> Data rapi dimulai dari struktur.

Output:
- clean_duplicates.py

---

## DAY 8 — Implement Format Rule
Fokus:
- Date parsing
- Numeric validation

Mindset:
> Format rusak = data tidak bisa dipercaya.

Output:
- clean_format.py

---

## DAY 9 — Helper Utilities
Fokus:
- Logging
- Report per rule

Mindset:
> Engine tanpa jejak = tidak profesional.

Output:
- utils.py

---

## DAY 10 — CleaningEngine (Orchestrator)
Fokus:
- Integrasi semua rule
- Engine sebagai pengendali, bukan pelaku

Mindset:
> Engine mengatur, rule bekerja.

Output:
- engine.py (versi awal)

---

## DAY 11 — Internal Testing
Fokus:
- Dataset kecil
- Pastikan engine jalan

Mindset:
> Lebih baik ketemu bug sekarang daripada di klien.

Output:
- Cleaned dataset
- Test log awal

---

## DAY 12 — Debug & Refinement
Fokus:
- Perbaikan alur
- Konsistensi output

Mindset:
> Iterasi = kualitas.

Output:
- Engine lebih stabil

---

## DAY 13 — Client Config (Scalability)
Fokus:
- Rule selection via YAML
- Tidak hardcode klien

Mindset:
> Banyak klien, satu engine.

Output:
- client_rules.yaml

---

## DAY 14 — Multi-Client Testing
Fokus:
- Dataset berbeda
- Pastikan reusable

Mindset:
> Engine harus tahan variasi.

Output:
- Report multi-client

---

## DAY 15 — Text Cleaning Rule
Fokus:
- Case normalization
- Whitespace
- Value mapping (typo, bahasa)

Mindset:
> 80% data rusak itu text.

Output:
- text_mapping.yaml
- clean_text.py

---

## DAY 16 — Full Integration
Fokus:
- Text rule masuk engine
- Pipeline lengkap

Mindset:
> Semua rule hidup dalam satu alur.

Output:
- engine.py (versi final pipeline)

---

## DAY 17 — End-to-End Stress Test
Fokus:
- Dataset rusak berat
- Simulasi klien nyata

Mindset:
> Engine diuji di kondisi terburuk.

Output:
- Cleaned dataset final
- README_test_log.md

---

## DAY 18 — Documentation
Fokus:
- README profesional
- Jelaskan masalah & solusi

Mindset:
> Code tanpa narasi = aset mati.

Output:
- README.md siap publik

---

## DAY 19 — Refactor & Maintainability
Fokus:
- Naming
- Modularitas
- Kebersihan code

Mindset:
> Hormati future self.

Output:
- Codebase rapi & konsisten

---

## DAY 20 — Unit Testing
Fokus:
- Test per rule
- Quality gate

Mindset:
> Percaya diri datang dari test.

Output:
- test_missing.py
- test_duplicates.py
- test_format.py
- test_text.py

---

## DAY 21 — Release & Positioning
Fokus:
- Final commit
- GitHub push
- Positioning profesional

Mindset:
> Ini bukan latihan, ini aset.

Output:
- Release v1.0
- Repo siap dipakai, dijual, dikembangkan

---

## PENUTUP
Engine ini adalah:
- Alat kerja harian
- Aset karier
- Fondasi automation & data extraction

Rule boleh bertambah.
Engine boleh berkembang.
Mindset ini tidak boleh hilang.
