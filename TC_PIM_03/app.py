from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import Data
from Test_Locators import Locators

class OrangeHrm:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    def __init__(self):
        self.driver.get(Data.Hrm_data().url)

    def login(self):
        #Login_Page
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.Hrm_locators().username_Box))).send_keys(Data.Hrm_data().username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.Hrm_locators().password_Box))).send_keys(Data.Hrm_data().password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().login_botton))).click()
        #Pim_Button
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Pim_Button))).click()
        #Delete_Record
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Delete_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DeletePopUp))).click()
        
        print('Employee Record Deleted successfully')    

OrangeHrm().login()