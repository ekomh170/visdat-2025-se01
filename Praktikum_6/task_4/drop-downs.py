import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Dropdown
st.title('Create Dropdown')
# Creating Dropdown
hobby = st.selectbox('Pilih Hobi : ', ['Membaca', 'Menulis', 'Berenang', 'Bersepeda'])
st.write('Hobi yang dipilih adalah : ', hobby)