#https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def extractText():
    """return the text in the image"""
    # Load an image
    img = Image.open("ss.png")

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(img)

    # return the extracted text
    return text;
