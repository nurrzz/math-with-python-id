# Math With Python ID (Indonesia)

Repo ini dibuat untuk membantu pembaca memahami konsep matematika dengan cara yang lebih praktis: melihat idenya, menerjemahkannya ke langkah berpikir, lalu menuliskannya sebagai kode Python.

Status repo: **draft catatan belajar**.

Materi di repo ini belum dimaksudkan sebagai course formal yang final. Isinya akan terus dirapikan, diperluas, dan diperbaiki seiring proses belajar.

Setiap materi membandingkan dua pendekatan:

1. **Tanpa library**, supaya proses berpikir dan rumusnya terlihat jelas.
2. **Dengan library**, supaya pembaca tahu cara yang lebih praktis digunakan saat membuat program sungguhan.

## Untuk Siapa Repo Ini?

Repo ini cocok untuk:

- Pelajar atau pemula yang ingin belajar matematika lewat kode.
- Orang yang merasa matematika lebih mudah dipahami kalau ada contoh praktis.
- Pembaca yang sedang belajar Python, data, machine learning, atau analisis.
- Pengajar yang butuh contoh sederhana untuk menjelaskan konsep matematika.

## Cara Belajar

Urutan belajar yang disarankan:

1. Mulai dari aritmetika untuk membiasakan operasi dasar.
2. Lanjut ke aljabar agar nyaman dengan variabel dan persamaan.
3. Masuk ke fungsi dan grafik untuk melihat hubungan input-output.
4. Pelajari trigonometri dan kalkulus dasar untuk memahami perubahan dan pola.
5. Lanjut ke statistika dan probabilitas untuk membaca data.
6. Gunakan aljabar linear sebagai fondasi tambahan untuk data dan machine learning.

Di tiap notebook, alurnya biasanya:

1. Pahami konsep matematika secara sederhana.
2. Lihat contoh manual dengan angka kecil.
3. Baca implementasi Python tanpa library.
4. Bandingkan dengan implementasi menggunakan library.
5. Simpan catatan penting untuk menghubungkan materi dengan topik berikutnya.

## Struktur Repo

```text
math-with-python-id/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01-aritmetika/
│   ├── 02-aljabar/
│   ├── 03-fungsi-grafik/
│   ├── 04-trigonometri/
│   ├── 05-kalkulus-dasar/
│   ├── 06-statistika/
│   ├── 07-probabilitas/
│   └── 08-aljabar-linear/
```

## Materi Awal

- Aritmetika
- Aljabar dasar
- Fungsi dan grafik
- Trigonometri
- Kalkulus dasar
- Statistika dasar
- Aljabar linear
- Probabilitas

## Notebook Yang Tersedia

Aritmetika:

- [Operasi Dasar](notebooks/01-aritmetika/01-operasi-dasar.ipynb)
- [Pecahan](notebooks/01-aritmetika/02-pecahan.ipynb)
- [Persen](notebooks/01-aritmetika/03-persen.ipynb)
- [Pangkat dan Akar](notebooks/01-aritmetika/04-pangkat-dan-akar.ipynb)

Aljabar dasar:

- [Variabel dan Ekspresi](notebooks/02-aljabar/01-variabel-dan-ekspresi.ipynb)
- [Persamaan Linear](notebooks/02-aljabar/02-persamaan-linear.ipynb)
- [Persamaan Kuadrat](notebooks/02-aljabar/03-persamaan-kuadrat.ipynb)
- [Sistem Persamaan Linear](notebooks/02-aljabar/04-sistem-persamaan-linear.ipynb)

Fungsi dan grafik:

- [Konsep Fungsi](notebooks/03-fungsi-grafik/01-konsep-fungsi.ipynb)
- [Fungsi Linear](notebooks/03-fungsi-grafik/02-fungsi-linear.ipynb)
- [Fungsi Kuadrat](notebooks/03-fungsi-grafik/03-fungsi-kuadrat.ipynb)
- [Domain, Range, dan Grafik](notebooks/03-fungsi-grafik/04-domain-range-dan-grafik.ipynb)

Trigonometri:

- [Sudut, Derajat, dan Radian](notebooks/04-trigonometri/01-sudut-derajat-radian.ipynb)
- [Sin, Cos, dan Tan](notebooks/04-trigonometri/02-sin-cos-tan.ipynb)
- [Identitas Trigonometri](notebooks/04-trigonometri/03-identitas-trigonometri.ipynb)
- [Grafik Trigonometri](notebooks/04-trigonometri/04-grafik-trigonometri.ipynb)

Kalkulus dasar:

- [Limit](notebooks/05-kalkulus-dasar/01-limit.ipynb)
- [Turunan Numerik](notebooks/05-kalkulus-dasar/02-turunan-numerik.ipynb)
- [Turunan Simbolik](notebooks/05-kalkulus-dasar/03-turunan-simbolik.ipynb)
- [Integral Numerik](notebooks/05-kalkulus-dasar/04-integral-numerik.ipynb)

Statistika dasar:

- [Rata-rata / Mean](notebooks/06-statistika/01-rata-rata.ipynb)
- [Median](notebooks/06-statistika/02-median.ipynb)
- [Modus](notebooks/06-statistika/03-modus.ipynb)
- [Varians dan Standar Deviasi](notebooks/06-statistika/04-varians-dan-standar-deviasi.ipynb)

Probabilitas:

- [Konsep Peluang](notebooks/07-probabilitas/01-konsep-peluang.ipynb)
- [Permutasi dan Kombinasi](notebooks/07-probabilitas/02-permutasi-dan-kombinasi.ipynb)
- [Probabilitas Bersyarat](notebooks/07-probabilitas/03-probabilitas-bersyarat.ipynb)
- [Simulasi Random](notebooks/07-probabilitas/04-simulasi-random.ipynb)

Aljabar linear:

- [Vektor](notebooks/08-aljabar-linear/01-vektor.ipynb)
- [Matriks](notebooks/08-aljabar-linear/02-matriks.ipynb)
- [Perkalian Matriks dan Dot Product](notebooks/08-aljabar-linear/03-perkalian-matriks-dan-dot-product.ipynb)
- [Determinan dan Invers](notebooks/08-aljabar-linear/04-determinan-dan-invers.ipynb)

Topik aritmetika menjadi fondasi awal sebelum masuk ke aljabar, fungsi, kalkulus, statistika, dan materi lain yang lebih besar.

## Menjalankan Contoh Kode

Buat virtual environment:

```bash
python3 -m venv .venv
```

Aktifkan virtual environment:

```bash
source .venv/bin/activate
```

Install library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

Buka notebook:

```bash
jupyter notebook
```

Lalu pilih file:

```text
notebooks/
```

Semua materi dan contoh kode ditulis langsung di dalam notebook.
