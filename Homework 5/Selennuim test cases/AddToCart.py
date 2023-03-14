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
driver.find_element(By.LINK_TEXT, "Shop Now").click()
# Locate the "Add to cart" button and click on it
add_to_cart_button = driver.find_element(By.XPATH, '//body[1]/section[1]/div[2]/div[1]/div[1]/a[1]')
add_to_cart_button.click()

# products = driver.find_elements(By.XPATH, "(//div[@class='box'])")
# assert len(products) > 0, "You didn't get anything"
# i = 0
# for product in products:
#     print(i)
#     product.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])").click()
#     driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
#     i += 1
#
# Verify that the product has been added to the cart list
cart_icon = driver.find_element(By.CSS_SELECTOR, '.header-icon i')
cart_icon.click()