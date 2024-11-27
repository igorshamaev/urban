import time
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

ch_options = Options()
ch_options.add_experimental_option("excludeSwitches", ["enable-logging"])
ch_options.binary_location = "c:/chrome-win64/chrome.exe"
driver = webdriver.Chrome(options=ch_options)
driver.get("https://nexaflora.tilda.ws/")

input_password = driver.find_element(By.XPATH,'//*[@id="page-auth-form"]/table/tbody/tr[2]/td[3]/input')
login_button = driver.find_element(By.XPATH, '//*[@id="page-auth-form"]/table/tbody/tr[2]/td[4]/button')

input_password.send_keys("_6-xm.dgTEO")
login_button.send_keys(Keys.RETURN)

goods1 = 'Суккулент Сервер'
goods2 = 'Кактус Кодинга'
goods3 = 'Эко-Пиксель'

time.sleep(8)
click_fv = driver.find_element(By.XPATH, '//*[@id="rec634117022"]/div/div[1]/div[1]/a/div/div[1]/a')
click_fv.click() # FV1 click

time.sleep(2)
click_fv = driver.find_element(By.XPATH, '//*[@id="rec634117022"]/div/div[1]/div[2]/a/div/div[1]/a')
click_fv.click() # FV2 click

time.sleep(2)
click_fv = driver.find_element(By.XPATH, '//*[@id="rec634117022"]/div/div[1]/div[3]/a/div/div[1]/a')
click_fv.click() # FV3 click

time.sleep(2)
click_fv = driver.find_element(By.CLASS_NAME, 't1002__wishlisticon-imgwrap')
click_fv.click() # FV_list_open click

print('-----------------------------------------------------')
try:
    added_fv = Wait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//*[@id="rec634117498"]/div/div[2]/div/div[3]/div[1]')))
    print(f"Товар1 '{goods1}' добавлен в Избранное.")
    print(Fore.GREEN + f"Тест1 пройден." + Style.RESET_ALL)
except TimeoutException:
    print(Fore.YELLOW + f"Ошибка: Товар1 '{goods1}' не добавлен в Избранное!")
    print(Fore.RED + f"Тест1.1 не пройден." + Style.RESET_ALL)
print('-----------------------------------------------------')
try:
    added_fv = Wait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//*[@id="rec634117498"]/div/div[2]/div/div[3]/div[2]')))
    print(f"Товар2 '{goods2}' добавлен в Избранное.")
    print(Fore.GREEN + f"Тест2 пройден." + Style.RESET_ALL)
except TimeoutException:
    print(Fore.YELLOW + f"Ошибка: Товар2 '{goods2}' не добавлен в Избранное!")
    print(Fore.RED + f"Тест2.1 не пройден." + Style.RESET_ALL)
print('-----------------------------------------------------')
try:
    added_fv = Wait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//*[@id="rec634117498"]/div/div[2]/div/div[3]/div[3]')))
    print(f"Товар3 '{goods3}' добавлен в Избранное.")
    print(Fore.GREEN + f"Тест3 пройден." + Style.RESET_ALL)
except TimeoutException:
    print(Fore.YELLOW + f"Ошибка: Товар3 '{goods3}' не добавлен в Избранное!")
    print(Fore.RED + f"Тест3.1 не пройден." + Style.RESET_ALL)
print('-----------------------------------------------------')
time.sleep(5)
try:
    click_fv = driver.find_element(By.XPATH, '//*[@id="rec634117498"]/div/div[2]/div/div[3]/div[1]/div[4]/img')
    click_fv.click()  # Remove FV1 click
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="rec634117498"]/div/div[2]/div/div[3]/div[1]')
    print(Fore.YELLOW + f"Ошибка: Товар1 '{goods1}' не удалён из Избранного!")
    print(Fore.RED + f"Тест1.2 не пройден." + Style.RESET_ALL)
except NoSuchElementException:
    print(f"Товар1 '{goods1}' удалён из Избранного.")
    print(Fore.GREEN + f"Тест1.2 пройден." + Style.RESET_ALL)

    click_fv = driver.find_element(By.XPATH, '//*[@id="rec634117498"]/div/div[2]/div/div[1]/button')
    click_fv.click() # Close_FV_list click

finally:
    time.sleep(2)
    driver.close()