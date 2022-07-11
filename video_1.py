from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com") #carga del sitio

time.sleep(3)
#elementos del sitio en los que voy a trabajar
user_box = driver.find_element_by_name('userName')
pass_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_name('login')

#interaccion o acciones que queremos que ejecuten  esos elementos
user_box.send_Keys('clave') #rellena con el nombre clave el cuadro de texto
pass_box.send_Keys('clave')
submit_button.click()

time.sleep(3)
driver.quit()


