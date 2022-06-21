from selenium import webdriver
# from selenium.webdriver import Firefox ##testiando
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## Driver relative directory
driver_path=Service("webdriver\\geckodriver.exe")


## Persistent profile FIrefox
profile_path = 'C:\\Users\\pedro\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\iwjqzb55.dev-edition-default'
profile_path = 'C:\\Users\\pedro\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\pk76zqg7.default-release'


## testing profiles
option=Options()
option=option.set_preference('profile', profile_path)

## General Options for the driver FUNCIONA
options = webdriver.FirefoxOptions()
options.add_argument("--width=800");
options.add_argument("--height=640");
options.add_argument("--disable-extensions");


# driver_path= 'webdriver\geckodriver.exe'

# # driver = webdriver.Firefox(executable_path=r'C:\Users\pedro\OneDrive\Documentos\test\geckodriver.exe')

# Start
browser = webdriver.Firefox(options=option, service=driver_path)
browser.get('https://www.presearch.com')


