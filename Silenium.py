import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options = Options()
options.binary_location = "с:/chrome-win64/chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")

input_username = driver.find_element(By.XPATH,'//*[@id="user-name"]')
input_password = driver.find_element(By.XPATH,'//*[@id="password"]')
login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

if input_username is None:
   print("Поле Username не найдено")
else:
   print("Поле Username найдено")

if input_password is None:
   print("Поле Password не найдено")
else:
   print("Поле Password найдено")

if login_button is None:
   print("Кнопка Login не найдена")
else:
   print("Кнопка Login найдена")

input_username.send_keys("standard_user")
input_password.send_keys("secret_sauce")
login_button.send_keys(Keys.RETURN)

time.sleep(10)
driver.close()