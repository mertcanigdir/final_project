from hashlib import shake_128
import random
from os import remove
import tkinter  as tk
from turtle import pen
from bs4 import BeautifulSoup
from numpy import place
from setuptools import Command
import requests
import datetime as dt
# from final_projesi import *
def mail_gönder():
    import smtplib                                                    #Kütüphanemizi çağırıyoru
    content ="Kullanılan Toplam m³={} m³ \nSU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nATIK SU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nBakım Bedeli={} TL \nToplam KDV={} TL \nÖDENECEK FATURA TUTARI={} TL".format(kullanılan,round(kademe1tutari,2),round(0,2),round(0,2),round(0,2),round(0,2),round(0,2),round(0,2),round(0,2),round(0,2))                     #content adında mesajımızı oluşturuyoruz
    mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
    mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
    mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
    mail.login("mertcan.igdir@gmail.com","mwkcldhgzckidlvk")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
    mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz
    
url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
r=requests.get(url1,verify=False) 
soup = BeautifulSoup(r.content,'html.parser')
gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
# onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
# onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)
# alt_12= float(onikimetrekupalti.replace(",","."))
# üst_12 = float(onikimetrekupustu.replace(",","."))


pencere = tk.Tk()                                      # arayüz pencere boyutlarının ayaralndığı kısım
pencere.geometry("700x500")

sayı1 =tk.Entry(width=12)                        # ilk değerin girildiği  kutucuğun konumu
sayı1.place(x=200,y=10)

sayı2 =tk.Entry(width=12)                        # son değerin girildiği kutucuğun konumu
sayı2.place(x=200,y=30)

sayı3 =tk.Entry(width=12)                        # kullandığı gün sayısının girildiği konum
sayı3.place(x=200, y=50)

deger=tk.IntVar()
deger.set(0)
isaret1=tk.Checkbutton(pencere,text="MAİL GÖNDER",variable=deger)
isaret1.place(x=300,y=45)
def mail_gönderme_isareti():
    if  deger.get()== 1:
        mail_gönder()
        print("mail gönderildi")
    elif deger.get() == 0:
        print("Mail gönderme işlemi iptal edildi")

ozellik=[
    "MESKEN","ISYERI (ATIKSU YUZDE 40)","ISYERI_ATIKSU_YOK",
    "OZEL_HASTANE","GAZI_SEHIT_DUL_YETIM","RESMI_DAIRE",
    "RESMI_OKUL_OZEL_OKUL","BELEDIYE_PARK_BAHCE","BELEDIYE_SOKAK_CESME",
    "ENGELLI","TOPLU_SU_UNIVERSITE","TOPLU_SU_SANAYI","RESMI_HASTANE",
    "TOPLU_SU_SANAYI_ATIKSULU","ISYERI (ATIKSU YUZDE 50)","ISYERI (ATIKSU YUZDE 60)",
    "RESMI_OKUL_OZEL_OKUL (ATIKSU YOK)","ATIKSU ISYERI - DEBIMETRE (YUZDE 20)",
    "ATIKSU ISYERI - JEOTERMAL","ATIKSU ISYERI - DEBIMETRE (YUZDE 30)"
]
var= tk.StringVar(pencere)
var.set(ozellik[0])

