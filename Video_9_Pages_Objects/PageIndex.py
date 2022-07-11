#PAGE OBJECTS: es utilizar por cada pagina del sitio distintas clases
import time
from selenium.webdriver.common.by import By


class Page_Index:
    def __init__(self,myDriver) :

        self.driver = myDriver
        #self para decirle que es de esta clase
        self.user_box = (By.NAME,"userName")
        self.pass_box = (By.NAME,"password")
        self.register_link = (By.LINK_TEXT,'REGISTER')

        self.submit_button = (By.XPATH,"//tbody/tr[4]/td[2]/div[1]/input[1]")

    def click_register(self):
        self.driver.find_element(*self.register_link).click()
        
    def login(self,user_name,password):
       
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(password)

        
        self.driver.find_element(*self.submit_button).click()
        time.sleep(2)