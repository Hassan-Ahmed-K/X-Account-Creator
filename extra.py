


import os
import time
from src.humen_behaviour_function import type_like_human,human_like_delay
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import random
import os
import time
import random
import pandas as pd
from src.humen_behaviour_function import type_like_human,human_like_delay,random_date_generator,generate_username,generate_password,scroll,generate_email
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


import undetected_chromedriver as uc

import os
import time
from src.humen_behaviour_function import type_like_human,human_like_delay
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import random





# Specify the path to chromedriver
chromedriver_path = '/home/hassan-ahmed-khan/Dex Shit/X Account Creator/chromedriver/chromedriver'

# Set up the proxy server
proxy = ''

proxy_options = {
    'proxy': {
        'http': 'http://sphuioau:x5vhup3coy2q@45.127.248.127:5128',
    }
}



first_name,last_name,_ = generate_username()
password = generate_password()
username = generate_email()
month,day,year,year_index = random_date_generator()


current_working_directory = os.getcwd()

chrome_driver_path = os.path.join(current_working_directory, "chromedriver/chromedriver")
capsolver_extension_path = os.path.join(current_working_directory, "Extentions/capsolver_extention")
# captcha2_extension_path = os.path.join(current_working_directory, "Extentions/captcha2_extention")

if not os.path.isfile(chrome_driver_path):
    raise FileNotFoundError(f"Chromedriver not found at {chrome_driver_path}")


if not os.path.isdir(capsolver_extension_path):
    raise FileNotFoundError(f"Capsolver extension directory not found at {capsolver_extension_path}")
if not os.path.isfile(os.path.join(capsolver_extension_path, "manifest.json")):
    raise FileNotFoundError(f"Manifest file not found in capsolver extension directory at {capsolver_extension_path}")


chrome_service = Service(executable_path=chrome_driver_path)
chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument("--load-extension={0}".format(capsolver_extension_path))
chrome_options.add_argument("--disable-blink-features=WebRTC")
# chrome_options.add_argument("--auto-open-devtools-for-tabs")
# chrome_options.headless = True
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = uc.Chrome(service=chrome_service, options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Open Google to test the proxy
driver.get('https://accounts.google.com')

actions = ActionChains(driver)
wait = WebDriverWait(driver=driver,timeout=30)
create_account_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[aria-haspopup="menu"]')))
actions.move_to_element(create_account_btn).click().perform()
human_like_delay()
personal_use_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'li[role="menuitem"]')))
actions.move_to_element(personal_use_btn).click().perform()

# input("Press Enter")
first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="firstName"]')))
type_like_human(first_name_element,first_name)
human_like_delay()
last_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="lastName"]')))
type_like_human(last_name_element,last_name)
human_like_delay()
next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="button"]')))
actions.move_to_element(next_btn).click().perform()
human_like_delay(min_delay=3,max_delay=5)

birth_month = (wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'select#month'))))


actions.move_to_element(birth_month).click().perform()
        # birth_month_dropdown.select_by_index(month) 
human_like_delay(min_delay=1,max_delay=2)
option = birth_month.find_elements(By.TAG_NAME,"option")[month]
# actions.move_to_element(option).click().perform()
option.click()
human_like_delay()
birth_day = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#day')))
# birth_day.type(day)
type_like_human(birth_day,str(day))
human_like_delay()
birth_year = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#year')))
type_like_human(birth_year,str(year))
gender = (wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#gender'))))
actions.move_to_element(gender).click().perform()
        # birth_month_dropdown.select_by_index(month) 
human_like_delay(min_delay=1,max_delay=2)

option = gender.find_elements(By.TAG_NAME,"option")[random.randint(1,3)]
# actions.move_to_element(option).click().perform()
option.click()
human_like_delay()
next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="button"]')))
actions.move_to_element(next_btn).click().perform()
time.sleep(10)

try:
    container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="radiogroup"]')))
    print(container)
    human_like_delay()
except:
    container = False
    print("No Suggested Email")

if (container):
    radio_options = container.find_elements(By.XPATH, '//div[@role="radio"]')
    radio_option = random.choice(radio_options[:(len(radio_options)-1)])
    actions.move_to_element(radio_option).click().perform()
    human_like_delay()
else:
    username_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="Username"]')))
    type_like_human(username_element,username)
    human_like_delay()

next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="button"]')))
actions.move_to_element(next_btn).click().perform()
    
# try:
#     custom_email_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Create your own Gmail address"]')))
#     custom_email_element.click()
# except:
#     print("No Suggested Email")

password = generate_password()
password_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[name="Passwd"]')))
type_like_human(password_element,str(password))
human_like_delay()
password_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[name="PasswdAgain"]')))
type_like_human(password_element,str(password))
human_like_delay()
next_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[type="button"]')))
actions.move_to_element(next_btn).click().perform()

# Perform actions on the webpage as needed
# ...
input("Press Enter")
# Close the browser
driver.quit()

