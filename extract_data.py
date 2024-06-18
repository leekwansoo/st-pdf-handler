import pdfplumber

def extract_pdf_data(feed):
    data = []
    with pdfplumber.open(feed) as pdf:
        pages = pdf.pages
        count = 0
        for p in pages:
            data.append(p.extract_tables())
            count += 1
    print(count)
    return data # build more code to return a dataframe

feed = "2023_movie_ranking.pdf"
print(feed)
data = extract_pdf_data(feed)

