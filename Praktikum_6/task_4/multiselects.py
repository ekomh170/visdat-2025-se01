import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Multiselects
st.title("Multi-selects")
# Define Multi-selects with pre-selection
hobbies = st.multiselect(
    "What are your hobbies",
    ["Reading", "Traveling", "Cooking", "Gaming"],
    default=["Reading", "Gaming"]
)