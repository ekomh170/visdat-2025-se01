import matplotlib.pyplot as plt

# Data Mahasiswa Atau Pengerjaan Nilai UTS
nama = "Eko Muchamad Haryono"
nim = "0110223079"
prodi = "Teknik Informatika"
peminatan = "Software Engineering"

# Data nilai mata kuliah
mata_kuliah = [
    "Visualisasi Data", 
    "Pendidikan Agama", 
    "Bahasa Indonesia", 
    "Pemrograman Web 1", 
    "Big Data", 
    "Basis Data", 
    "Dasar-Dasar Pemrograman"
]

nilai = [90, 75, 85, 70, 80, 95, 88]  # Nilai random atau yang sesuai

# Membuat grafik horizontal
plt.barh(mata_kuliah, nilai, color='salmon', edgecolor='black')

# Menambahkan judul dan label
plt.title(f"Nilai Kuliah {nama} ({nim})\nProdi: {prodi} | Peminatan: {peminatan}", fontsize=12, fontfamily='Times New Roman')
plt.xlabel("Nilai Akhir Kuliah", fontsize=12, fontfamily='Times New Roman')
plt.ylabel("Mata Kuliah", fontsize=12, fontfamily='Times New Roman')

# Menampilkan grafik
plt.show()
