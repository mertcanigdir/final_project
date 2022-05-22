from gettext import gettext
from html.parser import HTMLParser
from tkinter import Frame
import cv2
from PIL import Image
from lib2to3.pgen2 import driver                                     
import time 
import requests
from bs4 import BeautifulSoup
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np



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
def sil():
    import os
    os.remove("{}".format(img_name)) #silinecek dosyanın ismi
            
    ################################# dosya silme bitiş
def kayıt():
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name)) #kaydedilecek dosyanın ismi
    



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
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()