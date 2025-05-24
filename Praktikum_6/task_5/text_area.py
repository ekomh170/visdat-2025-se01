import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 5. Forms
# Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""", input_text)