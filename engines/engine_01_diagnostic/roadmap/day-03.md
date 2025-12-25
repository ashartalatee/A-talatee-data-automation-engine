# Day 03 — Missing Value Diagnostic

## Tujuan Hari Ini
Membuat engine mampu mendeteksi dan melaporkan
missing value secara objektif per kolom.

Missing value adalah sinyal awal bahwa data
berpotensi tidak siap dipakai untuk keputusan.

## Yang Dikerjakan
- Membuat modul MissingValueDiagnostic
- Menghitung missing value per kolom
- Menghitung persentase missing terhadap total baris
- Mengurutkan kolom berdasarkan tingkat risiko

## Output
- File: engine/diagnostics/missing.py
- DataFrame laporan missing value per kolom

## Pelajaran Penting
Missing value bukan sekadar angka kosong.
Ia adalah cerita tentang proses bisnis yang gagal,
input yang tidak konsisten, atau sistem yang bocor.

Mengisi missing tanpa memahami sumbernya
hanya menyembunyikan masalah.

## Dampak ke Agency
- Klien bisa melihat dengan jelas kolom bermasalah
- Mudah menjelaskan risiko tanpa jargon teknis
- Menjadi dasar keputusan: lanjut, perbaiki, atau tolak data

Diagnostic ini adalah “lampu merah” pertama dalam engine.
