from ast import Break
from cProfile import label
from gettext import gettext
from html.parser import HTMLParser
from tkinter import Frame, Label
import cv2
from PIL import Image
from lib2to3.pgen2 import driver                       
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import tkinter as tk
pencere =tk.Tk()


url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
r=requests.get(url1,verify=False) 
soup = BeautifulSoup(r.content,'html.parser')
gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)


kademe_1_birim_fiyatı = float(onikimetrekupalti.replace(",","."))#virgulleri noktaya ceviriyorum
kademe_2_birim_fiyatı = float(onikimetrekupustu.replace(",","."))#virgulleri noktaya ceviriyorum


pencere.title("ilk arayüz.")                    #pencere boyutu
pencere.geometry("500x300")




label = tk.Label(text="İlk değeri giriniz :")                      #   verinin girleceğini  yeri yazan yer
label.place(x=20,y=20)

label = tk.Label(text="Son değeri giriniz :")                       #   verinin girleceğini  yeri yazan yer
label.place(x=20,y=50)






ilk_deger =tk.Entry()                                               #     ilk sayının  girilidği kutucuk
ilk_deger.place(x=200,y=20)                                         #
                                                                   

son_deger =tk.Entry()                                                #    ikici sayının girildiği kutucuk
son_deger.place(x=200,y=50)                                          #




def Hesapla():
    deger_1=int(ilk_deger.get())                           
    deger_2=int(son_deger.get())
    sonuc["text"] =str((deger_2-deger_1)/4)

    if (deger_2-deger_1)<=12:
        sonuc=tk.Label(text="Düşük seviye atık su vergisi ")
        sonuc.place(x=200,y=80)
    elif(deger_2-deger_1)>12:
        sonuc=tk.Label(text="Yüksek seviye atık su vergisi ")
        sonuc.place(x=200,y=80)

islem=tk.Button(text="Hesapla",command=(Hesapla)).place(x=400,y=30)              #hesapla butonuna basınca hangi işlemin gerçekleşeceğini comman içersindeki def ten alıyor


sonuc=tk.Label(text=" ")                                                         #butona basınca hesaplayı aktifleştirip 
sonuc.place(x=200,y=80)





def Hesapla_1():
    deger_3=int(ilk_deger.get())
    deger_4=int(son_deger.get())
    sonuc["text"] =str((deger_3-deger_4)/4)





pencere.mainloop()


# label = tk.Label(text="Kademe 1 :")
# label.place(x=20,y=110)

# label = tk.Label(text="Atık su kademe 1  :")
# label.place(x=20,y=140)

# label = tk.Label(text="Toplam su bedeli :")
# label.place(x=20,y=170)

# label = tk.Label(text="toplam atık su bedeli :")
# label.place(x=20,y=200)

# label = tk.Label(text="Toplam su faturası bedeli :")
# label.place(x=20,y=230)

# ( sideden veri çekme uygulaması)



# ######### hesaplama
# kademe_1_birim_fiyatı = float(onikimetrekupalti.replace(",","."))#virgulleri noktaya ceviriyorum
# kademe_2_birim_fiyatı = float(onikimetrekupustu.replace(",","."))#virgulleri noktaya ceviriyorum
# while True:
#     try:
#         ilk_deger=int(input("ilk değer : "))
#         break
#     except ValueError:
#         print("Lütfen sadece tam sayı giriniz.")
# while True:
#     try:
#         son_deger=int(input("son değer : "))
#         break
#     except (NameError,ValueError):
    
#         print("Lütfen sadece tam sayı giriniz.")


# kullanılan=(son_deger-ilk_deger)/4  #m³ e çeviriyorum
# oniki_metrekupustu=kullanılan-12 # kademe 
# oniki_metrekupalti=kullanılan-oniki_metrekupustu # kademe 1
# kirksekiz_metrekup_ustu=kullanılan-48 #kademe 2 atı su hesaplama
# kirksekiz_metrekup_alti=kullanılan-kirksekiz_metrekup_ustu #kademe 1 atık su hesaplama
# kademe_1_tl=oniki_metrekupalti*kademe_1_birim_fiyatı # kademe 1 in fiyatı
# kademe_2_tl=oniki_metrekupustu*kademe_2_birim_fiyatı # kademe 2 nin fiyatı
# atık_su_kademe_1=kirksekiz_metrekup_alti*0.44 # atık su kademe 1 in fiyatı
# atık_su_kademe_2=kirksekiz_metrekup_ustu*0.83 # atık su kademe 2 nin fiyatıadana
# toplam_su_bedeli=kademe_1_tl+kademe_2_tl #toplamı
# toplam_atık_su_bedeli=atık_su_kademe_1+atık_su_kademe_2 # atık su toplamı


# if ilk_deger < son_deger:    
#     print("ilk değer son değerden büyük olamaz")

# elif ilk_deger == son_deger:
#     print("Şuana kadar su tüketimi gerçekleşmemiştir")

# else:
#     print("ilk değer son değerden büyük olamaz")
#     print("kullanılan toplam m³ :",kullanılan)
#     print("kademe 1 :",round(kademe_1_tl,2),"TL","kademe 2 :", round(kademe_2_tl,2),"TL")
#     print("atık su kademe 1 :",round(atık_su_kademe_1,2),"TL","atık su kademe 2:",round(atık_su_kademe_2,2),"TL")
#     print("toplam su bedeli :",round(toplam_su_bedeli,2),"TL")
#     print("toplam atık su bedeli :",round(toplam_atık_su_bedeli),2,"TL")
#     print("toplam su faturası bedeli :",round((toplam_su_bedeli+toplam_atık_su_bedeli),2),"TL")