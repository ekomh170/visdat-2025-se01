import streamlit as st
import numpy as np

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

st.title("Container")
with st.container():
    st.write("Element Inside Container")
    # Defining Chart Element
    st.line_chart(np.random.rand(40, 4))
st.write("Element Outside Container")
