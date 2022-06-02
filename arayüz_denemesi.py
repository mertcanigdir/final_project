
import tkinter  as tk

from setuptools import Command


pencere = tk.Tk()
pencere.geometry("700x500")



def kdv():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    vergi["text"] = str(s1+s2)


def kullanılan_su():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    kullanılan["text"] = str(s2-s1)


def bakım():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    bakım_bedeli["text"] = int((s2-s1)*(8))


def atık():
    s1=int(sayı1.get())
    s2=int(sayı2.get())
    atık_bedeli["text"] = int((s2-s1)*(8))

bilgi1=tk.Label(text="Başlagıç değerini giriniz :")
bilgi1.place(x=20,y=10)


sayı1 =tk.Entry(width=12)
sayı1.place(x=200,y=10)


bilgi2 =tk.Label(text="Bitiş değerini giriniz :")
bilgi2.place(x=20,y=30)

sayı2 =tk.Entry(width=12)
sayı2.place(x=200,y=30)

vergi=tk.Label(text="Vergi")
vergi.place(x=200,y=110)

kullanılan=tk.Label(text="kullanılan mereküp")
kullanılan.place(x=200,y=150)

bakım_bedeli=tk.Label(text="Bakım bedeli")
bakım_bedeli.place(x=200,y=200)


atık_bedeli=tk.Label(text="atık bedeli")
atık_bedeli.place(x=200,y=250)

hesap =tk.Button(text="Hesapla",width=15,command=lambda:[kullanılan_su(),kdv(),bakım()])
hesap.place(x=300,y=15)



pencere.mainloop()