import os
import time
from src.humen_behaviour_function import type_like_human,human_like_delay,random_date_generator,generate_username,generate_password,scroll
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import pyautogui
import requests
import random


email = "kind.dingo.24@hotmail.com"
password = r"#h.#=q}[?QlO"

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

chrome_options.add_argument("--load-extension={0}".format(capsolver_extension_path))
chrome_options.add_argument("--disable-blink-features=WebRTC")
# chrome_options.add_argument("--auto-open-devtools-for-tabs")
chrome_options.headless = True
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

proxy_file_path = './assets/proxyscrape_premium_http_proxies.txt'
# proxy = get_proxy_from_webshare()
# print(proxy)

# if proxy is None:
# proxy = get_proxy_from_file(proxy_file_path)

# if proxy is None:
#     raise Exception("No valid proxy found.")

# proxy = '104.207.43.251:3128'
# chrome_options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# driver = uc.Chrome(service=chrome_service, options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


driver.switch_to.window(driver.window_handles[0])
driver.maximize_window()
driver.get("https://login.microsoftonline.com")


wait = WebDriverWait(driver=driver,timeout=30)

email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="email"]')))
type_like_human(email_element,email)
human_like_delay()

next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="submit"]')))
next_btn.click()
human_like_delay(min_delay=3,max_delay=5)

password_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[type="password"]')))
type_like_human(password_element,password)
human_like_delay()

signin_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
signin_btn.click()

try:
    human_like_delay()
    decline_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button#declineButton')))
    decline_btn.click()
except:   
    pass  


driver.get("https://outlook.com/?refd=account.microsoft.com&fref=home.card.outlook.cold")
time.sleep(5)
human_like_delay()


main_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"]')))
email_container = main_div.find_element(By.CSS_SELECTOR,"div.customScrollBar")
email_container = email_container.find_element(by=By.TAG_NAME,value="div")
emails = email_container.find_elements(By.TAG_NAME, 'div')

verification_code = False
for div in emails:
    try:
        div_text = div.text
        if (div_text.startswith('X')):
                try:
                    verification_code = int(div_text.split()[1])
                except:
                    verification_code = int(div_text.split()[2])
                break
    except:
        pass

if(not(verification_code)):
    
    side_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#folderPaneDroppableContainer')))
    parent_container = side_bar.find_element(By.CSS_SELECTOR, f'div[aria-labelledby="primaryMailboxRoot_{email}"]')
    junk_email_element = parent_container.find_element(By.CSS_SELECTOR,'div[data-folder-name="junk email"]')

    # Create an action chain to move to the element and click it
    actions = ActionChains(driver)
    actions.move_to_element(junk_email_element).click().perform()

    main_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"]')))
    email_container = main_div.find_element(By.CSS_SELECTOR,"div.customScrollBar")
    email_container = email_container.find_element(by=By.TAG_NAME,value="div")
    emails = email_container.find_elements(By.TAG_NAME, 'div')
    for div in emails:
            try:
                div_text = div.text
                if (div_text.startswith('X')):
                        try:
                            verification_code = int(div_text.split()[1])
                        except:
                            verification_code = int(div_text.split()[2])
                        print("Extracted verification code:", verification_code)
                        break
                print("=================================================================")
            except:
                pass

# driver.switch_to.window(driver.window_handles[1])

if(not(verification_code)):
    buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
    for button in buttons:
        print(button.text)
        print((button.text).strip() == "Didn't receive email?")
        if((button.text).strip() == "Didn't receive email?"):
            button.click()

    resend_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="menuitem"]')))
    resend_email.click()

    time.sleep(60)
    driver.switch_to.window(driver.window_handles[0])

    driver.get("https://outlook.com/?refd=account.microsoft.com&fref=home.card.outlook.cold")

    main_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"]')))
    email_container = main_div.find_element(By.CSS_SELECTOR,"div.customScrollBar")
    email_container = email_container.find_element(by=By.TAG_NAME,value="div")
    emails = email_container.find_elements(By.TAG_NAME, 'div')
    for div in emails:
            try:
                div_text = div.text
                if (div_text.startswith('X')):
                        try:
                            verification_code = int(div_text.split()[1])
                        except:
                            verification_code = int(div_text.split()[2])
                        print("Extracted verification code:", verification_code)
                        break
                print("=================================================================")
            except:
                pass




    # driver.quit()
    # exit()

print(verification_code)
input("Press Enter")