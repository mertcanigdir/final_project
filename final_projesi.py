from selenium import webdriver # burdaki import ile chrome üzerinden herhangi bir sayfaya giriş yapmamızı sağlıyor
import time 

driver_path ="C:\Users\emrea\Desktop\final_project\chromedriver.exe"   #burada web driverın bilgasayarımızda indirildiği yerin konumu
browse =webdriver.Chrome(driver_path)
browse.get("https://www.google.com.tr") #chrome üzerinden hangi siteye giriş yapmak istediğimiz parantez içine yazmamız yeterli 
time.sleep(5)                   # chrome un ne kadar süre ile açık kalacağını 
browse.quit()                  # ve süre bittikten sonra ne olacağını söylüyoruz. 


import easyocr                             # pip install easyocr yaıp indiriyoruz 

reader = easyocr.Reader(['en','ch_tra'])        # burda çözümlenmek istenen resimlerdeki yazının hangi dilde olduğunun kısaltmları  (kısaltmlar sayfasında var ) 


results = reader.readtext('test.jpg')            #jpg formatı olması gerekiyor 

text = ''

for result in results:
    text += result[1] + ''


print( 'sonuc' + text )