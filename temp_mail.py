import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import logging

class TempMail:
    def __init__(self):
        self.driver = uc.Chrome()
        self.driver.get('https://temp-mail.org/en/')
        logging.info(f'https://temp-mail.org/en/ Başarılı 🟩')
        
        time.sleep(5)
        while True:
            time.sleep(10)
            if self.driver.title == 'Bir dakika lütfen...':# Sitenin başlığı eğer bir dakika lütfen diyorsa, siteye 10 saniye içinde yeninde başlatmak için kullanılır
                logging.info('Page not found🟥')
            else:
                if self.tekrar_dene():
                    logging.error('Too many new mailboxes created. Upgrade to Premium or try again later🟥')
                    self.driver.quit() 
                    sys.exit()
                    # print(f'-Mail Adresi için sonra deneyiniz\nToo many new mailboxes created. Upgrade to Premium or try again later.')
                    break
                else:
                    logging.info('The program is working🟩')
                    time.sleep(5)
                    break

    def tekrar_dene(self):
        for _ in range(5): 
            try:
                growl_message = self.driver.find_element(By.CSS_SELECTOR, '.growl-message')
                if growl_message.text == 'Too many new mailboxes created. Upgrade to Premium or try again later.':
                    logging.error('Çok fazla mail talebinde bulunuldu, beklememiz gerekiyor')
                    return True
            except:
                time.sleep(1) 
        return False

    def mail_get(self):
        try:
            mail_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mail")))
            if mail_input.get_attribute("value") == '':
                logging.error("Mail address could not be retrieved, closing the page🟥")
                self.driver.quit()
                
            if mail_input.get_attribute('value') == 'Loading':
                pass
            else:
                try:
                    fake_mail=mail_input.get_attribute("value")
                    logging.info(f'Fake mail successful🟩')
                    return fake_mail
                except:
                    logging.error('Fake Mail Address Not Found🟥')
        except:
            return "Yok"
        
    def href_get(self):# Gelen mail in url bilgisini aldı sonra bu url bilgisine geçiş yaptık
        time.sleep(10)
        self.driver.refresh()
        time.sleep(10)
        try:
            email_list = self.driver.find_elements(By.CSS_SELECTOR, ".inbox-dataList ul li")
            print('Adet li değeri var',len(email_list))
            logging.info(f'Mail number :{len(email_list)}')
            for a in reversed(email_list): # En sondaki liste değerinin href bilgisini alır.
                link_element = a.find_element(By.CSS_SELECTOR, "div a")
                href_mail_href = link_element.get_attribute("href")

                if href_mail_href.startswith("https://temp-mail.org/en/view/"):  
                    logging.info(f'Temp Mail link: {href_mail_href}')
                    self.driver.get(href_mail_href)
                    return href_mail_href

                else:
                    logging.error('Mail adress password not found🟥')
            return None
        except Exception as e:
            print("Link bulunamadı:", str(e))
            return None


    def mail_sifre(self):
        try:
            mail_password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.inbox-data-content-intro span span div p'))
            ).text
            logging.info(f'Mail Password succesful {mail_password.strip()}🟩')
            return mail_password.strip()
        except:
            logging.error('Mail password not found🟥')
            return None

    def deneme(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.temp-emailbox').text

