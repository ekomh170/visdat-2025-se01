import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ========================
# Gambar 1: Stacked Vertical Bar Chart (Gender per Store)
# ========================

st.title("Stacked Vertical Bar Chart")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Data populasi berdasarkan gender
stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

# Grafik
fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male_population, label='Male', color='blue')
ax.bar(x, female_population, bottom=male_population, label='Female', color='pink')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()
st.pyplot(fig)
# Grafik batang bertumpuk yang menunjukkan jumlah populasi laki-laki dan perempuan di setiap toko.

# ========================
# Gambar 2: Stacked Vertical Bar Chart (Produk per Store)
# ========================

st.subheader("Membuat Stacked Vertical Bar Chart dengan Matplotlib")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Data penjualan produk
product_a_sales = [200, 250, 300]
product_b_sales = [150, 300, 250]

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a_sales, label='Product A', color='blue')
ax.bar(x, product_b_sales, bottom=product_a_sales, label='Product B', color='green')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_title('Sales Transactions by Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()
st.pyplot(fig)
# Grafik batang bertumpuk yang membandingkan penjualan Product A dan Product B di setiap toko.

# ========================
# Gambar 3: Kustomisasi Label di Stacked Bar
# ========================

st.subheader("Kustomisasi Stacked Vertical Bar Chart")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Tambahkan label ke setiap batang
for i in range(len(x)):
    plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')
    plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='black')

st.pyplot(fig)
# Grafik batang bertumpuk dengan label pada setiap batang untuk memperjelas jumlah masing-masing produk.

# ========================
# Gambar 4: Multiple Stacked Vertical Bar Chart (Q1 vs Q2)
# ========================

st.subheader("Multiple Stacked Vertical Bar Chart")

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Data populasi per kuartal
q1_male = [150, 180, 160]
q1_female = [130, 100, 120]
q2_male = [170, 200, 175]
q2_female = [135, 210, 100]

fig, ax = plt.subplots()
x = np.arange(len(stores))
bar_width = 0.3

# Q1 Bars
ax.bar(x - bar_width / 2, q1_male, label='Q1 Male', color='lightblue', width=bar_width)
ax.bar(x - bar_width / 2, q1_female, bottom=q1_male, label='Q1 Female', color='pink', width=bar_width)

# Q2 Bars
ax.bar(x + bar_width / 2, q2_male, label='Q2 Male', color='blue', width=bar_width)
ax.bar(x + bar_width / 2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=bar_width)

ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store (Multiple Quarter)')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()
st.pyplot(fig)
# Grafik batang bertumpuk ganda yang membandingkan populasi laki-laki dan perempuan di setiap toko untuk dua kuartal berbeda (Q1 dan Q2).
