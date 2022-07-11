from selenium import webdriver


#chrome_path = r"C:/Users/Jose Luis/Desktop/Escritorio Mauro/QA TESTER AUTOMATIZACION/chromedriver.exe"
driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com")
user_box = driver.find