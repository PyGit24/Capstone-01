### Test case ID: TC_PIM_01

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

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
password.send_keys('admin123')

driver.maximize_window()

# Clicking the Login Button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
time.sleep(1)
login_button.click()

# verify_login= "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
# print(verify_login)

# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList')
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee')

# Locating the Menu on the side pane of the admin page
main_menu= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
main_menu.click()
drop_menu = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')))
drop_menu.click()

first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//input[@class="oxd-input oxd-input--active orangehrm-firstname"]'))).send_keys('Nancy')
mid_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//input[@class="oxd-input oxd-input--active orangehrm-middlename"]'))).send_keys('Albert')
last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//input[@class="oxd-input oxd-input--active orangehrm-lastname"]'))).send_keys('Sha')

addbtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')))

time.sleep(5)
addbtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')))

addbtn.click()
time.sleep(5)
# # wait for the checkbox to be loaded
# checkbox = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-switch-wrapper"]/label/input[@type="checkbox"]')))
#
# # click the checkbox using JavaScript
# driver.execute_script("arguments[0].click();", checkbox)
#
# username = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//label[text()="Username"]/following-sibling::div/input')))
# username.send_keys('your_username')
#
# Password = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys('madara123')
#
# # wait for the confirm password field to be loaded and enter a password
# confirm_password_field = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')))
# confirm_password_field.send_keys(Password)
