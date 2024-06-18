from spire.pdf.common import *
from spire.pdf import *

def split_by_range(startpage, endpage, title, max_page, input_document):
    # Create a PdfDocument object
    document = input_document
    pdf = PdfDocument()
    # Load a PDF file
    pdf.LoadFromFile(document)
    #pdf.LoadFromFile("documents/100년후.pdf")

    # input data for pdf split

    page_count = pdf.Pages.Count
    startpage = startpage
    endpage = endpage
    max_page = max_page
    # if max_page is larger than page_count replace with page_count
    if endpage > page_count:
        print("page_count, max_page", page_count, max_page)
        endpage = page_count
        print("page_count, max_page", page_count, max_page)
        
    title = title
    n=startpage # starting page number
    m= max_page-1  # number of pages in a pdf file -1 (max pages = 10)
             
    remain_page = endpage-startpage + 1
    last_page = page_count
    files = []
    for page in range(startpage-1, last_page-1):
        # Create two new PdfDocument objects
        newPdf_1 = PdfDocument()
       
        print("remainpage, max_page", remain_page, m+1)
        if remain_page <= m+1:  # max_pages for output pdf file
            
            print("startpage, remaining page", n, remain_page)
            newPdf_1.InsertPageRange(pdf, n-1, endpage-1)
            # Insert the rest pages of the source file into the second PDF file
        
            # Save the resulting files
            newPdf_1.SaveToFile(f"documents/{title}_{n}.pdf")
            file_path = f"documents/{title}_{n}.pdf" 
            files.append(file_path)
            break
        else:
            # Insert number of m pages of the source file into the first PDF file
            last_page = n+m
            print("startpage, endpage", n, last_page)
            newPdf_1.InsertPageRange(pdf, n-1, last_page-1)
            newPdf_1.SaveToFile(f"documents/{title}_{n}.pdf")
            
            file_path = f"documents/{title}_{n}.pdf" 
            files.append(file_path)
            # Insert the rest pages of the source file into the second PDF file
            n = n+m+1
            remain_page = remain_page - (m + 1) # Number of page in a file
            # print(remain_page)
    
    # Close the PdfDocument objects
    pdf.Close()
    newPdf_1.Close()
    
    return (files, page_count)
    


    
