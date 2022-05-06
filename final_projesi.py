######################## herhangi bir site üzerinden veri çekilme

# from lib2to3.pgen2 import driver
# from selenium import webdriver                                             # burdaki import ile chrome üzerinden herhangi bir sayfaya giriş yapmamızı sağlıyor
# import time 

# driver_path ="C:\\Users\\emrea\\Downloads\\chromedriver.exe"             # chrome driver exe sinin konumu 
# browser =webdriver.Chrome(driver_path)
# browser.get("https://www.epdk.gov.tr/Detay/Icerik/3-1327/elektrik-faturalarina-esas-tarife-tablolari") #chrome üzerinden hangi siteye giriş yapmak istediğimiz parantez içine yazmamız yeterli 

# button = browser.find_element_by_xpath('...........')  # tıklama yeri bulunacak 
# button.click()
# time.sleep(0)                   # chrome un ne kadar süre ile açık kalacağını 
# browser.quit()                  # ve süre bittikten sonra ne olacağını söylüyoruz. 


# ################################################################## resimden rakamları alma 

import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\emrea\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'    # tesseract.exe nin bilgisayarda kurulu olduğu yer
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

img =cv2.imread('C:\\Users\\emrea\Desktop\\New folder\\final_project\\img.png')  # okunacak resimin konumu

def get_grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img= thresholding(img)
img=remove_noise(img)

print(ocr_core(img))
print(type(ocr_core(img)))


#################################################################### mail gönderme




# import smtplib                                                    #Kütüphanemizi çağırıyoruz

# content = "merhaba"                                               #content adında mesajımızı oluşturuyoruz
# mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
# mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
# mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
# mail.login("mertcan.igdir@gmail.com","2000mmmm")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
# mail.sendmail("mertcan.igdir@gmail.com","emrearas95@hotmail.com",content)      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz


# print("Gönderildi")
##################################################################### kamera açma


# import cv2    
# from cv2 import VideoCapture
# from cv2 import waitKey
 
# kamera = cv2.VideoCapture(0)
 
# while (True):
#     ret, videoGoruntu = kamera.read()
#     cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)
#     if cv2.waitKey(50) & 0xFF == ord('x'):
#         break
 
# kamera.release()
# cv2.destroyAllWindows()

