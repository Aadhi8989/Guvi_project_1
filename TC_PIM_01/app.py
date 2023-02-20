from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import Data
from Test_Locators import Locators

#TestCase_PIM_01

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
        #Add_Button
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Add_button))).click()
        #Page_1 Fist,Middle,Last Name
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().firstName_Box))).send_keys(Data.Hrm_data().firstName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().middleName_Box))).send_keys(Data.Hrm_data().middleName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().lastName_Box))).send_keys(Data.Hrm_data().lastName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Save_Button))).click()
        #Page_2 Personal Details
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().NickName_Box))).send_keys(Data.Hrm_data().NickName)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().EmployeId_Box))).send_keys(Data.Hrm_data().employeid)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId_box))).send_keys(Data.Hrm_data().otherId)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DL_Number_Box))).send_keys(Data.Hrm_data().DriverLicense)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().LicenseExpiryDate))).send_keys(Data.Hrm_data().LicenseExpiryDate)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().SSNNumber_Box))).send_keys(Data.Hrm_data().SSN_Number)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().SinNumber_Box))).send_keys(Data.Hrm_data().SinNumber)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Nationality))).click()                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Indian_Button))).click()                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().MaritalStatus))).click()                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Single_button))).click()                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().DateofBirth_D))).send_keys(Data.Hrm_data().DateofBirth)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Gender_Button))).click()                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().MilitaryService))).send_keys(Data.Hrm_data().Military_Service)                                                                                               
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Pim_Save_Button))).click() 
        
        print('successful added Employee Details')    

OrangeHrm().login()