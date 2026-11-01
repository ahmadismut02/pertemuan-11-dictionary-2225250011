"""Praktik mengelola data beberapa mahasiswa dengan dictionary."""

def cari_mahasiswa(data, nim):
  return data.get(nim)


def rata_rata_nilai(data):
  if len(data) == 0:
    return 0
  total = 0
  for info in data.values():
    total += info["nilai"]
  return total / len(data)


# 1. Inisialisasi Dictionary Data Mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88},
}

# 2. Uji Pencarian (Test Case)
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
  print(f"Data {nim_cari}: {hasil}")
else:
  print("Data tidak ditemukan")

# 3. Penambahan Data Mahasiswa Baru
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 80}

# 4. Pembaruan Nilai Mahasiswa
data_mahasiswa["A002"]["nilai"] = 82

# 5. Menampilkan Seluruh Data & Rata-rata Kelas
print("\nRekap Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
  print(f"{nim} -> {info}")

print(f"\nRata-rata nilai kelas = {rata_rata_nilai(data_mahasiswa):.2f}")