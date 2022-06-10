from ast import Break
from gettext import gettext
from html.parser import HTMLParser
import random
from telnetlib import PRAGMA_HEARTBEAT
from tkinter import Frame
import cv2
from PIL import Image
from lib2to3.pgen2 import driver                       
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import random


# ( sideden veri çekme uygulaması)

url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
r=requests.get(url1,verify=False) 
soup = BeautifulSoup(r.content,'html.parser')
gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)

######### hesaplama   *Su Tarifesinde KDV % 1, Atıksu Tarifesinde KDV % 8 , Bakım Bedelinde KDV % 18 olarak uygulanır.
kademe_1_birim_fiyati = float(onikimetrekupalti.replace(",","."))#virgulleri noktaya ceviriyorum
kademe_2_birim_fiyati = float(onikimetrekupustu.replace(",","."))#virgulleri noktaya ceviriyorum
kademe_1_atiksu_fiyati=1.76 # m³ cinsinden
kademe_2_atiksu_fiyati=3.32 # m³ cinsinden
bakım_bedeli=1.09 # son gelen fatura baz alınmıştır 

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
while True:
    try:
        gun_sayısı=int(input("kaç günlük bir kullanım yaptınız : "))
        break
    except (NameError,ValueError):
    
        print("Lütfen sadece tam sayı giriniz.")

kullanılan=(son_deger-ilk_deger)/4  #m³ e çeviriyorum

#12 m3 altı
if kullanılan < 12:
    kademe1tutari=kademe_1_birim_fiyati*kullanılan
    kademe2tutari=0
    kademe1atiksututari=kademe_1_atiksu_fiyati*kullanılan
    kademe2atiksututari=0

else:
    kademe1tutari=kademe_1_birim_fiyati*12
    kademe2tutari=(kullanılan-12)*kademe_2_birim_fiyati
    kademe1atiksututari=kademe_1_atiksu_fiyati*12
    kademe2atiksututari=(kullanılan-12)*kademe_2_atiksu_fiyati
su_tarifesi_KDV_1=(kademe1tutari+kademe2tutari)*1/100
atiksu_tarifesi_KDV_8=(kademe1atiksututari+kademe2atiksututari)*8/100
bakim_bedeli_KDV_18=bakım_bedeli*18/100
toplam_kdv=su_tarifesi_KDV_1+atiksu_tarifesi_KDV_8+bakim_bedeli_KDV_18
ödenecek_fatura_tutari=kademe1tutari+kademe2tutari+kademe1atiksututari+kademe2atiksututari+bakım_bedeli+toplam_kdv
gunluk_ortalama_tuketim=ödenecek_fatura_tutari/gun_sayısı
gunluk_ortalama_m3=kullanılan/gun_sayısı


# def mail_gönder():
#     import smtplib                                                    #Kütüphanemizi çağırıyoru
#     content ="Kullanılan Toplam m³={} m³ \nSU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nATIK SU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nBakım Bedeli={} TL \nToplam KDV={} TL \nGünlük Ortalama m³ Tüketimi={} m³ \nGunluk Ortalama Tüketim Ücreti={} TL \nÖDENECEK FATURA TUTARI={} TL".format(kullanılan,round(kademe1tutari,2),round(kademe2tutari,2),round(kademe1tutari+kademe2tutari,2),round(kademe1atiksututari,2),round(kademe2atiksututari,2),round((kademe1atiksututari+kademe2atiksututari),2),round(bakım_bedeli,2),round(toplam_kdv,2),round(gunluk_ortalama_m3,2),round(gunluk_ortalama_tuketim,2),round(ödenecek_fatura_tutari,2))                     #content adında mesajımızı oluşturuyoruz
#     mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
#     mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
#     mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
#     mail.login("mertcan.igdir@gmail.com","mxcan80ertxn,")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
#     mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz
#     print("Gönderildi")

if ilk_deger > son_deger:    
    print("ilk değer son değerden büyük olamaz")

elif ilk_deger == son_deger:
    print("Şuana kadar su tüketimi gerçekleşmemiştir")

else:
    print("kullanılan toplam m³ :",kullanılan)
    print("kademe 1 su ücreti : ",round(kademe1tutari,2),"TL  kademe 2 su ücreti : ",round(kademe2tutari,2),"TL  toplam su ücreti : ",round(kademe1tutari+kademe2tutari,2),"TL")
    print("kademe 1 atık su ücreti : ",round(kademe1atiksututari,2),"TL  kademe 2 atık su ücreti : ",round(kademe2atiksututari,2),"TL  toplam atık su ücreti : ",round(kademe1atiksututari+kademe2atiksututari,2),"TL")
    print("bakım bedeli : ",round(bakım_bedeli,2),"TL")
    print("toplam KDV : ",round(toplam_kdv,2),"TL")
    print("gunluk ortalama m³ tüketimi : ",round(gunluk_ortalama_m3,2),"m³")
    print("gunluk ortalama tüketim ücreti : ",round(gunluk_ortalama_tuketim,2),"TL")
    print("ödenecek fatura tutari : ",round(ödenecek_fatura_tutari,2),"TL")
    
    sözler=["Musluklarınızı Gereksiz Yere Açık Bırakmayın","Tasarruf Etmenize Yardımcı Olacak Bataryalar Tercih Edin","Sebze ve Meyveleri Akan Suda Yıkamayın"
,"Bulaşık ve Çamaşır Makinelerini Kullanın","Duşa Girmek İçin Suyun Isınmasını Beklerken Suyun Boşa Akmasına İzin Vermeyin","Sifon Sisteminde Su Tüketimini Azaltacak Önlemler Alın","Bahçeniz İçin Sulama Aparatlarını Tercih Edin",
"Evlerde, banyo ve tuvalette tüketilen su miktarı evde tüketilen toplam suyun %70’ini oluşturmaktadır.","Dış fırçalama ortalama 3 dakika süre alır. Eğer musluk açık bırakılırsa her fırçalama esnasında ortalama 15 litre suyu israf etmiş olursunuz."]

    bilgi=random.choice(sözler)
    print(bilgi)
    # mail_gönder()
# print()



