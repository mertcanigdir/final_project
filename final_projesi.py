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
######################## herhangi bir site üzerinden veri çekilme

# (daha kısa alternatif sideden veri çekme uygulaması)

# url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
# r=requests.get(url1,verify=False) 
# soup = BeautifulSoup(r.content,'html.parser')
# gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
# ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
# ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
# onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
# onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)
# print(onikimetrekupalti,onikimetrekupustu) 

##################

# driver_path ="C:\\Users\\emrea\\Downloads\\chromedriver.exe"             # chrome driver exe sinin konumu 
# browser =webdriver.Chrome(driver_path)
# browser.get("https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7") #chrome üzerinden hangi siteye giriş yapmak istediğimiz parantez içine yazmamız yeterli 
# browser.maximize_window()
# button = browser.find_element_by_xpath ('//*[@id="abone-rehberi-header-2"]/button')
# button.click()
# url = "https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7"
# #requests.get("https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7", verift = False)
# soup = BeautifulSoup(browser.page_source,'html.parser')
# bilgi=[td.text for td in soup.findAll('td',style="text-align:center")]
# table =soup.find('div',attrs = {'id':'quotesList'})
# time.sleep(3)                   # chrome un ne kadar süre ile açık kalacağını 
# browser.quit()                  # ve süre bittikten sonra ne olacağını söylüyoruz. 
# onİkimetrekupustu = bilgi[1]
# onİkimetrekupalti = bilgi[0]

# print(onİkimetrekupalti,onİkimetrekupustu)


# ################################################################## resimden rakamları alma 


# pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\emrea\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'    # tesseract.exe nin bilgisayarda kurulu olduğu yer
# def ocr_core(img):
#     text = pytesseract.image_to_string(img)
#     return text

# img =cv2.imread('C:\\Users\\emrea\Desktop\\New folder\\final_project\\img.png')  # okunacak resimin konumu

# def get_grayscale(image):
#     return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# def remove_noise(image):
#     return cv2.medianBlur(image,5)

# def thresholding(image):
#     return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# img = get_grayscale(img)
# img= thresholding(img)
# img=remove_noise(img)

# print(ocr_core(img))
# print(type(ocr_core(img)))


#################################################################### mail gönderme




# import smtplib                                                    #Kütüphanemizi çağırıyoruz

# content = "merhaba"                                               #content adında mesajımızı oluşturuyoruz
# mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
# mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
# mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
# mail.login("mertcan.igdir@gmail.com","2000mmmm")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
# mail.sendmail("mertcan.igdir@gmail.com","emrearas95@hotmail.com",content)      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz


# print("Gönderildi")
##################################################################### kamera açma ve kaydetme

################################# dosya silme baslangıç
def sil():
    
    import os
    if k == ord('d'): # eğer "d" tuşuna basarsak çalış anlamında

        os.remove("{}".format(img_name)) #silinecek dosyanın ismi
        
################################# dosya silme bitiş

import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # kamerayı kapatmak için ESC ye 
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # Resim çekmek için SPACE tuşuna bassa biliri resimleri bu klasöre atıyor :D
        
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
    
    sil()

cam.release()

cv2.destroyAllWindows(0)