secici=tk.OptionMenu(pencere,var,ozellik[0],ozellik[1],ozellik[2],ozellik[3],ozellik[4],ozellik[5],ozellik[6],ozellik[7],ozellik[8],ozellik[9],ozellik[10],ozellik[11],ozellik[12],ozellik[13],ozellik[14],ozellik[15],ozellik[16],ozellik[17],ozellik[18],ozellik[19])
secici.place(x=450,y=17)
def abone_turu():                    #abone türünün seçilmesi
    global alt_12
    global üst_12
    global atiksu_12_alti
    global atiksu_12_ustu
    if  var.get()==ozellik[0]:
        alt_12=float(ucret[0].text.replace(",","."))
        üst_12=float(ucret[1].text.replace(",","."))
        atiksu_12_alti=float(ucret[2].text.replace(",","."))
        atiksu_12_ustu=float(ucret[3].text.replace(",","."))
        print("MESKEN")
    elif var.get()==ozellik[1]:
        alt_12=float(ucret[4].text.replace(",","."))
        üst_12=float(ucret[5].text.replace(",","."))
        atiksu_12_alti=float(ucret[6].text.replace(",","."))
        atiksu_12_ustu=float(ucret[7].text.replace(",","."))
        print("ISYERI (ATIKSU YUZDE 40)")
    elif var.get()==ozellik[2]:
        alt_12=float(ucret[8].text.replace(",","."))
        üst_12=float(ucret[9].text.replace(",","."))
        atiksu_12_alti=float(ucret[10].text.replace(",","."))
        atiksu_12_ustu=float(ucret[11].text.replace(",","."))
        print("ISYERI_ATIKSU_YOK")
    elif var.get()==ozellik[3]:
        alt_12=float(ucret[12].text.replace(",","."))
        üst_12=float(ucret[13].text.replace(",","."))
        atiksu_12_alti=float(ucret[14].text.replace(",","."))
        atiksu_12_ustu=float(ucret[15].text.replace(",","."))
        print("OZEL_HASTANE")
    elif var.get()==ozellik[4]:
        alt_12=float(ucret[16].text.replace(",","."))
        üst_12=float(ucret[17].text.replace(",","."))
        atiksu_12_alti=float(ucret[18].text.replace(",","."))
        atiksu_12_ustu=float(ucret[19].text.replace(",","."))
        print("GAZI_SEHIT_DUL_YETIM")
    elif var.get()==ozellik[5]:
        alt_12=float(ucret[20].text.replace(",","."))
        üst_12=float(ucret[21].text.replace(",","."))
        atiksu_12_alti=float(ucret[22].text.replace(",","."))
        atiksu_12_ustu=float(ucret[23].text.replace(",","."))
        print("RESMI_DAIRE")
    elif var.get()==ozellik[6]:
        alt_12=float(ucret[24].text.replace(",","."))
        üst_12=float(ucret[25].text.replace(",","."))
        atiksu_12_alti=float(ucret[26].text.replace(",","."))
        atiksu_12_ustu=float(ucret[27].text.replace(",","."))
        print("RESMI_OKUL_OZEL_OKUL")
    elif var.get()==ozellik[7]:
        alt_12=float(ucret[28].text.replace(",","."))
        üst_12=float(ucret[29].text.replace(",","."))
        atiksu_12_alti=float(ucret[30].text.replace(",","."))
        atiksu_12_ustu=float(ucret[31].text.replace(",","."))
        print("BELEDIYE_PARK_BAHCE")
    elif var.get()==ozellik[8]:
        alt_12=float(ucret[32].text.replace(",","."))
        üst_12=float(ucret[33].text.replace(",","."))
        atiksu_12_alti=float(ucret[34].text.replace(",","."))
        atiksu_12_ustu=float(ucret[35].text.replace(",","."))
        print("BELEDIYE_SOKAK_CESME")
    elif var.get()==ozellik[9]:
        alt_12=float(ucret[36].text.replace(",","."))
        üst_12=float(ucret[37].text.replace(",","."))
        atiksu_12_alti=float(ucret[38].text.replace(",","."))
        atiksu_12_ustu=float(ucret[39].text.replace(",","."))
        print("ENGELLI")
    elif var.get()==ozellik[10]:
        alt_12=float(ucret[40].text.replace(",","."))
        üst_12=float(ucret[41].text.replace(",","."))
        atiksu_12_alti=float(ucret[42].text.replace(",","."))
        atiksu_12_ustu=float(ucret[43].text.replace(",","."))
        print("TOPLU_SU_UNIVERSITE")
    elif var.get()==ozellik[11]:
        alt_12=float(ucret[44].text.replace(",","."))
        üst_12=float(ucret[45].text.replace(",","."))
        atiksu_12_alti=float(ucret[46].text.replace(",","."))
        atiksu_12_ustu=float(ucret[47].text.replace(",","."))
        print("TOPLU_SU_SANAYI")
    elif var.get()==ozellik[12]:
        alt_12=float(ucret[48].text.replace(",","."))
        üst_12=float(ucret[49].text.replace(",","."))
        atiksu_12_alti=float(ucret[50].text.replace(",","."))
        atiksu_12_ustu=float(ucret[51].text.replace(",","."))
        print("RESMI_HASTANE")
    elif var.get()==ozellik[13]:
        alt_12=float(ucret[52].text.replace(",","."))
        üst_12=float(ucret[53].text.replace(",","."))
        atiksu_12_alti=float(ucret[54].text.replace(",","."))
        atiksu_12_ustu=float(ucret[55].text.replace(",","."))
        print("TOPLU_SU_SANAYI_ATIKSULU")
    elif var.get()==ozellik[14]:
        alt_12=float(ucret[56].text.replace(",","."))
        üst_12=float(ucret[57].text.replace(",","."))
        atiksu_12_alti=float(ucret[58].text.replace(",","."))
        atiksu_12_ustu=float(ucret[59].text.replace(",","."))
        print("ISYERI (ATIKSU YUZDE 50)")
    elif var.get()==ozellik[15]:
        alt_12=float(ucret[60].text.replace(",","."))
        üst_12=float(ucret[61].text.replace(",","."))
        atiksu_12_alti=float(ucret[62].text.replace(",","."))
        atiksu_12_ustu=float(ucret[63].text.replace(",","."))
        print("ISYERI (ATIKSU YUZDE 60)")
    elif var.get()==ozellik[16]:
        alt_12=float(ucret[64].text.replace(",","."))
        üst_12=float(ucret[65].text.replace(",","."))
        atiksu_12_alti=float(ucret[66].text.replace(",","."))
        atiksu_12_ustu=float(ucret[67].text.replace(",","."))
        print("RESMI_OKUL_OZEL_OKUL (ATIKSU YOK)")
    elif var.get()==ozellik[17]:
        alt_12=float(ucret[68].text.replace(",","."))
        üst_12=float(ucret[69].text.replace(",","."))
        atiksu_12_alti=float(ucret[70].text.replace(",","."))
        atiksu_12_ustu=float(ucret[71].text.replace(",","."))
        print("ATIKSU ISYERI - DEBIMETRE (YUZDE 20)")
    elif var.get()==ozellik[18]:
        alt_12=float(ucret[72].text.replace(",","."))
        üst_12=float(ucret[73].text.replace(",","."))
        atiksu_12_alti=float(ucret[74].text.replace(",","."))
        atiksu_12_ustu=float(ucret[75].text.replace(",","."))
        print("ATIKSU ISYERI - JEOTERMAL")
    elif var.get()==ozellik[19]:
        alt_12=float(ucret[76].text.replace(",","."))
        üst_12=float(ucret[77].text.replace(",","."))
        atiksu_12_alti=float(ucret[78].text.replace(",","."))
        atiksu_12_ustu=float(ucret[79].text.replace(",","."))
        print("ATIKSU ISYERI - DEBIMETRE (YUZDE 30)")


