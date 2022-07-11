from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class Page_Register():
    def __init__(self,myDriver):
        self.driver = myDriver

    def verify_registration_form(self):
        link_registration = self.driver.find_element(By.LINK_TEXT,"REGISTER")

        #creamos un objeto de tipo unittest
        tc = unittest.TestCase('__init__')
        
        tc.assertEqual(link_registration.text,"REGISTER")