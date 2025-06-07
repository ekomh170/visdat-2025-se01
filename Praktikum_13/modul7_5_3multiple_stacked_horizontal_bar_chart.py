import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Kode ini membuat multiple stacked horizontal bar chart untuk membandingkan penjualan smartphone dari beberapa merek (Samsung, Iphone, Vivo, Oppo) pada tahun 2023, 2024, dan 2025. Setiap bar merek terdiri dari tiga bagian yang ditumpuk secara horizontal, sehingga memudahkan analisis kontribusi penjualan tiap tahun pada total penjualan setiap merek selama tiga tahun berturut-turut.

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
plt.barh(y_pos, sales_2023, color='skyblue', label='2023')
plt.barh(y_pos, sales_2024, left=sales_2023, color='salmon', label='2024')
plt.barh(y_pos, sales_2025, left=np.array(sales_2023) + np.array(sales_2024), color='lime', label='2025')
plt.yticks(y_pos, brands)
plt.title('Penjualan Smartphone 2023-2025 (Multiple Stacked)')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Merek')
plt.legend()
st.pyplot(plt)