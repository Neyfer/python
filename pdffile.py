import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tqdm import tqdm

img_dir = r"./logos"  # Directory containing the images
output_pdf = r"C:/Users/User/Documents/test/Secondary.pdf"  # Output PDF file

# Number of images
num_images = 3  

# Ensure the output directory exists
output_dir = os.path.dirname(output_pdf)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

c = canvas.Canvas(output_pdf, pagesize=letter)
width, height = letter

gap_size = 14  

image_height = (height / 2) - (gap_size / 2)

# Loop through images with progress bar
for i in tqdm(range(1, num_images + 1, 2), desc="Creating PDF from images"):
    if i <= num_images:
        img_file_top = os.path.join(img_dir, f"image{i}.png")
        c.drawImage(img_file_top, 0, height / 2 + (gap_size / 2), width=width, height=image_height)
    if i + 1 <= num_images:
        img_file_bottom = os.path.join(img_dir, f"image{i + 1}.png")
        c.drawImage(img_file_bottom, 0, 0, width=width, height=image_height)
    c.showPage()

# Save the PDF
c.save()

print(f"PDF saved as {output_pdf}")