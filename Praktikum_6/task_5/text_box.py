import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 5. Forms
# Text Box
st.title("Text Box")
# Creating Text Box
name = st.text_input("Enter your name")
st.write ("Your name is ", name)
