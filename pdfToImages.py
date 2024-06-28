import os
from pdf2image import convert_from_path
from tqdm import tqdm
from PyPDF2 import PdfReader

pdf_path = r"C:/Users/User/Documents/test/Secondary.pdf" 
output_dir = r"./imagesSecondary/" 

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the number of pages in the PDF
with open(pdf_path, "rb") as file:
    pdf = PdfReader(file)
    num_pages = len(pdf.pages)

# Process each page individually
for page_num in tqdm(range(num_pages), desc="Converting PDF to images", unit="page"):
    pages = convert_from_path(pdf_path, 300, first_page=page_num+1, last_page=page_num+1)
    for page in pages:
        image_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        page.save(image_path, 'PNG')

print("Conversion completed. Images saved in:", output_dir)
