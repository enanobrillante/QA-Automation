#un dropdown es una lista desplegable

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para poder trabajar con las listas desplegables select

driver = webdriver.Chrome('chromedriver3.exe')
driver.get('http://demo.guru99.com/test/newtours/')

time.sleep(5)

driver.find_element_by_link_text("REGISTER").click()
countryDropDown = Select(driver.find_element_by_name("country")) #esto es nuestro selector

#para buscar un valor dentro del select
countryDropDown.select_by_value("ARGENTINA")

time.sleep(4)

driver.quit()


