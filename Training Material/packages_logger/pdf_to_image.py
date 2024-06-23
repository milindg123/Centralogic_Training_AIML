import fitz  # PyMuPDF
from PIL import Image
import io

def convert_pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # Render page to an image
        pix = page.get_pixmap()
        
        # Convert the image to a PIL image
        image = Image.open(io.BytesIO(pix.tobytes()))

        # Save the image
        image_path = f"{output_folder}/page_{page_num + 1}.png"
        image.save(image_path)
        print(f"Saved {image_path}")

    pdf_document.close()

# Example usage
if __name__ == "__main__":
    # Path to the PDF file
    pdf_path = "00000.pdf"
    
    # Output folder to save images
    output_folder = "output_images"
    
    # Create output folder if it does not exist
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    convert_pdf_to_images(pdf_path, output_folder)
