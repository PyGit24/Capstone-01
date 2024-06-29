## Test case ID: TC_PIM_02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
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

actions=ActionChains(driver)
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

# Locating the PIM on the side pane of the admin page
pim_menu= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
pim_menu.click()

first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'))).send_keys('Nancy Albert Sha')

searchbtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
searchbtn.click()

time.sleep(5)

checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="oxd-table-row oxd-table-row--with-border oxd-table-row--clickable"]')))
checkbox.click()

checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="oxd-checkbox-wrapper"]/label/input[@type="checkbox"]')))

# click the checkbox using JavaScript
driver.execute_script("arguments[0].click();", checkbox)

#Selecting the Nationality from drop down
nationality = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div")))
nationality.click()


# nationality = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element_value("Indian"))
nation=Select(nationality)
nation.select_by_visible_text("Indian")
nation.select_by_index(5)
time.sleep(5)

gender= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="oxd-radio-wrapper"]/label/input[@type="radio"]')))

driver.execute_script("arguments[0].click();", checkbox)

# Saving the entries by clicking Save Button
savebtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')))
savebtn.click()

time.sleep(5)
