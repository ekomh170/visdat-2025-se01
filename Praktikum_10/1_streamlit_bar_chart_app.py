# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================= #
# Data Dasar Mahasiswa
# ======================= #
data = {
    'Jurusan': ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa': [120, 150, 100, 80]
}
df = pd.DataFrame(data)

# ============================= #
# Streamlit App: st.bar_chart
# ============================= #
st.title("Basic Bar Chart - Jumlah Mahasiswa per Jurusan")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Menampilkan bar chart menggunakan fungsi bawaan Streamlit
st.bar_chart(df.set_index('Jurusan'))


# ============================================= #
# Streamlit App: Basic Bar Chart dengan Matplotlib
# ============================================= #
st.title("Basic Bar Chart Menggunakan Matplotlib")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Membuat bar chart dasar dengan matplotlib
fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menampilkan plot di Streamlit
st.pyplot(fig)


# ============================================= #
# Kustomisasi Warna dan Nilai pada Batang Chart
# ============================================= #
st.title("Kustomisasi Basic Bar Chart")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Membuat bar chart dengan warna berbeda-beda
fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'purple']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menambahkan nilai di atas setiap batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
            str(bar.get_height()), ha='center')

# Menampilkan chart
st.pyplot(fig)


# ========================================== #
# Multiple Bar Chart: Perbandingan 2023 & 2024
# ========================================== #
st.title("Multiple Basic Bar Chart")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Data untuk dua tahun
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

# Posisi dan lebar batang
x = range(len(data['Jurusan']))
width = 0.4

# Membuat grouped bar chart
fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

# Label dan keterangan
ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan'])
ax.legend()

# Tampilkan grafik
st.pyplot(fig)
