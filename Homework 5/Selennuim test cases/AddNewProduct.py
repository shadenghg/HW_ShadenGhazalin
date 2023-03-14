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


# ADD NEW PRODUCT:
driver.find_element(By.XPATH, "//a[normalize-space()='Products']").click()
time.sleep(3)
# Click on the "Add new product" button
driver.find_element(By.XPATH, "//a[normalize-space()='Add new product']").click()

# Fill out the form and submit it
driver.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Samana/Copy/static/images/p12.png")
driver.find_element(By.NAME, "product_name").send_keys("Instant Coffee")
driver.find_element(By.NAME, "product_price").send_keys("$ 9.99")
driver.find_element(By.NAME, "product_quantity").send_keys("60")
driver.find_element(By.NAME, "product_description").send_keys("Instant coffee is made from real coffee beans. The "
                                                              "soluble and volatile contents of the beans are "
                                                              "extracted. Then the water is removed so powder or "
                                                              "concentrated soluble coffee powder are left over. It’s "
                                                              "essentially been dehydrated for our convenience – just "
                                                              "add water and you have yourself a brew!")
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='ADD THE PRODUCT']").click()
