## Test case ID: TC_PIM_03

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Setup WebDriver path and options
# paths = r"D:\ProgramS\PyCharm\chromedriver.exe"
# os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# Getting the Webpage
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


## locating the elements and providing credentials for login
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))

username.send_keys('Admin')

password = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
password.send_keys('admin123')

driver.maximize_window()

# Clicking the Login Button
login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
time.sleep(1)
login_button.click()

# Locating the PIM on the side pane of the admin page
pim_menu= WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
pim_menu.click()

first_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'))).send_keys('Nancy Albert Sha')

searchbtn = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
searchbtn.click()
time.sleep(5)

checkbox2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i")))
checkbox2.click()

time.sleep(5)

confirm_delete= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,("/html/body/div/div[3]/div/div/div/div[3]/button[2]"))))
confirm_delete.click()
time.sleep(10)
