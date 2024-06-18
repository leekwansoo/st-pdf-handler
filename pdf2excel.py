from spire.pdf.common import *
from spire.pdf import *

# Create an object of the PdfDocument class
pdf = PdfDocument()
# Load a PDF file
pdf.LoadFromFile("2023_movie_ranking.pdf")

# Save the PDF file to Excel XLSX format
pdf.SaveToFile("2023_movie_ranking.xlsx", FileFormat.XLSX)
# Close the PdfDocument object
pdf.Close()