import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Kode ini membuat stacked horizontal bar chart dengan kustomisasi warna, garis tepi, dan grid, untuk membandingkan penjualan smartphone dari beberapa merek (Samsung, Iphone, Vivo, Oppo) pada tahun 2023 dan 2024. Visualisasi ini memudahkan analisis kontribusi penjualan tiap tahun pada total penjualan setiap merek, serta memperjelas tampilan dengan grid dan warna berbeda.

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Data penjualan smartphone
brands = ['Samsung', 'Iphone', 'Vivo', 'Oppo']
sales_2023 = [500, 700, 300, 400]
sales_2024 = [550, 750, 350, 450]
sales_2025 = [600, 800, 400, 500]

y_pos = np.arange(len(brands))
plt.barh(brands, sales_2023, color='lightcoral', edgecolor='black', label='2023')
plt.barh(brands, sales_2024, left=sales_2023, color='lightskyblue', edgecolor='black', label='2024')
plt.title('Penjualan Smartphone (Kustom Stacked)')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Merek')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.legend()
st.pyplot(plt)