# ======================== Gambar Pertama ========================
# Scatter Plot Visualisasi hubungan suhu dan penjualan tanpa kustomisasi.

import streamlit as st
import matplotlib.pyplot as plt

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

st.subheader("1. Scatter Plot Dasar")

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Scatter plot menggunakan Matplotlib
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='blue')
ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')

# Tampilkan di Streamlit
st.pyplot(fig)

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# ======================== Gambar Kedua ========================
# Scatter Plot Dengan Kustomisasi Menggunakan warna, ukuran, edge, dan transparansi.
st.subheader("2. Scatter Plot dengan Kustomisasi")

# Kustomisasi scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.grid(True)

# Tampilkan di Streamlit
st.pyplot(fig)

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# ======================== Gambar Ketiga ========================
# Scatter Plot Berdasarkan Kategori Hari Menampilkan perbandingan antara hari kerja dan akhir pekan.
st.subheader("3. Scatter Plot Berdasarkan Kategori Hari")

# Data tambahan untuk kategori hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Multiple scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
ax.set_title('Penjualan Es Krim Berdasarkan Hari')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.legend()
ax.grid(True)

# Tampilkan di Streamlit
st.pyplot(fig)
