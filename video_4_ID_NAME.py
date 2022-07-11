
from selenium import webdriver

import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.netflix.com/es/')
time.sleep(1)


email = driver.find_element(By.CLASS_NAME,'nfTextField')
email.click()
email.send_keys("AHORA SIIIIIII!!!!!@gmal.com")

time.sleep(1)
boton_empezar = driver.find_element(By.ID,'//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div/div/button')
boton_empezar.click()




time.sleep(2)
driver.close()
driver.quit()
