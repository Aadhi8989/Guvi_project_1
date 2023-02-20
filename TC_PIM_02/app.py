from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import Data
from Test_Locators import Locators

#Testcase_PIM_02

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
        #Edit_Button
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().edit_button))).click()


        # #Page_2 Personal Details
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().NickName_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().NickName_Box))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().NickName_Box))).send_keys(Data.Hrm_data().NickName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId_box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId_box))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId_box))).send_keys(Data.Hrm_data().otherId)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DL_Number_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DL_Number_Box))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DL_Number_Box))).send_keys(Data.Hrm_data().DriverLicense)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DateofBirth_D))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DateofBirth_D))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DateofBirth_D))).send_keys(Data.Hrm_data().DateofBirth)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Pim_Save_Button))).click()
        print('Personal Detail Updated')
      
OrangeHrm().login()