
import streamlit as st
st.title('Read TXT')
uploaded_file = st.file_uploader(label="Choose a TXT file", type=['.txt'])

if uploaded_file is not None:
  # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

col1, col2 = st.columns([0.5,1.5])

with col1:
    st.button('Previous TXT')
with col2:
    st.button('Next TXT')