# Day 06 — Encoding Diagnostic

## Tujuan Hari Ini
Mendeteksi potensi masalah encoding pada dataset
sebelum data digunakan oleh sistem lain
(API, database, automation, atau model).

Encoding error sering tidak terlihat di awal,
tapi fatal di tahap produksi.

## Yang Dikerjakan
- Membuat EncodingDiagnostic module
- Fokus pada kolom bertipe string/object
- Mendeteksi karakter non-ASCII sebagai sinyal risiko
- Menghitung persentase potensi masalah per kolom

## Output
- File: engine/diagnostics/encoding.py
- Laporan kolom rawan encoding error

## Pelajaran Penting
Data bisa terbaca hari ini,
tapi gagal besok saat pindah sistem.

Encoding bukan masalah bahasa,
tapi masalah kompatibilitas.

## Dampak ke Agency
- Mencegah error mendadak di pipeline klien
- Memberi peringatan dini sebelum integrasi
- Menambah nilai profesional tanpa cleaning data

Encoding diagnostic adalah asuransi diam-diam.
