import streamlit as st 
from extract_data import extract_data
import json

uploaded_file = st.file_uploader('Choose your json file')
if uploaded_file is not None:
   
    read_json_file = json.load(uploaded_file)
    st.write(read_json_file)