import pytesseract
from PIL import Image


# Load image
image_path = 'testingResources/IMscoresheet1.jpg'
image = Image.open(image_path)

# Perform OCR(Optical Character Recognition)]
text = pytesseract.image_to_string(image)

# Print recognized text
print(text.replace('\n',''))