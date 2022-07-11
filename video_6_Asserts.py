#los assert a diferencia de una verificacion, cortan la prueba si algo falla, el codigo no continua.Se corta.

import time
from typing import Text
from selenium import webdriver
from selenium.webdriver.support.ui import Select #para poder trabajar con las listas desplegables select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver3.exe')
driver.get('http://demo.guru99.com/test/newtours/')

time.sleep(5)
user_box = driver.find_element(By.XPATH,'//tbody/tr[2]/td[2]/input[1]')
pass_box= driver.find_element(By.CSS_SELECTOR,'table:nth-child(1) tbody:nth-child(1) tr:nth-child(3) td:nth-child(2) > input:nth-child(1)')
submit_button = driver.find_element(By.NAME,'submit')

user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
time.sleep(2)


register = driver.find_element(By.LINK_TEXT,'REGISTER')
#el assert devuelve true o false, si da false corta la prueba
#assert register.text == ("REGISTER")
assert register.text == ("REGISTRE") #el nombre no existe por lo tanto devolvera false
#el problema de usarlo asi, esque no llega a driver.quit() para cerrar la pagina.

time.sleep(3)

driver.quit()
