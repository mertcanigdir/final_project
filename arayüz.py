from hashlib import shake_128
import random
from os import remove
import tkinter  as tk
from turtle import pen
from bs4 import BeautifulSoup
# from matplotlib.ft2font import GLYPH_NAMES
from numpy import place
from setuptools import Command
import requests
import datetime as dt
# from final_projesi import *
def mail_gönder():
    import smtplib                                                    #Kütüphanemizi çağırıyoru
    s9=str(mail_1.get())
    content ="Kullanılan Toplam m³={} m³ \nSU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nATIK SU BEDELİ \nKademe 1={} TL  Kademe 2={} TL \nToplam Tutar={} TL \nBakım Bedeli={} TL \nToplam KDV={} TL \nGünlük Ortalama m³ Tüketimi={} m³ \nGunluk Ortalama Tüketim Ücreti={} TL \nÖDENECEK FATURA TUTARI={} TL".format(kullanılan,round(kademe1tutari,2),round(kademe2tutari,2),round(kademe1tutari+kademe2tutari,2),round(kademe1atiksututari,2),round(kademe2atiksututari,2),round((kademe1atiksututari+kademe2atiksututari),2),round(bakim,2),round(toplam_kdv,2),round(kullanilan/g1,2),round(toplam_para1/g1,2),round(toplam_para1,2))                     #content adında mesajımızı oluşturuyoruz
    mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
    mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
    mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
    mail.login("mertcan.igdir@gmail.com","mwkcldhgzckidlvk")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
    mail.sendmail(f"mertcan.igdir@gmail.com",{s9},content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz 
    
url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
r=requests.get(url1,verify=False) 
soup = BeautifulSoup(r.content,'html.parser')
gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır


pencere = tk.Tk()                                      # arayüz pencere boyutlarının ayaralndığı kısım
pencere.geometry("870x550")
pencere.title("BUSKİ Su Faturası Hesaplayıcı")

pencere.iconbitmap("Google-Noto-Emoji-Travel-Places-42699-water-wave.ico")

mail_1 = tk.Entry(width=20)
mail_1.place(x=720,y=40)

sayı1 =tk.Entry(width=12)                        # ilk değerin girildiği  kutucuğun konumu
sayı1.place(x=200,y=10)

sayı2 =tk.Entry(width=12)                        # son değerin girildiği kutucuğun konumu
sayı2.place(x=200,y=30)

sayı3 =tk.Entry(width=12)                        # kullandığı gün sayısının girildiği konum
sayı3.place(x=200, y=50)

# mail gondermenin seçildigi checkbuton;
deger=tk.IntVar()  # (deger) değiskenini integer tipinde olduğunu belirtiyoruz.
deger.set(0)  # checkbutonun seçili olmadan başlamasını sağlıyoruz.
isaret1=tk.Checkbutton(pencere,text="MAİL GÖNDER",variable=deger) #"MAİL GÖNDER" adında checkbuton oluşturuyoruz .Sıfır yada bir oldugunu (deger) değiskenine aktarıyoruz.
isaret1.place(x=600,y=15)   #butonun konumunun ayarlandığı kısım.
def mail_gönderme_isareti():
    if  deger.get()== 1:  #eğer checkbuton seçili ise;
        mail_gönder()  #mail gönderme fonksiyonunu çağırıyoruz.
        print("mail gönderildi")  #mail gönderildi yazdırıyoruz.
    elif deger.get() == 0:  #eğer checkbuton seçili değil ise.
        print("Mail gönderme işlemi iptal edildi")  #mail gönderme işlemi iptal edildi yazdırıyoruz.

#özellik adında değiişken ile abone turlerini tutuyoruz.
ozellik=[
    "MESKEN","ISYERI (ATIKSU YUZDE 40)","ISYERI_ATIKSU_YOK",
    "OZEL_HASTANE","GAZI_SEHIT_DUL_YETIM","RESMI_DAIRE",
    "RESMI_OKUL_OZEL_OKUL","BELEDIYE_PARK_BAHCE","BELEDIYE_SOKAK_CESME",
    "ENGELLI","TOPLU_SU_UNIVERSITE","TOPLU_SU_SANAYI","RESMI_HASTANE",
    "TOPLU_SU_SANAYI_ATIKSULU","ISYERI (ATIKSU YUZDE 50)","ISYERI (ATIKSU YUZDE 60)",
    "RESMI_OKUL_OZEL_OKUL (ATIKSU YOK)","ATIKSU ISYERI - DEBIMETRE (YUZDE 20)",
    "ATIKSU ISYERI - JEOTERMAL","ATIKSU ISYERI - DEBIMETRE (YUZDE 30)"
]
var= tk.StringVar(pencere) # (var) değiskenini string tipinde olduğunu belirtiyoruz.
var.set(ozellik[0])  #özellik [0] yani mesken seçili olarak baslamasının sağlıyoruz.

secici=tk.OptionMenu(pencere,var,ozellik[0],ozellik[1],ozellik[2],ozellik[3],ozellik[4],ozellik[5],ozellik[6],ozellik[7],ozellik[8],ozellik[9],ozellik[10],ozellik[11],ozellik[12],ozellik[13],ozellik[14],ozellik[15],ozellik[16],ozellik[17],ozellik[18],ozellik[19])
secici.place(x=300,y=30)  #menü konumunun ayarlandığı kısım.
def abone_turu():                    #abone türünün seçilmesi
    global alt_12  # baska yerlerde de kullanabilmek için global yaptıldı.
    global üst_12
    global atiksu_12_alti
    global atiksu_12_ustu
    if  var.get()==ozellik[0]:  #eğer özellik [0] yani mesken seçili ise;
        alt_12=float(ucret[0].text.replace(",","."))  #alt 12 değerini web sitesindeki mesken kısmındeki 12 m³ altının fiyatının alınmasını sağlıyoruz.
        üst_12=float(ucret[1].text.replace(",","."))  #üst 12 değerini web sitesindeki mesken kısmındeki 12 m³ üstünün fiyatının alınmasını sağlıyoruz.
        atiksu_12_alti=float(ucret[2].text.replace(",","."))  #atiksu 12 altı değerini web sitesindeki mesken kısmındeki atık su 12 m³ altının fiyatının alınmasını sağlıyoruz.
        atiksu_12_ustu=float(ucret[3].text.replace(",","."))  #atiksu 12 üstü değerini web sitesindeki mesken kısmındeki atık su 12 m³ üstünün fiyatının alınmasını sağlıyoruz.
        print("MESKEN")  #mesken yazdırıyoruz.
        # aynı şekilde tüm abone türlerinin değerlerini aşağıda alıyoruz.
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
    global kademe2tutari
    global kademe1atiksututari
    global kademe2atiksututari
    global toplam_kdv
    s1=int(sayı1.get())
    s2=int(sayı2.get())                                                    # kullanılan değişkenin değerini alması.
    kullanılan=s2-s1 #kullanılan m³ değerinin hesaplanması.
    if(kullanılan<12): #kullanılan değerinin 12 m³ üzerinde olup olmadığını kontrol eder. Eğer kullanılan 12nin altında ise aşağıda hesaplamalar yapar.
        kademe1tutari = round((kullanılan*alt_12),2)
        kademe2tutari = 0
        kademe1atiksututari=round((kullanılan*atiksu_12_alti),2)
        kademe2atiksututari=0
        su_ucreti["text"]=kademe1tutari
        kademe_2["text"] = kademe2tutari
        kademe1atiksututari_arayuz["text"] = kademe1atiksututari
        kademe2atiksututari_arayuz["text"] = kademe2atiksututari
    else:  #Eğer kullanılan 12nin altında değilse aşağıda hesaplamalar yapar.
        kademe1tutari = round((alt_12*12),2)
        kademe2tutari = round((kullanılan-12)*üst_12,2)
        kademe1atiksututari=round((12*atiksu_12_alti),2)
        kademe2atiksututari=round((kullanılan-12)*atiksu_12_ustu,2)
        su_ucreti["text"]=kademe1tutari
        kademe_2["text"] = kademe2tutari
        kademe1atiksututari_arayuz["text"] = kademe1atiksututari
        kademe2atiksututari_arayuz["text"] = kademe2atiksututari                      
    toplam_tutar["text"] = round(float(su_ucreti["text"])+float(kademe_2["text"]),2)
    toplam_atiksututari_arayuz["text"] = round(float(kademe1atiksututari_arayuz["text"])+float(kademe2atiksututari_arayuz["text"]),2)
    kullanılanm3["text"] = kullanılan
    su_tarifesi_KDV_1=(kademe1tutari+kademe2tutari)*1/100
    atiksu_tarifesi_KDV_8=(kademe1atiksututari+kademe2atiksututari)*8/100
    bakim_bedeli_KDV_18=bakim*18/100
    toplam_kdv=su_tarifesi_KDV_1+atiksu_tarifesi_KDV_8+bakim_bedeli_KDV_18
    print(kullanılan)

def kaç_gun():                                                                #suyun kaç günde kullanıldığının tarihini alması
    global g1
    global kullanilan
    global toplam_para1
    a1=int(sayı1.get())
    a2=int(sayı2.get())
    g1=int(sayı3.get())
    kullanilan=a2-a1
    toplam2=toplam_tutar["text"]
    toplam3=bakım["text"]
    toplam4=toplam_atiksututari_arayuz["text"]
    toplam5=vergi["text"]
    toplam6=çtv["text"]
    toplam_para1=round(float(toplam2)+float(toplam3)+float(toplam4)+float(toplam5)+float(toplam6),2)
    toplam_para["text"]=toplam_para1
    ortalama_gunluk["text"] = (f"Ortalama Günlük {round(kullanilan/g1),2} m³ Kullanılmıştır.")
    print(ortalama_gunluk["text"])
    ortalama_gunluk_tutar1["text"]=(f"Ortalama Günlük {round(toplam_para1/g1),2} TL Kullanılmıştır.")
    print(ortalama_gunluk_tutar1["text"])                                    #suyun kaç günde kullanıldığının tarihi ve günlük ortalama tutarın alınması
    
    


    

def kdv():                                                              #kullanılan su  kdvsi'nin hesaplanması

    vergi["text"] = round(toplam_kdv,2)


def atık_su():
    s1=int(sayı1.get())                                                 #kullanılan su atık vergisini hesaplandığı kısım
    s2=int(sayı2.get())
    x=s2-s1
    if x >= 0 and x <= 12:
        atık_bedeli["text"] = round(x*atiksu_12_alti,2)
    elif x > 12:
        atık_bedeli["text"] = round(x*atiksu_12_ustu,2)

bakim=4.66
def bakım_bedeli():                                                     #kullanılan su bakım bedelini hesaplandığı kısım
    global bakim
    
    bakım["text"] = bakim


def kullanılan_metreküp():                                               #kullanılan metreküp değerinin 
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    
    kullanılan_m3["text"] = (f"Toplam {round(s2-s1),2} m³ su tüketimi yapılmıştır")  

vergi=tk.Label(text="")
vergi.place(x=220,y=230)


bakım=tk.Label(text="")
bakım.place(x=220,y=270)

kullanılan_m3=tk.Label(text="")                                           #kullanılan metreküp  hesaplamasının  yazdırıldığı yer
kullanılan_m3.place(x=220,y=310)


toplam_para=tk.Label(font=("TkDefaultFont", 10, "underline") ,fg="white",bg="red",text="")
toplam_para.place(x=580,y=430)
def ÇTV():
    çtv["text"] = 4.08
    

çtv=tk.Label(text="")
çtv.place(x=220,y=190)


bilgi1=tk.Label(text="Başlagıç Değerini Giriniz :")                #başlangıç değeri bitiş değeri girilmesi yazılarının penceredeki yerlerini belirledik 
bilgi1.place(x=20,y=10)


sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)


