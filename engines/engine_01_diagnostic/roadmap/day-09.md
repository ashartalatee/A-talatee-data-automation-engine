# Day 09 — Column Quality Scoring

## Tujuan Hari Ini
Mengubah hasil diagnostic menjadi skor kualitas
per kolom agar risiko data dapat diringkas
dalam bentuk angka yang mudah dibaca.

Scoring ini bukan keputusan,
melainkan alat bantu diskusi.

## Yang Dikerjakan
- Membuat ColumnQualityScorer
- Menggabungkan missing value & encoding risk
- Menerapkan penalty berbasis threshold
- Menghasilkan skor 0–100 per kolom

## Output
- File: engine/scoring.py
- Laporan skor kualitas per kolom

## Pelajaran Penting
Skor bukan kebenaran,
tapi ringkasan risiko.

Angka hanya berguna
jika bisa dijelaskan asalnya.

## Dampak ke Agency
- Klien cepat melihat kolom bermasalah
- Engineer punya dasar objektif diskusi
- Mempermudah prioritas perbaikan

Kolom dinilai,
bukan langsung dataset.
