import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Progress Bar
import time
st.write("Progress Bar")
download = st.progress(0)
for persentanse in range(100):
    time.sleep(0.1)
    download.progress(persentanse + 1)
st.write("Download Complete")