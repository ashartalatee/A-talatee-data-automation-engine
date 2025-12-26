# Day 10 — Dataset Quality Score

## Tujuan Hari Ini
Menghasilkan satu skor kualitas dataset
sebagai ringkasan kondisi data secara keseluruhan
berdasarkan skor tiap kolom.

Skor ini adalah ringkasan,
bukan keputusan akhir.

## Yang Dikerjakan
- Membuat DatasetQualityScorer
- Menghitung rata-rata skor kolom
- Menyertakan skor kolom terburuk
- Menyajikan skor dataset dalam format ringkas

## Output
- Update file: engine/scoring.py
- Skor kualitas dataset (0–100)

## Pelajaran Penting
Rata-rata yang baik
tidak menghapus masalah ekstrem.

Skor dataset harus jujur
tentang bagian terlemahnya.

## Dampak ke Agency
- Klien langsung paham kondisi umum data
- Diskusi fokus, bukan defensif
- Menjadi pintu masuk keputusan bisnis

Hari ini engine bisa menjawab:
"Secara keseluruhan, data ini bernilai X."
