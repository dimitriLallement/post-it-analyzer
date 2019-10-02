import cv2
import pytesseract
from PIL import Image

def extract_text(image, language):
    # image pre-processing : grayscale to improve the OCR result
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = "tmp.png"
    cv2.imwrite(filename, gray)
    # OCR application
    text = pytesseract.image_to_string(Image.open(filename), lang=language)
    print("[Debug] - Extracted text: {}".format(text))
    return text
        
