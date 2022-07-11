#Unittest: 
from selenium.webdriver.support.ui import Select
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Video_9_Pages_Objects.PageRegister import *
from Video_9_Pages_Objects.PageIndex import *
from Video_9_Pages_Objects.Flight_Page import *

#los casos de prueba pueden estar dentro de una clase.
#los asserts dependen del modulo unittest. por lo tanto creamos un objeto unittest en cada page object para poder utilizarlo. Los assert conviene que esten en los pages objects

class newTours(unittest.TestCase):
    #primer metodo es setUP , para levantar el browser e ir a un sitio en particular
    def setUp(self) :
        #self.driver para que el driver sea unico para toda la clase
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

        self.driver.get('http://demo.guru99.com/test/newtours/')

        self.page_index = Page_Index(self.driver) #usamos la clase

        self.Page_Fligth = Fligth_Page(self.driver)

        self.PageRegister = Page_Register(self.driver)

        time.sleep(4)
        
        
    #casos de prueba: cada uno va a ser un metodo, y debe comenzar con la palabra test
    def test_dropDown(self):
        
        
        self.page_index.click_register() #llamo a la funcion que está en la clase PageIndex

        self.Page_Fligth.select_country_by_value("ARGENTINA")

     #ahora es mas facil ubicar un fallo, ya que buscamos en la pagina que ocurre el fallo
     # 
        self.Page_Fligth.verify_country("ARGENTINA")

        self.Page_Fligth.verify_not_country("CONGO")

    
    def test_register(self):
        self.page_index.login("test","test")
        
        self.PageRegister.verify_registration_form()
        


    def tearDown(self): #una vez que termina nuestro caso se aplica el tearDown
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()