bilgi2 =tk.Label(text="Bitiş Değerini Giriniz :")
bilgi2.place(x=20,y=30)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)

bilgi3 =tk.Label(text="Kaç Günlük Kullanım :")
bilgi3.place(x=20,y=50)

sayı3 =tk.Entry(width=12)
sayı3.place(x=200,y=50)

secim=tk.Label(text="↓ ABONE TÜRÜ ↓")                            #abone türü seçimi butonunun yerini belirledik
secim.place(x=300,y=0)

kullanılanm3=tk.Label(text="?")
kullanılanm3.place(x=25,y=110)

mail1=tk.Label(text="Mail Adresinizi Giriniz :")
mail1.place(x=590,y=40)




su_ucreti=tk.Label(text="")                        #işlemlerin sonuçlarının yazılacağı penceredeki yeri belirledik
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

atık_bedeli=tk.Label(text="")
atık_bedeli.place(x=20,y=700)

ortalama_gunluk=tk.Label(text="")
ortalama_gunluk.place(x=220,y=350)

ortalama_gunluk_tutar1=tk.Label(text="")
ortalama_gunluk_tutar1.place(x=220,y=390)



hesap =tk.Button(text="Hesapla",width=21,command=lambda:[ÇTV(),abone_turu(),kullanılan_su(),kdv(),atık_su(),bakım_bedeli(),kullanılan_metreküp(),kaç_gun(),mail_gönderme_isareti()])
hesap.place(x=670,y=90)


