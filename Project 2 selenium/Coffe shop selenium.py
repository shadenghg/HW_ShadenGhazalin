# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Set up the options for the Chrome browser
chrome_options = Options()

# Add an experimental option to keep the browser window open after the script finishes
chrome_options.add_experimental_option("detach", True)

# Create a Service object for the Chrome browser, pointing to the location of the ChromeDriver executable
service_obj = Service("Chrome Browser/chromedriver_win32/chromedriver.exe")

# Use the Service object to instantiate a Chrome driver object, passing in the options we just defined
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# Set an implicit wait of 3 seconds, which will be applied to all subsequent find_element and find_elements calls
driver.implicitly_wait(3)

# Maximize the window to ensure the elements we need are visible
driver.maximize_window()

# Load the target URL
driver.get("http://127.0.0.1:5000")

########################################################################

# Check that I am redirected to the homepage after logging in.
