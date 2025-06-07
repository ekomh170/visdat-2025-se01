import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Kode ini membuat stacked horizontal bar chart untuk membandingkan penjualan smartphone dari beberapa merek (Samsung, Iphone, Vivo, Oppo) pada tahun 2023 dan 2024. Setiap bar merek terdiri dari dua bagian yang ditumpuk secara horizontal, sehingga memudahkan analisis kontribusi penjualan tiap tahun pada total penjualan setiap merek. Visualisasi ini membantu melihat perbandingan penjualan antar merek dan antar tahun secara jelas.

brands = ['Samsung', 'Iphone', 'Vivo', 'Oppo']
sales_2023 = [500, 700, 300, 400]
sales_2024 = [550, 750, 350, 450]
sales_2025 = [600, 800, 400, 500]

y_pos = np.arange(len(brands))
plt.barh(brands, sales_2023, color='skyblue', label='2023')
plt.barh(brands, sales_2024, left=sales_2023, color='salmon', label='2024')
plt.title('Penjualan Smartphone Stacked (2023 & 2024)')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Merek')
plt.legend()
st.pyplot(plt)