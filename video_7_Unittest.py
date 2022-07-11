#Unittest: 
from selenium.webdriver.support.ui import Select
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#los casos de prueba pueden estar dentro de una clase

class newTours(unittest.TestCase):
    #primer metodo es setUP , para levantar el browser e ir a un sitio en particular
    def setUp(self) :
        #self.driver para que el driver sea unico para toda la clase
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('http://demo.guru99.com/test/newtours/')
        time.sleep(4)
        
        
    #casos de prueba: cada uno va a ser un metodo, y debe comenzar con la palabra test
    def test_dropDown(self):
        driver = self.driver
        
        boton_register= driver.find_element(By.LINK_TEXT,'REGISTER')
        boton_register.click()
        countryDropDown = Select(driver.find_element(By.NAME,"country")) #esto es nuestro selector
        #para buscar un valor dentro del select
        countryDropDown.select_by_value("ARGENTINA")

        #assertEquals nos dice si un texto es igual a otro
        self.assertEqual(countryDropDown.first_selected_option.text.strip(),"ARGENTINA")
    #.strip es para quitar espacios en blanco
        time.sleep(4)

    def test_register(self):
        driver = self.driver
        user_box = driver.find_element(By.NAME,"userName")
        pass_box = driver.find_element(By.NAME,"password")

        user_box.send_keys("test")
        pass_box.send_keys("test")

        submit_button = driver.find_element(By.XPATH,"//tbody/tr[4]/td[2]/div[1]/input[1]")
        submit_button.click()
        time.sleep(2)

        register_button = driver.find_element(By.LINK_TEXT,"REGISTER")

        self.assertEqual(register_button.text(),"REGISTER")


    def tearDown(self): #una vez que termina nuestro caso se aplica el tearDown
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()