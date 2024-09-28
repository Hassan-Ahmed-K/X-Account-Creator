
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

import time
from src.humen_behaviour_function import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd

# api_key = os.getenv('APIKEY_2CAPTCHA', '36c969b0cacd5d4b2429b3177ac03e38')

# solver = TwoCaptcha(api_key)



# 36c969b0cacd5d4b2429b3177ac03e38

# email = "ebtineccompva3088@rambler.ru"
# password = "LgbQBRJe^2GYC+NDA2"



def ramble_login(email,password,confirmation_code_lock_screen=False):

    try:

        # Get current working directory
        current_working_directory = os.getcwd()

        # Construct paths to chromedriver and extension
        chrome_driver_path = os.path.join(current_working_directory, "chromedriver/chromedriver.exe")
        capsolver_extension_path = os.path.join(current_working_directory, "Extentions/capsolver_extension")
        captcha2_extension_path = os.path.join(current_working_directory, "Extentions/captcha2_extention")


        # Check if chromedriver exists
        if not os.path.isfile(chrome_driver_path):
            raise FileNotFoundError(f"Chromedriver not found at {chrome_driver_path}")

        # Check if capsolver extension directory exists and contains manifest.json
        if not os.path.isdir(capsolver_extension_path):
            raise FileNotFoundError(f"Capsolver extension directory not found at {capsolver_extension_path}")
        if not os.path.isfile(os.path.join(capsolver_extension_path, "manifest.json")):
            raise FileNotFoundError(f"Manifest file not found in capsolver extension directory at {capsolver_extension_path}")

        if not os.path.isdir(captcha2_extension_path):
            raise FileNotFoundError(f"Capsolver extension directory not found at {captcha2_extension_path}")
        if not os.path.isfile(os.path.join(captcha2_extension_path, "manifest.json")):
            raise FileNotFoundError(f"Manifest file not found in capsolver extension directory at {captcha2_extension_path}")

        # Initialize Chrome service and options
        chrome_service = Service(executable_path=chrome_driver_path)
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument(f"--load-extension={capsolver_extension_path},{captcha2_extension_path}")

        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        prefs = {
            "profile.default_content_setting_values.notifications": 2  # 1: Allow, 2: Block
        }
        chrome_options.add_experimental_option("prefs", prefs)


        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.maximize_window()
        # driver.execute_script(f"window.open('https://mail.rambler.ru/', '_blank');")
        driver.get("https://mail.rambler.ru/")
        driver.switch_to.window(driver.window_handles[0])

        wait = WebDriverWait(driver=driver,timeout=30)
        time.sleep(5)
        iframe = driver.find_element(By.TAG_NAME,"iframe")

        driver.switch_to.frame(iframe)

        email_input = driver.find_element(By.ID, "login")
        type_like_human(email_input,email)

        password_input = driver.find_element(By.ID, "password")
        type_like_human(password_input,password)

        login_button = driver.find_element(By.CSS_SELECTOR, "button[data-cerber-id='login_form::main::login_button']")
        login_button.click()
        print("Login Button CLicked")
        try:
            h_captcha = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe')))
            captcha_solver_status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.captcha-solver'))).text
            i=0
            print(captcha_solver_status != "Captcha solved!")
            while((captcha_solver_status != "Captcha solved!")):
                if(i==20):
                    break
                captcha_solver_status = driver.find_element(By.CSS_SELECTOR,'div.captcha-solver').text
                time.sleep(3)
                i+=1
            login_button = driver.find_element(By.CSS_SELECTOR, "button[data-cerber-id='login_form::main::login_button']")
            login_button.click()
            time.sleep(10)
                
        except:
            print("Pass the H_Captcha")


        driver.refresh()
        time.sleep(5)

        try:
            cross_button = WebDriverWait(driver=driver,timeout=10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.styles-close-5S')))
            cross_button.click()
        except Exception as e:
            pass

        mails_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.MailList-list-2L')))
        mails = mails_container.find_elements(By.CSS_SELECTOR,'div[draggable="true"]')

        for mail in mails:
            try:
                if(confirmation_code_lock_screen):
                    verification_element = mail.find_element(By.CSS_SELECTOR,"div.ListItem-sender-2L")
                    if (str(verification_element.text) == "verify"):
                        verification_email = mail.find_element(By.CSS_SELECTOR,"a.ListItem-root-1i")
                        verification_email.click()
                        # wait.until(EC.url_changes(driver.current_url))
                        time.sleep(5)
                        email_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.AppContainer-mainContainer-3e")))
                        email_content = email_container.find_element(By.CSS_SELECTOR,"div.LetterBody-root-3k")
                        email_table = email_content.find_element(By.TAG_NAME,"table")
                        verification_code = email_table.find_element(By.CSS_SELECTOR,"td.h1.black").text
                        print(verification_code)
                        return verification_code
                        
                    # verification_code = str(verification_element.text).split()[5]
                else:
                    verification_element = mail.find_element(By.CSS_SELECTOR,"div.ListItem-title-2m")
                    
                    if (str(verification_element.text).split()[1] == "X"):
                        verification_code = verification_element.find_element(By.CSS_SELECTOR,"span.ListItem-subject-2M ").text
                        
                        verification_code = verification_code.split(" ")[5]
                        return verification_code

            except:
                return False
    except:
        return False
    

