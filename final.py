from selenium import webdriver # burdaki import ile chrome üzerinden herhangi bir sayfaya giriş yapmamızı sağlıyor
import time 

driver_path ="C:\Users\emrea\Desktop\final_project\chromedriver.exe"   #burada web driverın bilgasayarımızda indirildiği yerin konumu
browse =webdriver.Chrome(driver_path)
browse.get("https://www.google.com.tr") #chrome üzerinden hangi siteye giriş yapmak istediğimiz parantez içine yazmamız yeterli 
time.sleep(5)                   # chrome un ne kadar süre ile açık kalacağını 
browse.quit()                  # ve süre bittikten sonra ne olacağını söylüyoruz. 
