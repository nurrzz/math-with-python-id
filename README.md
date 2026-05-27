# Math With Python ID

Math With Python ID adalah repo belajar matematika menggunakan Python untuk pembaca Indonesia.

Repo ini dibuat untuk membantu pembaca memahami konsep matematika dengan cara yang lebih praktis: melihat idenya, menerjemahkannya ke langkah berpikir, lalu menuliskannya sebagai kode Python.

Setiap materi membandingkan dua pendekatan:

1. **Tanpa library**, supaya proses berpikir dan rumusnya terlihat jelas.
2. **Dengan library**, supaya pembaca tahu cara yang lebih praktis digunakan saat membuat program sungguhan.

Tujuan repo ini bukan hanya membuat pembaca bisa menjalankan kode, tapi juga memahami hubungan antara konsep matematika dan cara komputer menyelesaikannya.

## Untuk Siapa Repo Ini?

Repo ini cocok untuk:

- Pelajar atau pemula yang ingin belajar matematika lewat kode.
- Orang yang merasa matematika lebih mudah dipahami kalau ada contoh praktis.
- Pembaca yang sedang belajar Python, data, machine learning, atau analisis.
- Pengajar yang butuh contoh sederhana untuk menjelaskan konsep matematika.

## Cara Belajar

Untuk setiap topik, alurnya seperti ini:

1. Pahami konsep matematika secara sederhana.
2. Lihat contoh manual dengan angka kecil.
3. Baca implementasi Python tanpa library.
4. Bandingkan dengan implementasi menggunakan library.
5. Kerjakan latihan.
6. Cek pembahasan di notebook setelah mencoba sendiri.

## Struktur Repo

```text
math-with-python-id/
├── README.md
├── requirements.txt
├── notebooks/
│   └── 03-statistika/
└── assets/
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

## Materi Pertama

Mulai dari:

[Notebook Rata-rata / Mean](notebooks/03-statistika/01-rata-rata.ipynb)

Topik ini sederhana, tapi bagus untuk melihat pola utama repo ini: dari konsep matematika, ke kode Python manual, lalu ke versi dengan library.

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
notebooks/03-statistika/01-rata-rata.ipynb
```

Semua materi, contoh kode, latihan, dan pembahasan ditulis langsung di dalam notebook.

## Prinsip Penulisan

Materi di repo ini ditulis dengan bahasa yang jelas, praktis, dan ramah untuk pemula. Penjelasan akan dibuat pelan-pelan, tanpa menganggap pembaca sudah nyaman dengan matematika atau coding.

Fokusnya bukan menghafal rumus, tapi memahami ide di baliknya.
