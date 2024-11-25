import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from colorama import Fore

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options = Options()
options.binary_location = "с:/chrome-win64/chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nexaflora.tilda.ws/")

# input_username = driver.find_element(By.XPATH,'//*[@id="user-name"]')
input_password = driver.find_element(By.XPATH,'//*[@id="page-auth-form"]/table/tbody/tr[2]/td[3]/input')
login_button = driver.find_element(By.XPATH, '//*[@id="page-auth-form"]/table/tbody/tr[2]/td[4]/button')

input_password.send_keys("_6-xm.dgTEO")
login_button.send_keys(Keys.RETURN)
time.sleep(2)

goods1 = 'Суккулент Сервер'
goods2 = 'Кактус Кодинга'
goods3 = 'Эко-Пиксель'

click_fv = driver.find_element(By.XPATH, '//*[@id="rec634117022"]/div/div[1]/div[3]/a/div/div[1]/a')
# element_to_click = driver.find_element(By.XPATH, '//*[@id="rec634117022"]/div/div[1]/div[1]/a/div/div[1]/a')
click_fv.click()

try:
    bubble = Wait(driver, 2).until(ec.presence_of_element_located((By.CLASS_NAME, 't1002__bubble-container')))
    print(f"Товар '{goods3}' добавлен в Избранное.")
except TimeoutException:
    print(Fore.RED + f"Ошибка: Товар '{goods3}' не добавлен в Избранное.")

finally:
    time.sleep(1)
    driver.close()
