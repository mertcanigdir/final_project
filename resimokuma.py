#import pytesseract
#import cv2

#b = "C:\\Users\\emrhn\\Documents\\GitHub\\final_project\\susayaci.jpg"

#pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\emrhn\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

#a = cv2.imread(b)

#metin = pytesseract.image_to_string(a)

#print(metin)

#cv2.imshow("resim", a)
#cv2.waitKey(0)

#import pytesseract
#import cv2

#yol = "C:\\Users\\emrhn\\Documents\\GitHub\\final_project\\test.jpg"

#pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\emrhn\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

#resim = cv2.imread(yol)

#metin = pytesseract.image_to_string(resim)

#print(metin)

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\emrhn\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

a=pytesseract.image_to_string(Image.open("susayaci.jpg"), lang="eng")

print(a)
