from pdf2image import convert_from_path
from PIL import Image

def convert_pdf2image(pdf_file, dest_dir):
    file_name = pdf_file
    file_name = file_name.split("/")[-1]
    print(file_name)
    file_name = file_name.split("\\")[-1]
    file_name = file_name.split(".")[0]
    print(file_name)
    directory = dest_dir # dest_directory where the images will be stored
    
    image_list = []
    pages = convert_from_path(pdf_file)
    for i, page in enumerate(pages):
        page.save(f"./{directory}/{file_name}_{str(i)}.jpg", "JPEG")
        image_list.append(page)
    return(image_list)
        

