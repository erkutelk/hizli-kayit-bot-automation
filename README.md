# QA Automation Case Çalışması

Bu proje, başvurduğum bir QA Automation pozisyonu için yaptığım case çalışmasıdır. Bana verilen web sitesine kayıt olup, giriş yapma süreçlerini otomatikleştirmem istendi.
Projede, her seferinde yeni bir sahte (fake) mail adresi oluşturarak hem bir bot hem de otomasyon senaryosu geliştirdim. Böylece gerçek kullanıcı bilgisi kullanmadan kayıt ve giriş işlemlerini test edebildim.
Kullandığım teknolojiler arasında Selenium, undetected\_chromedriver, TempMail (fake mail oluşturmak için) ve logging gibi kütüphaneler yer alıyor. Ayrıca, işlemlerin ne aşamada olduğunu ve olası hataları kolayca takip etmek için detaylı bir log sistemi oluşturdum.
Kod yapısını daha düzenli ve yönetilebilir hale getirmek için Page Object Model (POM) tasarım desenini kullandım.
Bu projeyi tamamen kendi başıma, herhangi bir destek almadan geliştirdim.

## Kullanılan Teknolojiler

- Python
- Selenium
- undetected_chromedriver
- TempMail API (sahte mail oluşturmak için)
- Logging (hata ve işlem takibi için)
- Page Object Model (POM) tasarım deseni


## Özellikler

- Gerçek kullanıcı verisi kullanmadan otomatik kayıt ve giriş senaryoları
- Dinamik fake mail üretimi
- Web işlemlerini beklemek için `WebDriverWait` ve `ExpectedConditions` kullanımı
- Hataların ve adımların izlenebilmesi için kapsamlı `logging` sistemi
- POM yapısıyla modüler ve okunabilir kod yapısı
