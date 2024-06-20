import cv2
import pytesseract

img = cv2.imread('the-art-of-not-giving-a-f.png')
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
text = pytesseract.image_to_string(image, lang='mya')

with open('output.txt', 'w') as f:
    f.write(text)