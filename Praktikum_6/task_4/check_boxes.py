import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Check Boxes
st.title('Creating CheckBoxes')
st.write('Select your hobbies')
# Define CheckBoxes
check_1 = st.checkbox('Reading')
check_2 = st.checkbox('Traveling')
check_3 = st.checkbox('Cooking')
check_4 = st.checkbox('Gaming')