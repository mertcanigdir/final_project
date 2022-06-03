
import tkinter  as tk

from setuptools import Command


pencere = tk.Tk()
pencere.geometry("700x500")

sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)



def kdv():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    vergi["text"] = str(s1+s2)


def kullanılan_su():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    oniki_altı=89.4
    oniki_ustu=((s2-s1)-12)*14.16
    if s2-s1<=12 and s2-s1>=0:
        kullanılan["text"] =(s2-s1)*7.45
    elif s2-s1>12:
         kullanılan["text"] =float(oniki_altı)+float(oniki_ustu)
       

def bakım():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    bakım_bedeli["text"] = int((s2-s1)*(8))


def atık():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    oniki_altı_atık=1.86*12
    oniki_ustu_atık=((s2-s1)-12)*3.54
    if s2-s1<=12 and s2-s1>=0:
        kullanılan["text"] =(s2-s1)*1.86

        
    elif s2-s1>12:
         kullanılan["text"] =float(oniki_altı_atık)+float(oniki_ustu_atık)

    else:
        print("yanlıs bir değer girdiniz")

bilgi1=tk.Label(text="Başlagıç değerini giriniz :")
bilgi1.place(x=20,y=10)


sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)


bilgi2 =tk.Label(text="Bitiş değerini giriniz :")
bilgi2.place(x=20,y=30)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)

vergi=tk.Label(text="=")
vergi.place(x=200,y=110)

kullanılan=tk.Label(text="=")
kullanılan.place(x=200,y=150)

bakım_bedeli=tk.Label(text="=")
bakım_bedeli.place(x=200,y=190)


atık_bedeli=tk.Label(text="=")
atık_bedeli.place(x=200,y=230)



hesap =tk.Button(text="Hesapla",width=15,command=lambda:[kullanılan_su(),kdv(),bakım(),atık()])
hesap.place(x=300,y=15)

sonuc1=tk.Label(text="Vergi  : ")
sonuc1.place(x=20,y=110)

sonuc2=tk.Label(text="Kullanılar metreküt tutarı : ")
sonuc2.place(x=20,y=150)

sonuc3=tk.Label(text="Bakım bedeli : ")
sonuc3.place(x=20,y=190)

sonuc4=tk.Label(text="Atık su bedeli : ")
sonuc4.place(x=20,y=230)

sonuc5=tk.Label(text="Fatura tutarınız: ")
sonuc5.place(x=20,y=270)


pencere.mainloop()