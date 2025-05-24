import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 5. Forms
# Color
st.title("Select Color")
# Defining a color picker
color_code = st.color_picker("Select your color")
st.header(color_code)