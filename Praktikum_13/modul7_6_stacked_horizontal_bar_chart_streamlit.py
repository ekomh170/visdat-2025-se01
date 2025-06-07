import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==================== Gambar 1 Code ====================

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# Contoh data penjualan
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, label='2022', color='skyblue')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='orange')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Smartphone Sales by Brand')
    ax.legend()
    return fig

# Render chart di Streamlit
st.title("Smartphone Sales Visualization")
st.pyplot(create_stacked_bar_chart())

# Gambar 1 menampilkan stacked horizontal bar chart penjualan smartphone per brand untuk tahun 2022 dan 2023. Setiap bar terdiri dari dua bagian yang ditumpuk secara horizontal, sehingga memudahkan analisis kontribusi penjualan tiap tahun pada total penjualan setiap brand.

# ==================== Gambar 2 Code ====================

# Informasi kelompok
st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

def create_custom_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, label='2022', color='blue', edgecolor='black', hatch='//')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='green', edgecolor='black', hatch='\\\\')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Customized Smartphone Sales by Brand')
    ax.legend()

    # Tambahkan anotasi
    for i in range(len(brands)):
        ax.text(sales_2022[i] / 2, i, f"{sales_2022[i]}", va='center', color='white')
        ax.text(sales_2022[i] + sales_2023[i] / 2, i, f"{sales_2023[i]}", va='center', color='black')

    return fig

st.pyplot(create_custom_stacked_bar_chart())
