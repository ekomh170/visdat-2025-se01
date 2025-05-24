# Displaying Latex
import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex(r'''(a+b)^2 = a^2 + b^2 + 2ab''')
st.latex(r'''\frac{\partial u}{\partial t} 
= h^2 \left( \frac{\partial^2 u}{\partial x^2} 
+ \frac{\partial^2 u}{\partial y^2} 
+ \frac{\partial^2 u}{\partial z^2} \right)''')
