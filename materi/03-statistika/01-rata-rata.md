# Rata-rata / Mean

Rata-rata adalah salah satu konsep paling dasar dalam statistika.

Kita memakai rata-rata saat ingin mendapatkan satu nilai yang mewakili sekumpulan data. Misalnya, dari beberapa nilai ujian, kita ingin tahu gambaran umumnya.

## Ide Matematika

Rumus rata-rata:

```text
rata-rata = jumlah semua data / banyak data
```

Contoh:

```text
data = 70, 80, 90
jumlah semua data = 70 + 80 + 90 = 240
banyak data = 3
rata-rata = 240 / 3 = 80
```

Jadi, rata-ratanya adalah `80`.

## Cara Berpikirnya

Kalau diterjemahkan ke langkah sederhana:

1. Siapkan data.
2. Jumlahkan semua angka.
3. Hitung berapa banyak angka di dalam data.
4. Bagi total angka dengan banyak data.

Langkah ini bisa langsung diterjemahkan ke Python.

## Python Tanpa Library

```python
data = [70, 80, 90]

total = 0

for nilai in data:
    total += nilai

rata_rata = total / len(data)

print(rata_rata)
```

Pada kode di atas:

- `total` digunakan untuk menyimpan jumlah semua nilai.
- `for nilai in data` membaca setiap angka satu per satu.
- `len(data)` menghitung banyak data.
- `total / len(data)` menghitung rata-rata.

Versi tanpa library membantu kita melihat bahwa rata-rata sebenarnya hanya proses menjumlahkan data, lalu membaginya dengan jumlah data.

## Python Dengan Library

Dengan NumPy, kodenya bisa menjadi lebih singkat:

```python
import numpy as np

data = [70, 80, 90]
rata_rata = np.mean(data)

print(rata_rata)
```

NumPy sering dipakai dalam data analysis, machine learning, dan komputasi numerik karena cepat dan praktis untuk data yang lebih besar.

## Perbandingan

| Pendekatan | Kelebihan | Cocok Untuk |
| --- | --- | --- |
| Tanpa library | Membantu memahami proses dari awal | Belajar konsep |
| Dengan library | Lebih ringkas dan siap dipakai | Data yang lebih besar atau project nyata |

Kalau sedang belajar, mulai dari versi tanpa library dulu. Setelah paham idenya, baru gunakan library agar pekerjaan lebih cepat dan rapi.

## Catatan Penting

Rata-rata mudah dihitung, tapi tidak selalu cukup untuk memahami data.

Contoh:

```text
data A = 70, 80, 90
data B = 10, 80, 150
```

Keduanya punya rata-rata `80`, tapi penyebaran datanya berbeda. Karena itu, setelah belajar rata-rata, kita juga perlu belajar median, modus, varians, dan standar deviasi.
