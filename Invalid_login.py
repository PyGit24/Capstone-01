### Test case ID: TC_Login_02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time

# Setup Automatic WebDriver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Setup WebDriver path and options
# paths = r"D:\ProgramS\PyCharm\chromedriver.exe"
# os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# Getting the Webpage inputs
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


## locating the elements and providing invalid credentials for login
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
username.send_keys('Admin')

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
password.send_keys('Invalidpassword')

driver.maximize_window()

# Clicking the Login Button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()

# try:
#   # wait for 10s to load element if it did not load then it will redirect to except block
#   WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='divLoginButton']/span[@id='spanMessage']").format(str())))
# except:
#   driver.refresh()
  # locate the elemnt here again
time.sleep(5)
