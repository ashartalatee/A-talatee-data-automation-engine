# Day 04 — Duplicate Row Diagnostic

## Tujuan Hari Ini
Mendeteksi dan mengukur duplicate row pada dataset
sebagai risiko tersembunyi yang sering tidak disadari.

Duplicate data tidak terlihat kosong,
tapi dapat menggandakan hasil analisis secara palsu.

## Yang Dikerjakan
- Membuat modul DuplicateRowDiagnostic
- Menghitung jumlah baris duplikat
- Menghitung persentase duplikat terhadap total data
- Menghasilkan ringkasan risiko duplikasi

## Output
- File: engine/diagnostics/duplicate.py
- Ringkasan duplicate row (jumlah & persentase)

## Pelajaran Penting
Data bisa terlihat lengkap,
tapi tetap berbahaya karena pengulangan.

Tanpa diagnostic duplikat,
angka yang terlihat “meyakinkan” bisa sepenuhnya salah.

## Dampak ke Agency
- Mencegah laporan dengan angka inflatif
- Mudah menjelaskan risiko ke klien non-teknis
- Menjadi dasar keputusan sebelum analisis lanjutan

Duplicate diagnostic menjaga kejujuran angka bisnis.
