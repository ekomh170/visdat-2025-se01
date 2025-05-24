import streamlit as st
import datetime

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079)  
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 5. Forms
# Date
st.title("Date")

# Defining Date Function 1
st.date_input("Select Your Date")

# Defining Date Function 2
st.date_input("Select Your Date min and max", 
              value=datetime.date(1989, 12, 25),
              min_value=datetime.date(1989, 1, 1),
              max_value=datetime.date(2005, 12, 1)
              )