#hesapla butonu ile çalışan fonksiyonların yazıldığı yer 



for i in range(1,38):                                                            # yan çizgilerin belirlenmesi.
    tk.Label(text=str("_")).place(x=200+(i*10),y=85)
    tk.Label(text=str("_")).place(x=200+(i*10),y=125)
    tk.Label(text=str("_")).place(x=200+(i*10),y=165)
    tk.Label(text=str("_")).place(x=200+(i*10),y=205)
    tk.Label(text=str("_")).place(x=200+(i*10),y=245)
    tk.Label(text=str("_")).place(x=200+(i*10),y=285)
    tk.Label(text=str("_")).place(x=200+(i*10),y=325)
    tk.Label(text=str("_")).place(x=200+(i*10),y=365)
    tk.Label(text=str("_")).place(x=200+(i*10),y=405)
    
    
for e in range(1,11):                                                       # eşittir ve dikey çizgilerin belirlenmesi.
    tk.Label(text=str("=")).place(x=200,y=30+(e*40))
    tk.Label(text=str("|")).place(x=325,y=70+(e*9))
    tk.Label(text=str("|")).place(x=425,y=70+(e*9))


 
ayrım1=tk.Label(text="Kademe 1")
ayrım1.place(x=250,y=80)

ayrım2=tk.Label(text="Kademe 2")
ayrım2.place(x=350,y=80)

