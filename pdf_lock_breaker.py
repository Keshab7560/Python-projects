
pip install pypdf

from pypdf import PdfReader

# Define the path to your PDF and the password
pdf_path = 'path/to/your/protected.pdf'
password = 'your_password'

# Open the PDF file
try:
    reader = PdfReader(pdf_path)
    if reader.is_encrypted:
        # Try to decrypt the PDF with the password
        reader.decrypt(password)

    # Now you can access the content
    for page in reader.pages:
        print(page.extract_text())

except Exception as e:
    print(f"An error occurred: {e}")
