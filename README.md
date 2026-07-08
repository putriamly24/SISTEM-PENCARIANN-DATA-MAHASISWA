# SISTEM-PENCARIAN-DATA-MAHASISWA

## Implementasi Algoritma dan Struktur Data

**Topik 0 - Sistem Pencarian Data Mahasiswa**

Program ini merupakan implementasi algoritma dan struktur data menggunakan bahasa pemrograman Python untuk melakukan pengelolaan dan pencarian data mahasiswa.

Sistem ini menerapkan:

**Algoritma Pencarian:**
- Linear Search
- Binary Search

**Struktur Data:**
- Array/List
- Hash Map (Dictionary)

Data mahasiswa disimpan dalam file CSV dan digunakan sebagai dataset utama dalam proses pengolahan data.

---

# 1. Deskripsi Program

Sistem Pencarian Data Mahasiswa merupakan aplikasi berbasis **Command Line Interface (CLI)** yang digunakan untuk mengelola dan melakukan pencarian data mahasiswa berdasarkan NIM.

Program memiliki beberapa fitur utama:

- Membaca data mahasiswa dari file CSV.
- Menampilkan seluruh data mahasiswa.
- Menampilkan jumlah data mahasiswa.
- Menambahkan data mahasiswa baru.
- Mengubah data mahasiswa.
- Menghapus data mahasiswa.
- Melakukan pencarian menggunakan beberapa metode.
- Membandingkan performa algoritma pencarian berdasarkan waktu eksekusi.

---

# 2. Tujuan Implementasi

Tujuan dari pembuatan program ini adalah:

1. Mengimplementasikan struktur data Array/List dan Hash Map.
2. Menerapkan algoritma Linear Search dan Binary Search.
3. Membandingkan performa metode pencarian data.
4. Mengukur waktu eksekusi algoritma.
5. Memahami pengaruh kompleksitas algoritma terhadap proses pencarian.

---

# 3. Teknologi yang Digunakan

| Komponen | Keterangan |
|---|---|
| Bahasa Pemrograman | Python |
| Versi | Python 3 |
| Penyimpanan Data | File CSV |
| Struktur Data | List dan Dictionary |
| Algoritma | Linear Search dan Binary Search |
| Library | csv dan time |

---

# 4. Struktur Folder

```
Sistem-Pencarian-Data-Mahasiswa/
│
├── main.py
├── database_1000.csv
└── README.md
```

Keterangan:

| File | Fungsi |
|---|---|
| main.py | Program utama sistem pencarian mahasiswa |
| database_1000.csv | Dataset mahasiswa |
| README.md | Dokumentasi program |

---

# 5. Dataset

Program menggunakan file CSV sebagai sumber data mahasiswa.

Format dataset:

| Atribut | Keterangan |
|---|---|
| no | Nomor urut mahasiswa |
| nim | Nomor induk mahasiswa |
| nama | Nama mahasiswa |
| semester | Semester mahasiswa |
| ipk | Nilai IPK mahasiswa |
| program_kelas | Program kelas mahasiswa |

Contoh data:

```csv
no,nim,nama,semester,ipk,program_kelas
1,2101070095,AFRINIA JUITA NAHAK,1,3.89,REGULER
2,2106070004,BEBY GRASYA ELIM,5,3.88,REGULER
```

---

# 6. Struktur Data yang Digunakan

## 6.1 Array/List

Program menggunakan struktur data **List** untuk menyimpan seluruh data mahasiswa.

Implementasi:

```python
data_mahasiswa = [
    {
        "nim":"2101070095",
        "nama":"AFRINIA JUITA NAHAK"
    }
]
```

Fungsi List dalam program:

- Menyimpan kumpulan data mahasiswa.
- Menampilkan seluruh data.
- Melakukan pencarian Linear Search.
- Melakukan perubahan dan penghapusan data.

---

## 6.2 Hash Map (Dictionary)

Program menggunakan Dictionary sebagai Hash Map dengan NIM sebagai key.

Implementasi:

```python
hash_map = {mhs["nim"]: mhs for mhs in data_mahasiswa}
```

Fungsi Hash Map:

- Mempercepat pencarian berdasarkan NIM.
- Menyimpan pasangan key dan value data mahasiswa.

Kompleksitas rata-rata:

```
O(1)
```

---

# 7. Algoritma Pencarian

## 7.1 Linear Search

Linear Search melakukan pencarian dengan cara memeriksa data satu per satu sampai data ditemukan.

Fungsi:

```python
linear_search(data, target_nim)
```

Karakteristik:

- Tidak membutuhkan data terurut.
- Implementasi sederhana.
- Cocok untuk data kecil.

Kompleksitas:

```
Best Case    : O(1)
Average Case : O(n)
Worst Case   : O(n)
```

---

## 7.2 Binary Search

