
from os import remove
import tkinter  as tk
from bs4 import BeautifulSoup
from setuptools import Command
import requests
# from final_projesi import *

url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
r=requests.get(url1,verify=False) 
soup = BeautifulSoup(r.content,'html.parser')
gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)
alt_12= float(onikimetrekupalti.replace(",","."))
üst_12 = float(onikimetrekupustu.replace(",","."))


pencere = tk.Tk()                                      # arayüz pencere boyutlarının ayaralndığı kısım
pencere.geometry("700x500")

sayı1 =tk.Entry(width=12)                        # ilk değerin girildiği  kutucuğun konumu
sayı1.place(x=200,y=10)

sayı2 =tk.Entry(width=12)                        # son değerin girildiği kutucuğun konumu
sayı2.place(x=200,y=30)


def kullanılan_su():
    global kullanılan                                                        # kullanılan değişkenin global olarak tanımlanması 
    s1=int(sayı1.get())
    s2=int(sayı2.get())                                                    # kullanılan değişkenin değerini alması
    x=s2-s1
    if(x>=0 and x<12):
        kullanılan=x*7.45     
                                                                         # 12 metre küp veya üstü değerlerin hesaplanması
    elif(s2-s1>=12):
        kademe1_1=(x-12)*float(üst_12)
        kademe2_2=(12*float(alt_12))
        kullanılan=(kademe1_1)+(kademe2_2)

    kullanılanm3["text"] = kullanılan
    su_ucreti["text"] = round((kullanılan),2)
    print(kullanılan)

def kdv():                                                              #kullanılan su  kdvsi'nin hesaplanması

    vergi["text"] = 2.18


def atık_su():
    s1=int(sayı1.get())                                                 #kullanılan su atık vergisini hesaplandığı kısım
    s2=int(sayı2.get())
    x=s2-s1
    if x >= 0 and x <= 12:
        atık_bedeli["text"] = round((x*1.86),2)
    elif x > 12:
        atık_bedeli["text"] = round((x*3.54),2)

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

bakım=tk.Label(text="4,66 TL")
bakım.place(x=220,y=270)

kullanılan_m3=tk.Label(text="")                                           #kullanılan metreküp  hesaplamasının  yazdırıldığı yer
kullanılan_m3.place(x=220,y=310)

# toplam_vergi1=tk.Label(text="toplam vergi")                             #vergi işlemi yapılan kısım mın yazdırıldığı yer 
# toplam_vergi1.place(x=450,y=230)

# vergi=tk.Label(text="Vergi")
# vergi.place(x=220,y=230)
    

    

    #12 m3 altı
# if kullanılan < 12:
#     kademe1tutari=kademe_1_birim_fiyati*kullanılan
#     kademe2tutari=0
#     kademe1atiksututari=kademe_1_atiksu_fiyati*kullanılan
#     kademe2atiksututari=0
# else:
#     kademe1tutari=kademe_1_birim_fiyati*12
#     kademe2tutari=(kullanılan-12)*kademe_2_birim_fiyati
#     kademe1atiksututari=kademe_1_atiksu_fiyati*12
#     kademe2atiksututari=(kullanılan-12)*kademe_2_atiksu_fiyati
# su_tarifesi_KDV_1=(kademe1tutari+kademe2tutari)*1/100
# atiksu_tarifesi_KDV_8=(kademe1atiksututari+kademe2atiksututari)*8/100
# bakim_bedeli_KDV_18=bakım_bedeli*18/100
# toplam_kdv=su_tarifesi_KDV_1+atiksu_tarifesi_KDV_8+bakim_bedeli_KDV_18
# ödenecek_fatura_tutari=kademe1tutari+kademe2tutari+kademe1atiksututari+kademe2atiksututari+bakım_bedeli+toplam_kdv
# gunluk_ortalama_tuketim=ödenecek_fatura_tutari/gun_sayısı
# gunluk_ortalama_m3=kullanılan/gun_sayısı

# def kdv():
#     s1=int(sayı1.get())
#     s2=int(sayı2.get())
#     vergi["text"] = str(s1+s2)

# def bakım():
#     s1=int(sayı1.get())
#     s2=int(sayı2.get())
#     bakım_bedeli["text"] = int((s2-s1)*(8))


# def atık():
#     s1=int(sayı1.get())
#     s2=int(sayı2.get())
#     oniki_altı_atık=1.86*12
#     oniki_ustu_atık=((s2-s1)-12)*3.54
#     if s2-s1<=12 and s2-s1>=0:
#         kullanılan["text"] =(s2-s1)*1.86

        
#     elif s2-s1>12:
#          kullanılan["text"] =float(oniki_altı_atık)+float(oniki_ustu_atık)

#     else:
#         print("yanlıs bir değer girdiniz")

bilgi1=tk.Label(text="Başlagıç değerini giriniz :")
bilgi1.place(x=20,y=10)


sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)


bilgi2 =tk.Label(text="Bitiş değerini giriniz :")
bilgi2.place(x=20,y=30)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)


kullanılanm3=tk.Label(text="?")
kullanılanm3.place(x=25,y=110)




su_ucreti=tk.Label(text="kademe 1 ")
su_ucreti.place(x=250,y=110)


kademe_2 =tk.Label(text="Kademe 2")
kademe_2.place(x=350,y=110)

kademe_2 =tk.Label(text="toplam tutar")
kademe_2.place(x=450,y=110)

# bakım_bedeli=tk.Label(text="=")
# bakım_bedeli.place(x=200,y=190)


atık_bedeli=tk.Label(text="=")
atık_bedeli.place(x=20,y=50)



hesap =tk.Button(text="Hesapla",width=15,command=lambda:[kullanılan_su(),kdv(),atık_su(),bakım_bedeli(),kullanılan_metreküp()])
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
for e in range(1,9):
    tk.Label(text=str("=")).place(x=200,y=70+(e*40))
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

sonuc10=tk.Label(text="GÜNLÜK ORTALAMA (m³)")
sonuc10.place(x=20,y=350)

sonuc11=tk.Label(text="GÜNLÜK ORTALAMA (TL)")
sonuc11.place(x=20,y=390)







# Su Tarifesinde KDV % 1, Atıksu Tarifesinde KDV % 8 , Bakım Bedelinde KDV % 18 olarak uygulanır.
pencere.mainloop()