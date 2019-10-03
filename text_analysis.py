import cv2
import pytesseract
from PIL import Image
import os

def extract_text(file, language):
    image = cv2.imread(file)
    # image pre-processing : grayscale to improve the OCR result
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = "tmp.png"
    cv2.imwrite(filename, gray)
    # OCR application
    text = pytesseract.image_to_string(Image.open(filename), lang=language)
    # remove tmp file
    os.remove(filename)
    print("[Debug] - Extracted text:\n{}".format(text))
    return text
        
