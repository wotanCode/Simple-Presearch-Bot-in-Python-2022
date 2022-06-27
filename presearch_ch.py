# General importss
import time
from selenium import webdriver

# Imports for chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# BEGIN
print("Starting presearch bot wotanCode...")

## Driver relative directory
driver_path=Service("webdriver\\chromedriver.exe")

# General Options
options = webdriver.ChromeOptions()
# Path to your chrome profile
options.add_argument("user-data-dir=C:\\Users\\pedro\\AppData\\Local\\Google\\Chrome\\User Data")
browser = webdriver.Chrome(options=options, service=driver_path)

# Start
def search(item):
  print ("Searching for: " + item)
  browser.get('https://presearch.com/search?q=' + item)
  time.sleep(10)

searching = open("search.txt", "r")

for text in searching.readlines():
  search(text)

# END
browser.close()
print('END')