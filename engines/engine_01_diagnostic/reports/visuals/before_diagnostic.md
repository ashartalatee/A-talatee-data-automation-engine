# BEFORE — Tanpa Data Diagnostic

## Kondisi Umum
Data diterima dari klien dalam format CSV
dan langsung digunakan untuk analisis.

Tidak ada pemeriksaan kualitas data awal.

## Asumsi yang Dipakai
- Data lengkap
- Tidak ada duplikat transaksi
- Nama produk konsisten
- Angka penjualan dapat dipercaya

## Risiko Tersembunyi
- Duplikat transaksi menyebabkan
  perhitungan revenue berlebih
- Missing quantity membuat
  total penjualan bias
- Nama kolom tidak konsisten
  menyebabkan agregasi salah
- Encoding error merusak hasil laporan

## Dampak ke Keputusan
Keputusan bisnis dibuat
berdasarkan data yang belum tervalidasi.

Potensi:
- Salah estimasi performa produk
- Forecast keliru
- Keputusan operasional tidak akurat