def kullanılan_su():
    global kullanılan
    global kademe1tutari                                                       # kullanılan değişkenin global olarak tanımlanması 
    s1=int(sayı1.get())
    s2=int(sayı2.get())                                                    # kullanılan değişkenin değerini alması
    kullanılan=s2-s1
    if(kullanılan<12):
        kademe1tutari = round((kullanılan*alt_12),2)
        su_ucreti["text"]=kademe1tutari
        kademe_2["text"] = ("0")
        kademe1atiksututari_arayuz["text"] = round((kullanılan*atiksu_12_alti),2)
        kademe2atiksututari_arayuz["text"] = ("0")
    else:
        su_ucreti["text"] = round((alt_12*12),2)
        kademe_2["text"] = round((kullanılan-12)*üst_12,2)
        kademe1atiksututari_arayuz["text"] = round((12*atiksu_12_alti),2)
        kademe2atiksututari_arayuz["text"] = round((kullanılan-12)*atiksu_12_ustu,2)                                                                        # 12 metre küp veya üstü değerlerin hesaplanması
    toplam_tutar["text"] = round(float(su_ucreti["text"])+float(kademe_2["text"]),2)
    kullanılanm3["text"] = kullanılan
    
    print(kullanılan)

def kaç_gun():
                                                                    #suyun kaç günde kullanıldığının tarihini alması
    a1=int(sayı1.get())
    a2=int(sayı2.get())
    g1=int(sayı3.get())
    kullanilan=a2-a1
    ortalama_gunluk["text"] = round(kullanilan/g1,2)
    print(ortalama_gunluk["text"])



