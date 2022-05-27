from gettext import gettext
from html.parser import HTMLParser
from tkinter import Frame
import cv2
import pytesseract
from PIL import Image
from lib2to3.pgen2 import driver
from selenium import webdriver                                             # burdaki import ile chrome üzerinden herhangi bir sayfaya giriş yapmamızı sağlıyor
import time 
import requests
from bs4 import BeautifulSoup
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import pytesseract
from PIL import Image
    
# ( sideden veri çekme uygulaması)

# url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
# r=requests.get(url1,verify=False) 
# soup = BeautifulSoup(r.content,'html.parser')
# gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
# ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
# ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
# onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
# onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)
# print(onikimetrekupalti,onikimetrekupustu) 


#################################################################### mail gönderme



# def mail_gönder():
#     import smtplib                                                    #Kütüphanemizi çağırıyoru
#     content = "fotokayıtedildi"                                               #content adında mesajımızı oluşturuyoruz
#     mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
#     mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
#     mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
#     mail.login("mertcan.igdir@gmail.com","mxcan80ertxn,")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
#     mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz
#     print("Gönderildi")


################## kamera açma ve kaydetme

    ################################# dosya silme baslangıç
# def sil():
#     import os
#     os.remove("{}".format(img_name)) #silinecek dosyanın ismi
            
#     ################################# dosya silme bitiş
# def kayıt():
#     cv2.imwrite(img_name, frame)
#     print("{} written!".format(img_name)) #kaydedilecek dosyanın ismi
    


# import cv2
# import os
# img_counter = 0

# cam = cv2.VideoCapture(1) #kamera seçimi

# cv2.namedWindow("test")
# img_name = "opencv_frame_{}.png".format(img_counter)
    

# while True:
#     ret, frame = cam.read()
#     cv2.imshow("test", frame)
#     if not ret:
#         print("failed to grab frame")
#         break

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # kamerayı kapatmak için ESC ye 
#         print("Escape hit, closing...")
#         break
#     time.sleep(5)
#     kayıt()
#     time.sleep(5)
#     # oku()
#     # time.sleep(5)
#     sil()

# cam.release()

# cv2.destroyAllWindows(0)

#### computer vision 

#from PIL import Image
#import pytesseract
#### resim okuma 
import cv2 
import numpy as np

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\\Users\\emrhn\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

kaynak=""

def metinOku(resim_yolu):
    image=cv2.imread("susayaci.jpg")

    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    kernel=np.ones((1,1),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.dilate(image,kernel,iterations=1)

    
    image=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)
    cv2.imwrite(kaynak+'temizlenmisResim.jpg',image)

    sonuc=pytesseract.image_to_string(Image.open(kaynak+'temizlenmisResim.jpg'),lang='eng')

    return sonuc
print('Okuma Başladı')
print(' ')

print(metinOku('temizlenmisResim.jpg'))
print(' ')
print('Okuma Bitti')