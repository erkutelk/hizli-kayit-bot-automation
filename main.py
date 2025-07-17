import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from temp_mail import TempMail
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("project_log.txt", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def main():
    from page_object_model import Project
    from register_page import Register_Page_Sayfasi
    from config import PASSWORD,REGISTER_URL
    from login_page import Login_Page
    try:
        fake_mail_class = TempMail() 
        fake_mail = fake_mail_class.mail_get()

        bot = Project(REGISTER_URL)
        logging.info(f'Fake mail: {fake_mail}')

        Register_Sayfası = Register_Page_Sayfasi(bot)
        Register_Sayfası.form_fill(fake_mail, PASSWORD)
        logging.info('Kayıt Formu Dolduruldu')

        fake_mail_class.href_get()
        gelen_sifre_kod = fake_mail_class.mail_sifre()

        logging.info(f'Mailden gelen şifre kodu: {gelen_sifre_kod}')
        
        
        Login_Value=Login_Page(bot=bot)# Siteye kayıt olduktan sonra, siteye aldığımız kullanıcı bilgileri ile giriş yapmamızı sağlar
        Login_Value.login_page_funcation(fake_mail=fake_mail,PASSWORD=PASSWORD)
        logging.info('Program Bitti...')
    except Exception as e:
        logging.error(e)
    
main()