def kdv():                                                              #kullanılan su  kdvsi'nin hesaplanması

    vergi["text"] = 2.18


def atık_su():
    s1=int(sayı1.get())                                                 #kullanılan su atık vergisini hesaplandığı kısım
    s2=int(sayı2.get())
    x=s2-s1
    if x >= 0 and x <= 12:
        atık_bedeli["text"] = round(x*atiksu_12_alti,2)
    elif x > 12:
        atık_bedeli["text"] = round(x*atiksu_12_ustu,2)

def bakım_bedeli():                                                     #kullanılan su bakım bedelini hesaplandığı kısım

    bakım["text"] = 4.66

# def toplam_vergi():                                                       #toplam verginin hesaplandığı kısım 
#     s1=int(sayı1.get())
#     s2=int(sayı2.get())
#     x=s2-s1
#     toplam_vergi1["text"]= round((kullanılan*0.18)+(kullanılan*0.8)+(kullanılan*0.01),2)

def kullanılan_metreküp():                                               #kullanılan metreküp değerinin 
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    
    kullanılan_m3["text"] = (f"Toplam {s2-s1} m^3 su tüketimi yapılmıştır")  

vergi=tk.Label(text="")
vergi.place(x=220,y=230)

# atık=tk.Label(text="Atık %8 ")
# atık.place(x=290,y=230)

bakım=tk.Label(text="")
bakım.place(x=220,y=270)

kullanılan_m3=tk.Label(text="")                                           #kullanılan metreküp  hesaplamasının  yazdırıldığı yer
kullanılan_m3.place(x=220,y=310)

def atık_su_toplam():
    atık_su_bedeli["text"] = round(float(kademe1atiksututari_arayuz["text"])+float(kademe2atiksututari_arayuz["text"]),2)
                                                                 #atık su tutarının hesaplanması
atık_su_bedeli=tk.Label(text="")                                           #kullanılan metreküp  hesaplamasının  yazdırıldığı yer
atık_su_bedeli.place(x=460,y=150)




bilgi1=tk.Label(text="Başlagıç değerini giriniz :")
bilgi1.place(x=20,y=10)


sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)


bilgi2 =tk.Label(text="Bitiş değerini giriniz :")
bilgi2.place(x=20,y=30)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)

bilgi3 =tk.Label(text="Kaç Günlük Kullanım :")
bilgi3.place(x=20,y=50)

sayı3 =tk.Entry(width=12)
sayı3.place(x=200,y=50)

secim=tk.Label(text="↓ ABONE TÜRÜNÜ SEÇİNİZ ↓")
secim.place(x=452,y=0)

kullanılanm3=tk.Label(text="?")
kullanılanm3.place(x=25,y=110)




su_ucreti=tk.Label(text="")
su_ucreti.place(x=250,y=110)


kademe_2 =tk.Label(text="")
kademe_2.place(x=350,y=110)

toplam_tutar =tk.Label(text="")
toplam_tutar.place(x=450,y=110)

kademe1atiksututari_arayuz=tk.Label(text="")
kademe1atiksututari_arayuz.place(x=260,y=150)

kademe2atiksututari_arayuz=tk.Label(text="")
kademe2atiksututari_arayuz.place(x=360,y=150)

toplam_atiksututari_arayuz=tk.Label(text="")
toplam_atiksututari_arayuz.place(x=490,y=150)

# bakım_bedeli=tk.Label(text="=")
# bakım_bedeli.place(x=200,y=190)


atık_bedeli=tk.Label(text="=")
atık_bedeli.place(x=20,y=50)

ortalama_gunluk=tk.Label(text="")
ortalama_gunluk.place(x=220,y=320)



hesap =tk.Button(text="Hesapla",width=15,command=lambda:[abone_turu(),kullanılan_su(),atık_su_toplam(),kdv(),atık_su(),bakım_bedeli(),kullanılan_metreküp(),mail_gönderme_isareti(),kaç_gun()])
hesap.place(x=300,y=15)




