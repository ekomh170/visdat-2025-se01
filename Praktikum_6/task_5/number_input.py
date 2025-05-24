import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 5. Forms
# Create number input 1
st.number_input("Enter your Number")

# Create a number input 2
num = st.number_input("Enter your Number", 0,10,5,2)
st.write("Min. Value is 0, \n Max. Value is 10")
st.write("Default Value is 5, \n Step Size is 2")
st.write("Total Value After Adding Number Entered with step value is:", num)