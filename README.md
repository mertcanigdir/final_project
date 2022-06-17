# final_project

Matbu olarak iletmiş olduğumuz proje fikrimizde değişiklikler olmuştur,Kamera ile çekilen sayaç fotografı üzerinden Computer Vision listesi altında tesseract,opencv,easyocr gibi kütüphaneler kullanılmıştır.Normal yüzeylerde  harfler ve rakamlar çok ufak hatalar ile çözümlenmiştir fakat sayaçların dönen ve girintili yüzeyi olması sebebi ile   rakamlar elde edilememiştir.
Elektronik sayaçlarda okuma gerçekleşmektedir fakat günümüzde hala yeteri düzeyde elektronik sayaç olmadığından bu fikirden vazgeçilip,girdiler ile bilgilerin alınıp hesaplanmasına karar verilmiştir.

Programımızın amacı olan su faturası hesaplama işlemi için güncel metre küp fiyatlarının ve atık vergisi,kdv gibi oranlar
buski nin web sitesi üzerinden "BeautifulSoup" kütüphanesinden yararlanılarak alınmıştır.
Ayrıca engelli bireylerin de dahil olduğu bazı vergi dilimi ve fiyatlandırma farklılıklarının olduğu seçeneklerde programımıza eklenmiştir.
 
Fatura hesaplama işlemi tamamlandıktan sonra kişi (smtlib) kütüphanesi ile isteği mail adresine fatura bilgilerini  gönderebilmektedir 

Programımızın arayüzü tkinter kütüphanesi ile yapılmıştır.

https://docs.python.org/3/library/tkinter.html

https://www.crummy.com/software/BeautifulSoup/bs4/doc/  web adresi üzerinden dökümanlara ulaşılmıştır.

https://mertmekatronik.com/python-ile-mail-gondermek => mail gönderme modülü (smtplib)