for i in range(1,38):
    tk.Label(text=str("_")).place(x=200+(i*10),y=85)
    tk.Label(text=str("_")).place(x=200+(i*10),y=125)
    tk.Label(text=str("_")).place(x=200+(i*10),y=165)
    tk.Label(text=str("_")).place(x=200+(i*10),y=205)
    tk.Label(text=str("_")).place(x=200+(i*10),y=245)
    tk.Label(text=str("_")).place(x=200+(i*10),y=285)
    tk.Label(text=str("_")).place(x=200+(i*10),y=325)
    tk.Label(text=str("_")).place(x=200+(i*10),y=365)
    tk.Label(text=str("_")).place(x=200+(i*10),y=405)
    # tk.Label(text=str("_")).place(x=200+(i*10),y=365)
    
for e in range(1,11):
    tk.Label(text=str("=")).place(x=200,y=30+(e*40))
    tk.Label(text=str("|")).place(x=325,y=70+(e*13))
    tk.Label(text=str("|")).place(x=425,y=70+(e*13))
    tk.Label(text=str("|")).place(x=550,y=70+(e*13))



# tk.Label(text="="),kdv_tutarı.place(x=200,y=230)

 
ayrım1=tk.Label(text="KADEME 1")
ayrım1.place(x=250,y=80)

ayrım2=tk.Label(text="KADEME 2")
ayrım2.place(x=350,y=80)

ayrım3=tk.Label(text="TOPLAM TUTAR")
ayrım3.place(x=450,y=80)

sonuc2=tk.Label(text="SU ÜCRETİ")
sonuc2.place(x=20,y=110)

sonuc1=tk.Label(text="ATIK SU ÜCRETİ")
sonuc1.place(x=20,y=150)

sonuc3=tk.Label(text="Maliye Bakanlığı (K.D.V)")
sonuc3.place(x=20,y=230)

sonuc4=tk.Label(text="BAKIM BEDELİ")
sonuc4.place(x=20,y=270)

sonuc5=tk.Label(text="KULLANILAN m3")
sonuc5.place(x=20,y=310)

sonuc6=tk.Label(text="ORTALAMA GÜNLÜK M3")
sonuc6.place(x=20,y=350)

sonuc7=tk.Label(text="ORTALAMA GÜNLÜK KAÇ TL")
sonuc7.place(x=20,y=390)

eşittir_silme=tk.Label(text="  ")
eşittir_silme.place(x=200,y=190)

# sonuc6=tk.Label(text="SU % 1")
# sonuc6.place(x=230,y=200)

# sonuc7=tk.Label(text="ATIKSU % 8")
# sonuc7.place(x=290,y=200)

# sonuc8=tk.Label(text="BAKIM % 18")
# sonuc8.place(x=375,y=200)

# sonuc9=tk.Label(text="TOPLAM KDV")
# sonuc9.place(x=470,y=200)

sonuc10=tk.Label(text="*ÖNEMLİ*")
sonuc10.place(x=20,y=430)


x=["Musluklarınızı Gereksiz Yere Açık Bırakmayın","Tasarruf Etmenize Yardımcı Olacak Bataryalar Tercih Edin","Sebze ve Meyveleri Akan Suda Yıkamayın"
,"Bulaşık ve Çamaşır Makinelerini Kullanın","Duşa Girmek İçin Suyun Isınmasını Beklerken Suyun Boşa Akmasına İzin Vermeyin","Sifon Sisteminde Su Tüketimini Azaltacak Önlemler Alın","Bahçeniz İçin Sulama Aparatlarını Tercih Edin",
"Evlerde, banyo ve tuvalette tüketilen su miktarı evde tüketilen toplam suyun %70’ini oluşturmaktadır.","Dış fırçalama ortalama 3 dakika süre alır. Eğer musluk açık bırakılırsa her fırçalama \nesnasında ortalama 15 litre suyu israf etmiş olursunuz."]

y=tk.Label(text=random.choice(x))
y.place(x=220,y=430)



        


    





# Su Tarifesinde KDV % 1, Atıksu Tarifesinde KDV % 8 , Bakım Bedelinde KDV % 18 olarak uygulanır.
pencere.mainloop()