ayrım3=tk.Label(text="Toplam Tutar")
ayrım3.place(x=450,y=80)

sonuc2=tk.Label(text="Su Ücreti")
sonuc2.place(x=20,y=110)

sonuc1=tk.Label(text="Atık Su Ücreti")
sonuc1.place(x=20,y=150)

sonuc8=tk.Label(font=("TkDefaultFont", 10, "underline") ,fg="white",bg="red",text="TOPLAM")
sonuc8.place(x=500,y=430)

sonuc3=tk.Label(text="Maliye Bakanlığı (K.D.V)")
sonuc3.place(x=20,y=230)

sonuc4=tk.Label(text="Bakım  Bedeli")
sonuc4.place(x=20,y=270)

sonuc9=tk.Label(text="ÇTV Bedeli")
sonuc9.place(x=20,y=190)

sonuc5=tk.Label(text="Kullanılan m³")
sonuc5.place(x=20,y=310)

sonuc6=tk.Label(text="Günlük Ortalam m³")
sonuc6.place(x=20,y=350)

sonuc7=tk.Label(text="Günlük Ortalama Tutarı")
sonuc7.place(x=20,y=390)

#sonuc20=tk.Label(font=("Times 22 bold", 15,),fg="white",bg="red", text="BUSKİ Su Faturası Hesaplayıcı")
#sonuc20.place(x=590,y=150)

eşittir_silme3=tk.Label(text="  ")
eşittir_silme3.place(x=200,y=70)

esittir_silme2=tk.Label(text="  ")
esittir_silme2.place(x=200,y=430)

esittir_ekleme=tk.Label(text=" =")
esittir_ekleme.place(x=560,y=428)

esittir_ekleme2=tk.Label(text=" = ")
esittir_ekleme2.place(x=200,y=480)

sonuc10=tk.Label(text="*ÖNEMLİ*")             #önemli bilgi eklenmesi için penceredeki yerini belirledik
sonuc10.place(x=20,y=480)


x=["Musluklarınızı Gereksiz Yere Açık Bırakmayın","Tasarruf Etmenize Yardımcı Olacak Bataryalar Tercih Edin","Sebze ve Meyveleri Akan Suda Yıkamayın"
,"Bulaşık ve Çamaşır Makinelerini Kullanın","Duşa Girmek İçin Suyun Isınmasını Beklerken Suyun Boşa Akmasına İzin Vermeyin","Sifon Sisteminde Su Tüketimini Azaltacak Önlemler Alın","Bahçeniz İçin Sulama Aparatlarını Tercih Edin",
"Evlerde, banyo ve tuvalette tüketilen su miktarı evde tüketilen toplam suyun %70’ini oluşturmaktadır.","Dış fırçalama ortalama 3 dakika süre alır. Eğer musluk açık bırakılırsa her fırçalama \nesnasında ortalama 15 litre suyu israf etmiş olursunuz."]
#random kelimelerin yazıldığı yer
y=tk.Label(text=random.choice(x))             #random kelimeyi yazdırır.
y.place(x=220,y=480)



        


    





# Su Tarifesinde KDV % 1, Atıksu Tarifesinde KDV % 8 , Bakım Bedelinde KDV % 18 olarak uygulanır.
pencere.mainloop()
