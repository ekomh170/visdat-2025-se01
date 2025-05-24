# Displaying Python Code
import streamlit as st

st.markdown("""
### Kelompok Visualisasi Data:  
- Eko Muchamad Haryono  (0110223079) 
- Raka Muhammad Rabbani (0110223050)
""", unsafe_allow_html=True)

st.subheader("""Python Code""")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
    public static void main(String args[]) {
        System.out.println("Hello World");
    }
}""", language='javascript')  # Perhatikan: sebenarnya ini Java, tapi diberi label 'javascript'

st.subheader("""JavaScript Code""")
st.code("""<p id="demo"></p>
<script>
try {
    addAlert("Welcome guest!");
} catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script>""")
