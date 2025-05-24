import streamlit as st
import numpy as np

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

st.title("Out of Order Container")
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
# Now insert a few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.rand(40, 4))
