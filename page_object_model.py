import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from temp_mail import TempMail
import logging

class Project:
    def __init__(self, url):
        ''' Program sinifi calisiyor '''
        self.driver = uc.Chrome(use_subprocess=True)
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info(f"https://app.forceget.com/system/account/register 🟩")
        time.sleep(20)# Sitede bulunan cptach için bekleme süresi ekledim, sitede bu beklme süresi olmaz ise site bot olduğumuzu anlıyor.
        for a in range(3):
            time.sleep(3)
            if not self.wait_for_element('#firstName', timeout=10):#Eğer firsname id değeri bulunamazsa sitede siteyi yenilesin
                self.driver.refresh()
                logging.error("Page not found, page refresh 🟥")

    def wait_for_element(self, css_selector, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            return True
        except:
            return False

    def input_func(self, css, value):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
            textbox = self.driver.find_element(By.CSS_SELECTOR, css)
            textbox.send_keys(value)
            textbox.send_keys(Keys.ENTER)
            time.sleep(0.5)
            logging.info('TextBox value entered successfully🟩')
        except:
            logging.error('Error occurred when entering the textbox value🟥')

    def click_funca(self, css):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
            textbox = self.driver.find_element(By.CSS_SELECTOR, css)
            textbox.click()
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Director of Marketing & Sales & HR"]'))).click()
            logging.info('Title succesful🟩')
        except Exception as e:
            logging.error('Kayıt kısmında bir hata meydana geldi',e)

    def click_modal_button(self):
        try:
            modal_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ant-modal-footer button")))
            time.sleep(2)
            modal_button.click()
        except Exception as e:
            logging.error('Modal butonuna takılanmadı.',e)

