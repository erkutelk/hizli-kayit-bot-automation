import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging
from config import LOGIN_URL

class Login_Page:
    MAIL_CSS='[formcontrolname="email"]'
    PASSWORD_CSS='[formcontrolname="password"]'

    def __init__(self, bot):
        self.bot = bot
        self.bot.driver.get(LOGIN_URL)

    def login_page_funcation(self, fake_mail, PASSWORD):
        try:
            self.bot.input_func(Login_Page.MAIL_CSS, fake_mail)
            logging.info('Login sayfasına yönlendirildi.')

            self.bot.input_func(Login_Page.PASSWORD_CSS, PASSWORD)
            password_input = self.bot.driver.find_element(By.CSS_SELECTOR, Login_Page.PASSWORD_CSS)
            password_input.send_keys(Keys.RETURN)
            self.save_mail_adres(fake_mail=fake_mail)
            time.sleep(50)
            self.bot.driver.quit()

        except Exception as e:
            logging.error('Bİlgiler girilirken bir hata meydana geldi',e)

    def save_mail_adres(self, fake_mail):
        try:
            with open('mail_adress.txt', 'a', encoding='utf-8') as file:
                file.write(fake_mail + '\n')
            logging.info(f"E-posta dosyaya yazıldı: {fake_mail}")
        except Exception as e:
            logging.info('Mail adersi kaydedilemedi')

