# ################################################################ herhangi bir site üzerinden veri çekilme


# from selenium import webdriver # burdaki import ile chrome üzerinden herhangi bir sayfaya giriş yapmamızı sağlıyor
# import time 

# driver_path ="C:\Users\emrea\Desktop\final_project\chromedriver.exe"   #burada web driverın bilgasayarımızda indirildiği yerin konumu
# browse =webdriver.Chrome(driver_path)
# browse.get("https://www.google.com.tr") #chrome üzerinden hangi siteye giriş yapmak istediğimiz parantez içine yazmamız yeterli 
# time.sleep(5)                   # chrome un ne kadar süre ile açık kalacağını 
# browse.quit()                  # ve süre bittikten sonra ne olacağını söylüyoruz. 


# ################################################################## resimden rakamları alma 


# import easyocr                             # pip install easyocr yaıp indiriyoruz 

# reader = easyocr.Reader(['en','ch_tra'])        # burda çözümlenmek istenen resimlerdeki yazının hangi dilde olduğunun kısaltmları  (kısaltmlar sayfasında var ) 


# results = reader.readtext('test.jpg')            #jpg formatı olması gerekiyor 

# text = ''

# for result in results:
#     text += result[1] + ''


# print( 'sonuc' + text )


#################################################################### mail gönderme

# def mail_gönder():
#     import smtplib                                                    #Kütüphanemizi çağırıyoruz

#     content = "merhaba"                                               #content adında mesajımızı oluşturuyoruz
#     mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz
#     mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
#     mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
#     mail.login("mertcan.igdir@gmail.com","*************")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
#     mail.sendmail("mertcan.igdir@gmail.com","alıcınınmail@gmail.com",content)      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz


##################################################################### kamera açma


import cv2
from cv2 import VideoCapture
from cv2 import waitKey
 
kamera = cv2.VideoCapture(0)
 
while (True):
    ret, videoGoruntu = kamera.read()
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)
    if cv2.waitKey(50) & 0xFF == ord('x'):
        break
 
kamera.release()
cv2.destroyAllWindows()

