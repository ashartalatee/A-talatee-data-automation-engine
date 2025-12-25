# Day 05 — Schema Consistency Diagnostic

## Tujuan Hari Ini
Menganalisis struktur dataset (schema) untuk memastikan
data memiliki bentuk yang konsisten dan dapat diprediksi.

Schema adalah kontrak tak tertulis antara data dan sistem.

## Yang Dikerjakan
- Membuat SchemaDiagnostic module
- Melaporkan nama kolom dan tipe data
- Menghitung jumlah data non-null per kolom
- Menghitung nilai unik per kolom

## Output
- File: engine/diagnostics/schema.py
- Laporan schema dataset per kolom

## Pelajaran Penting
Data bisa penuh dan tidak duplikat,
tapi tetap berbahaya jika schema-nya tidak konsisten.

Tipe data yang salah
sering menjadi akar bug paling mahal.

## Dampak ke Agency
- Klien bisa melihat struktur data secara transparan
- Mudah mendeteksi kolom yang tidak sesuai fungsi
- Menjadi dasar penolakan data yang tidak stabil

Schema diagnostic menjaga fondasi teknis proyek klien.
