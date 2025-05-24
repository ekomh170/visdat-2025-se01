import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)


st.write('World!!!!')
st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""This is our Sub-header""")
st.caption("""This is our Caption""")

# Displaying Plain Text
st.text("Hi, \nPeople\t!!!!!!!!!")
st.text('Welcome to')
st.text(""" Streamlit's World""")

# Displaying Markdown
st.markdown("# Hi,\n ***People*** \t!!!!!!!!!")
st.markdown("## Welcome to")
st.markdown("### Streamlit's World")
