# Day 02 — Data Loader (Reading Data Safely)

## Tujuan Hari Ini
Membangun satu pintu resmi bagi engine untuk membaca data mentah
tanpa mengubah, memperbaiki, atau memanipulasi isi dataset.

Loader adalah gerbang integritas seluruh diagnostic engine.

## Yang Dikerjakan
- Membuat DataLoader class
- Validasi keberadaan file & format
- Support CSV dan Excel
- Error handling eksplisit jika data gagal dibaca
- Menolak dataset kosong

## Output
- File: engine/loader.py
- Loader stabil untuk input data mentah

## Pelajaran Penting
Kesalahan terbesar dalam data bukan di analisis,
tapi saat data pertama kali dibaca.

Jika engine diam-diam "memperbaiki" data saat loading,
maka semua diagnostic setelahnya tidak jujur.

Loader yang baik lebih sering berkata "tidak".

## Dampak ke Agency
- Klien tahu sejak awal apakah datanya layak dianalisis
- Scope kerja jelas (error teknis ≠ analisis)
- Menghindari jam kerja sia-sia karena data gagal dibaca

Loader ini melindungi reputasi agency sebelum laporan dibuat.
