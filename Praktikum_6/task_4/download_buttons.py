import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Download Buttons
st.title("Download Buttons")
# Creating Download Buttons
down_button = st.download_button(
    label="Download Images",
    data="https://raw.githubusercontent.com/streamlit/streamlit/develop/examples/dog.jpg",
    file_name="dog.jpg",
    mime="image/jpeg",
)

