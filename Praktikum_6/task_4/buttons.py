import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Buttons
st.title('Creating a Button')
# Define a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the button!')
else:
    st.write('You have not clicked the button!')    