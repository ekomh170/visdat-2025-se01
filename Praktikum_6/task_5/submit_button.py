import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

# 5. Forms
# Submit Button
my_form = st.form(key='form')
a = my_form.text_input("Enter any text")
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)