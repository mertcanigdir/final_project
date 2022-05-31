from ast import Break
from gettext import gettext
from html.parser import HTMLParser
from telnetlib import PRAGMA_HEARTBEAT
from tkinter import Frame
import cv2
from PIL import Image
from lib2to3.pgen2 import driver                       
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# ( sideden veri çekme uygulaması)

url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
r=requests.get(url1,verify=False) 
soup = BeautifulSoup(r.content,'html.parser')
gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)

######### hesaplama
kademe_1_birim_fiyatı = float(onikimetrekupalti.replace(",","."))#virgulleri noktaya ceviriyorum
kademe_2_birim_fiyatı = float(onikimetrekupustu.replace(",","."))#virgulleri noktaya ceviriyorum
while True:
    try:
        ilk_deger=int(input("ilk değer : "))
        break
    except ValueError:
        print("Lütfen sadece tam sayı giriniz.")
while True:
    try:
        son_deger=int(input("son değer : "))
        break
    except (NameError,ValueError):
    
        print("Lütfen sadece tam sayı giriniz.")

kullanılan_atık_su_1=(son_deger-ilk_deger)
kullanılan=(son_deger-ilk_deger)/4  #m³ e çeviriyorum
oniki_metrekupustu=kullanılan-12 # kademe 
oniki_metrekupalti=kullanılan-oniki_metrekupustu # kademe 1
kirksekiz_metrekup_ustu=kullanılan_atık_su_1-48 #kademe 2 atı su hesaplama
kirksekiz_metrekup_alti=kullanılan_atık_su_1-kirksekiz_metrekup_ustu #kademe 1 atık su hesaplama
kademe_1_tl=oniki_metrekupalti*kademe_1_birim_fiyatı # kademe 1 in fiyatı
kademe_2_tl=oniki_metrekupustu*kademe_2_birim_fiyatı # kademe 2 nin fiyatı
atık_su_kademe_1=kirksekiz_metrekup_alti*0.44 # atık su kademe 1 in fiyatı
atık_su_kademe_2=kirksekiz_metrekup_ustu*0.83 # atık su kademe 2 nin fiyatıadana
toplam_su_bedeli=kademe_1_tl+kademe_2_tl #toplamı
toplam_atık_su_bedeli=atık_su_kademe_1+atık_su_kademe_2 # atık su toplamı

def mail_gönder():
    import smtplib                                                    #Kütüphanemizi çağırıyoru
    content ="Kullanılan Toplam m³={} m³ \nSU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nATIK SU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL".format(kullanılan,round(kademe_1_tl,2),round(kademe_2_tl,2),round(toplam_su_bedeli,2),round(atık_su_kademe_1,2),round(atık_su_kademe_2,2),round((toplam_atık_su_bedeli),2))                     #content adında mesajımızı oluşturuyoruz
    mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
    mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
    mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
    mail.login("mertcan.igdir@gmail.com","mxcan80ertxn,")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
    mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz
    print("Gönderildi")

if ilk_deger > son_deger:    
    print("ilk değer son değerden büyük olamaz")

elif ilk_deger == son_deger:
    print("Şuana kadar su tüketimi gerçekleşmemiştir")

else:
    print("kullanılan toplam m³ :",kullanılan)
    print("kademe 1 :",round(kademe_1_tl,2),"TL","kademe 2 :", round(kademe_2_tl,2),"TL","toplam su bedeli :",round(toplam_su_bedeli,2),"TL")
    print("atık su kademe 1 :",round(atık_su_kademe_1,2),"TL","atık su kademe 2:",round(atık_su_kademe_2,2),"TL")
    print("toplam atık su bedeli :",round((toplam_atık_su_bedeli),2),"TL")
    print("toplam su faturası bedeli :",round((toplam_su_bedeli+toplam_atık_su_bedeli),2),"Türk Lirasısır")
    mail_gönder()
if (son_deger-ilk_deger)<48 and (son_deger-ilk_deger)>0:
    print("48 metre küp altı tüketim sağlanmıştır,Tutarınız:",round(kademe_1_tl,2),"Türk Lirasısır")


elif (son_deger-ilk_deger)>48:
    print("48 metre küp altı tüketim sağlanmıştır, Tutarınız:",round(kademe_2_tl,2),"Türk Lirasısır")




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
############################ resim okuma 
# import cv2 
# import numpy as np

# from PIL import Image
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd="C:\\Users\\emrhn\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# kaynak=""

# def metinOku(resim_yolu):
#     image=cv2.imread("susayaci.jpg")

#     image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#     kernel=np.ones((1,1),np.uint8)
#     image=cv2.erode(image,kernel,iterations=1)
#     image=cv2.dilate(image,kernel,iterations=1)

    
#     image=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)
#     cv2.imwrite(kaynak+'temizlenmisResim.jpg',image)

#     sonuc=pytesseract.image_to_string(Image.open(kaynak+'temizlenmisResim.jpg'),lang='eng')

#     return sonuc
# print('Okuma Başladı')
# print(' ')

# print(metinOku('temizlenmisResim.jpg'))
# print(' ')
# print('Okuma Bitti')