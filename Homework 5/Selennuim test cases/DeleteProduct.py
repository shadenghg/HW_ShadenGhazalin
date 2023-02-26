import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Create a Service object for the Chrome browser
service_obj = Service("Chrome Browser/chromedriver_win32/chromedriver.exe")

# Use the Service object to instantiate a Chrome driver object
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# Maximize the window
driver.maximize_window()

driver.get("http://127.0.0.1:5000/")

driver.find_element(By.XPATH, "//a[normalize-space()='Products']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "a[href='/product_info/5']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Delete Product").click()
cart_icon = driver.find_element(By.CSS_SELECTOR, '.header-icon i')
cart_icon.click()