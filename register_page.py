import logging
import time
from temp_mail import TempMail
from selenium.webdriver.common.by import By
from config import COMPANY,COUNTRY,FIRST_NAME,LAST_NAME,MOBILE_NUMBER,PASSWORD,REGISTER_URL
from page_object_model import Project

class Register_Page_Sayfasi:
    def __init__(self,bot):
        self.bot=bot

    def form_fill(self,mail,password):
        try:
            self.bot.input_func(css='#firstName', value=FIRST_NAME)
            self.bot.input_func(css='#lastName', value=LAST_NAME)
            self.bot.input_func(css='.ant-select-selection-search-input', value=COUNTRY)
            self.bot.input_func(css='#phoneNumber', value=MOBILE_NUMBER)
            self.bot.input_func(css='#companyName', value=COMPANY)
            self.bot.input_func(css='[formcontrolname="email"]', value=mail)
            self.bot.click_funca(css='[formcontrolname="jobTitle"]')
            self.bot.input_func(css='[formcontrolname="password"]', value=password)
            self.bot.input_func(css='[formcontrolname="passwordConfirm"]', value=password)
            self.bot.driver.find_element(By.CSS_SELECTOR, '.checkbox-box').click()
            self.bot.click_modal_button()
            time.sleep(5)
            self.bot.driver.find_element(By.CSS_SELECTOR,'.ant-btn-primary').click()
        except Exception as e:
            print(f'Hata meydana geldi',str(e))
    