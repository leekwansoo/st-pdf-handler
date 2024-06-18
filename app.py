import streamlit as st 
from extract_data import extract_pdf_data
from pdf_splitter import split_by_range
from pdf2img import *
import tempfile
import os

st.title("PDF File Handler")

st.header("PDF File-Splitter")
uploaded_file = st.file_uploader("File upload", type="pdf", key="splitter")

if uploaded_file:
    #temp_dir = tempfile.mkdtemp()
    #cwd_dir = os.getcwd()
    file_path = os.path.join(uploaded_file.name)
    file_path = uploaded_file.name
    file_name = uploaded_file.name
    print(file_name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
        
    file_path = os.getcwd()
    print(file_path)
    files_list = os.listdir(file_path) 

    with st.form("PDF_Splitter"):
        col1, col2, col3 = st.columns(3)
        with col1:
            startpage = st.text_input("enter startpage", max_chars =3)
        with col2:    
            endpage = st.text_input("enter endpage", max_chars =3)
        with col3:   
            max_page = st.text_input("enter pages in a pdf_file", max_chars =3)
            
        submitted = st.form_submit_button("Submit")
        if submitted: 
            startpage = int(startpage)
            endpage = int(endpage)
            max_page = int(max_page)      
            file_path = file_name
            file_name_prefix = file_name.split(".")[0]
            st.write(startpage, endpage, file_name_prefix, max_page, file_path)
            # process for splitting PDF file
            # splitted pdf files are stored in the documents directory
            files, page_count = split_by_range(startpage, endpage, file_name_prefix, max_page, file_path)
            
            st.write("Number of pages in uploaded PDF", page_count)  
            for file_path in files:
                st.write(file_path)
                
st.divider()
st.markdown("""***""")
st.header("PDF2JPG Converter")
uploaded_file = st.file_uploader("File upload", type="pdf", key="image_converter")

if uploaded_file:
    #temp_dir = tempfile.mkdtemp()
    cwd_dir = os.getcwd()
    file_path = os.path.join(cwd_dir, uploaded_file.name)
    file_name = uploaded_file.name
    print(file_path, file_name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    directory = st.text_input("enter the destination_directory")    
                
    button_pressed = st.button("Process")
    if button_pressed: 
        image_list = convert_pdf2image(file_path, directory)
        
        #for image in image_list:
        cwd = os.getcwd()
        st.write(f"generated images are stored at {directory}")
            
    