Binary Search melakukan pencarian dengan membagi data menjadi dua bagian secara berulang.

Fungsi:

```python
binary_search(data, target_nim)
```

Syarat:

- Data harus terurut berdasarkan NIM.

Kompleksitas:

```
Best Case    : O(1)
Average Case : O(log n)
Worst Case   : O(log n)
```

---

## 7.3 Hash Map Search

Hash Map Search menggunakan Dictionary untuk mencari data berdasarkan NIM.

Fungsi:

```python
hash_search(target_nim)
```

Keunggulan:

- Proses pencarian lebih cepat.
- Tidak perlu melakukan pemeriksaan satu per satu.

Kompleksitas:

```
Average Case : O(1)
Worst Case   : O(n)
```

---

# 8. Fitur Program

## 8.1 Kelola Dataset

Menu dataset memiliki fitur:

- Menampilkan semua data mahasiswa.
- Melihat jumlah data mahasiswa.
- Memuat ulang data dari CSV.

---

## 8.2 Tambah Data Mahasiswa

Pengguna dapat menambahkan data baru dengan memasukkan:

- NIM
- Nama
- Semester
- IPK
- Program Kelas

Data akan disimpan pada:

- List mahasiswa.
- Hash Map.

---

## 8.3 Ubah Data Mahasiswa

Pengubahan data dilakukan berdasarkan NIM.

Data yang dapat diubah:

- Nama.
- Semester.
- IPK.
- Program Kelas.

---

## 8.4 Hapus Data Mahasiswa

Penghapusan data dilakukan berdasarkan NIM.

Proses:

1. Mencari data melalui Hash Map.
2. Menghapus data dari List.
3. Menghapus data dari Dictionary.

---

## 8.5 Pencarian Data

Program menyediakan tiga metode pencarian:

### Linear Search

Melakukan pencarian secara berurutan.

### Binary Search

Melakukan pencarian dengan metode pembagian data.

### Hash Map Search

Melakukan pencarian menggunakan Dictionary.

---

## 8.6 Perbandingan Metode Pencarian

Program dapat membandingkan:

- Jumlah langkah pencarian.
- Waktu eksekusi.
- Metode dengan waktu tercepat.

Pengukuran waktu menggunakan:

```python
time.perf_counter()
```

Satuan waktu:

```
millisecond (ms)
```

---

# 9. Cara Menjalankan Program

## 1. Pastikan Python sudah terinstall

Cek versi Python:

```
python --version
```

---

## 2. Pastikan file berada dalam folder yang sama

```
main.py
database_1000.csv
README.md
```

---

## 3. Jalankan program

Buka terminal pada folder program:

```
python main.py
```

---

# 10. Tampilan Menu Utama

Program akan menampilkan menu:

```
==================================================
        SISTEM PENCARIAN DATA MAHASISWA
==================================================
1. Kelola Dataset
2. Tambah Data Mahasiswa
3. Ubah Data Mahasiswa
4. Hapus Data Mahasiswa
5. Pencarian Data
6. Tampilkan Semua Data
7. Keluar
==================================================
```

---

# 11. Contoh Hasil Pencarian

Contoh output:

```
[✓] Data ditemukan!

Metode: Linear Search
Langkah: 25
Waktu: 0.012300 ms

---------------------------------------------
No           : 25
NIM          : 2101070025
Nama         : NAMA MAHASISWA
Semester     : 4
IPK          : 3.75
Program Kelas: REGULER
---------------------------------------------
```

---

# 12. Analisis Kompleksitas

| Metode | Struktur Data | Kompleksitas |
|---|---|---|
| Linear Search | List | O(n) |
| Binary Search | List Terurut | O(log n) |
| Hash Map Search | Dictionary | O(1) rata-rata |

Berdasarkan kompleksitas teori:

- Hash Map memiliki waktu pencarian paling cepat karena menggunakan akses langsung berdasarkan key.
- Binary Search lebih efisien dibanding Linear Search pada data yang sudah terurut.
- Linear Search lebih sederhana tetapi membutuhkan pengecekan data satu per satu.

---

# 13. Kesimpulan

Program Sistem Pencarian Data Mahasiswa berhasil menerapkan konsep algoritma dan struktur data menggunakan Python.

Implementasi yang digunakan:

- List sebagai penyimpanan utama data mahasiswa.
- Dictionary sebagai Hash Map untuk pencarian berdasarkan NIM.
- Linear Search untuk pencarian data berurutan.
- Binary Search untuk pencarian data terurut.

Program ini dapat digunakan untuk melihat perbedaan performa algoritma pencarian berdasarkan jumlah langkah dan waktu eksekusi.

---

# 14. Author

**Implementasi Algoritma dan Struktur Data**

**Topik 0: Sistem Pencarian Data Mahasiswa**

Bahasa Pemrograman:

```
Python
```

Tahun:

```
2026
```
