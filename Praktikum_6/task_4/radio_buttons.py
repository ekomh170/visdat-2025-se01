import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 4. Buttons and Sliders
# Radio Buttons
st.title('Creating Radio Buttons')
# Define Radion Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")  
else:
    st.write("You have selected Others.")