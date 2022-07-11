from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import unittest


class Fligth_Page:
    def __init__(self,myDriver):#constructor
        self.driver = myDriver

        # self.countryDropDown = Select(self.driver.find_element(By.NAME,"country")) #declarar la variable aqui sirve para luego, en el caso de que cambie algo en el desarrollo, solo se cambia desde aqui...por ejemplo si cambia el name, o el id...es decir el atributo por el que se lo busca.
        self.countryDropDown = (By.NAME,'country')



    def select_country_by_value(self,value):
          
        #self.countryDropDown.select_by_value(value)
        Select(self.driver.find_element(*self.countryDropDown)).select_by_value(value)

        
        

    def verify_country(self,country):
        
        
        #creamos un objeto de tipo unittest.estos objetos son creados exclusivamente para que los utilice el metodo, y una vez que el metodo termina el objeto se destruye liberando memoria
        tc = unittest.TestCase('__init__')

        tc.assertEqual(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip(),country)
    
    
    def verify_not_country(self,country):
        

        tc = unittest.TestCase('__init__')
        
        tc.assertNotEqual(Select(self.driver.find_element(*self.countryDropDown)).first_selected_option.text.strip(),country)
    