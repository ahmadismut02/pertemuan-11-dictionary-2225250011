# Pertemuan 11: Dictionary/Map dan Pasangan Key-Value dalam Python

**Nama:** Ahmad Ismut Thoriequddin
**NIM:** 2225250011  
**Kelas:** 3A 
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa  
**Tahun Ajaran:** 2026/2027 Ganjil

## 🎯 Tujuan Pembelajaran

1. Memodelkan data pendidikan menggunakan dictionary dan pasangan *key-value*.
2. Mengakses dan memodifikasi data berdasarkan *key* secara tepat serta aman menggunakan method `get()`.
3. Menelusuri isi dictionary menggunakan `.keys()`, `.values()`, dan `.items()`.
4. Menggabungkan dictionary bersarang (*nested dictionary*) dengan list dan fungsi Python.
5. Menguji program di Visual Studio Code, mendokumentasikan hasil pengujian, dan mengunggahnya ke repositori GitHub.

## 🗂️ Struktur Folder Proyek

```text
pertemuan-11-dictionary-2225250011/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## 📊 Struktur Data

Data mahasiswa pada proyek ini dimodelkan menggunakan **dictionary bersarang** (*nested dictionary*) dengan ketentuan:

- **Key utama:** String berisi NIM, misalnya `"A001"` atau `"A002"`. NIM digunakan sebagai key karena unik untuk setiap mahasiswa.
- **Value:** Dictionary internal yang menyimpan detail mahasiswa:
  - `"nama"` *(String)*: nama lengkap mahasiswa.
  - `"kelas"` *(String)*: kelas mahasiswa, misalnya `"A"` atau `"B"`.
  - `"nilai"` *(Integer/Float)*: nilai akademik mahasiswa.

Contoh struktur:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
}
```

## 🚀 Cara Menjalankan Program

1. Buka terminal Visual Studio Code pada root folder proyek.
2. Pastikan Python 3 sudah terinstal.
3. Jalankan program praktik utama:

   ```bash
   python praktik/data_mahasiswa.py
   ```

   Pada sistem yang menggunakan perintah `python3`, jalankan:

   ```bash
   python3 praktik/data_mahasiswa.py
   ```

4. Jalankan skrip latihan satu per satu, misalnya:

   ```bash
   python latihan/01_dasar_dictionary.py
   python latihan/02_akses_get.py
   ```

## 🧪 Tabel Uji Coba (*Test Case*)

| Kasus Pengujian | Skenario Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Pencarian data ada | Cari NIM `"A003"` | Detail Citra (`nama`, `kelas`, `nilai`) ditampilkan | `Data A003: {'nama': 'Citra', 'kelas': 'B', 'nilai': 92}` | PASSED |
| Pencarian data tidak ada | Ubah `nim_cari` menjadi `"A999"` lalu jalankan program | Menampilkan `"Data tidak ditemukan"` tanpa `KeyError` | `Data tidak ditemukan` | PASSED |
| Pemberian nilai baru | Ubah nilai NIM `"A002"` dari `78` menjadi `82` | Nilai Budi menjadi `82` | `A002 -> {'nama': 'Budi', 'kelas': 'A', 'nilai': 82}` | PASSED |
| Penambahan mahasiswa | Tambahkan NIM `"A006"` atas nama Fajar | Data `"A006"` dapat diakses dan tercantum di rekap | `A006 -> {'nama': 'Fajar', 'kelas': 'B', 'nilai': 80}` | PASSED |
| Rekap data dan rata-rata | Iterasi seluruh data setelah perubahan | Enam mahasiswa tampil dan rata-rata terhitung | Seluruh data tampil; rata-rata nilai = **83.50** | PASSED |

> Rata-rata `83.50` dihitung dari nilai akhir `85, 82, 92, 74, 88, dan 80`.

## 📝 Refleksi dan Pembelajaran

- **Kesalahan akses key yang ditemukan:** Mengakses key yang tidak terdaftar secara langsung, misalnya `data[nim]` untuk `"A999"`, dapat menyebabkan `KeyError`.
- **Solusi penanganan:** Gunakan `data.get(nim)` atau periksa keberadaan key dengan `if nim in data:` sebelum mengaksesnya. Program praktik menggunakan `get()` agar pencarian data yang tidak ditemukan dapat ditangani dengan aman.
- **Koneksi materi:** Dictionary memudahkan penyimpanan dan pengelolaan data terstruktur di memori. Pemahaman pasangan key-value ini menjadi dasar untuk membaca dan menyimpan data secara permanen pada materi File Input-Output (Pertemuan 12).