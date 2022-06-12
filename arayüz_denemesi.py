
import tkinter  as tk

from setuptools import Command
# from final_projesi import *


pencere = tk.Tk()
pencere.geometry("700x500")

sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)


def kullanılan_su():
    global kullanılan
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    x=s2-s1
    if(x>=0 and x<48):
        kullanılan=x*1,75
    elif(s2-s1>=48):
        kullanılan=((x-48)*3.30)+(48*1.75)

    kullanılanm3["text"] = kullanılan
    su_ucreti["text"] = round((kullanılan),2)
    print(kullanılan)

def kdv():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    vergi["text"] = round((kullanılan*0.01),2)


def atık_su():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    atık["text"] = round((kullanılan*0.8),2)

vergi=tk.Label(text="Vergi")
vergi.place(x=220,y=230)

atık=tk.Label(text="Atık verg")
atık.place(x=300,y=230)
    
    

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
kullanılanm3.place(x=220,y=310)




su_ucreti=tk.Label(text="?")
su_ucreti.place(x=260,y=110)


bakım_bedeli=tk.Label(text="=")
bakım_bedeli.place(x=200,y=190)


atık_bedeli=tk.Label(text="=")
atık_bedeli.place(x=200,y=230)



hesap =tk.Button(text="Hesapla",width=15,command=lambda:[kullanılan_su(),kdv(),atık_su()])
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

sonuc3=tk.Label(text="KDV")
sonuc3.place(x=20,y=230)

sonuc4=tk.Label(text="BAKIM BEDELİ")
sonuc4.place(x=20,y=270)

sonuc5=tk.Label(text="KULLANILAN m3")
sonuc5.place(x=20,y=310)

eşittir_silme=tk.Label(text="  ")
eşittir_silme.place(x=200,y=190)

sonuc6=tk.Label(text="SU % 1")
sonuc6.place(x=230,y=200)

sonuc7=tk.Label(text="ATIKSU % 8")
sonuc7.place(x=290,y=200)

sonuc8=tk.Label(text="BAKIM % 18")
sonuc8.place(x=375,y=200)

sonuc9=tk.Label(text="TOPLAM KDV")
sonuc9.place(x=470,y=200)

sonuc10=tk.Label(text="GÜNLÜK ORTALAMA (m³)")
sonuc10.place(x=20,y=350)

sonuc11=tk.Label(text="GÜNLÜK ORTALAMA (TL)")
sonuc11.place(x=20,y=390)







# Su Tarifesinde KDV % 1, Atıksu Tarifesinde KDV % 8 , Bakım Bedelinde KDV % 18 olarak uygulanır.
pencere.mainloop()