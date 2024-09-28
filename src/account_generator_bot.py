import os
import time
import random
import pandas as pd
from src.humen_behaviour_function import type_like_human,human_like_delay
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select




def hotmail_account_creator(driver,first_name,last_name,username,password,month,day,year):
    try:

        # # Get current working directory
        # current_working_directory = os.getcwd()

        # # Construct paths to chromedriver and extension
        # chrome_driver_path = os.path.join(current_working_directory, "chromedriver/chromedriver")
        # capsolver_extension_path = os.path.join(current_working_directory, "Extentions/capsolver_extention")
        # # captcha2_extension_path = os.path.join(current_working_directory, "Extentions/captcha2_extention")

        # # Check if chromedriver exists
        # if not os.path.isfile(chrome_driver_path):
        #     raise FileNotFoundError(f"Chromedriver not found at {chrome_driver_path}")

        # # Check if capsolver extension directory exists and contains manifest.json
        # if not os.path.isdir(capsolver_extension_path):
        #     raise FileNotFoundError(f"Capsolver extension directory not found at {capsolver_extension_path}")
        # if not os.path.isfile(os.path.join(capsolver_extension_path, "manifest.json")):
        #     raise FileNotFoundError(f"Manifest file not found in capsolver extension directory at {capsolver_extension_path}")
        
        # # Initialize Chrome service and options
        # chrome_service = Service(executable_path=chrome_driver_path)
        # chrome_options = webdriver.ChromeOptions()

        # chrome_options.add_argument("--load-extension={0}".format(capsolver_extension_path))
        # # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # if(proxy_flag == "on"):
        #     chrome_options.add_argument(f'--proxy-server={proxy}')

        # driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


        driver.get("https://signup.live.com/signup")


        wait = WebDriverWait(driver=driver,timeout=30)

        email_switch = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Get a new email address']")))
        email_switch.click()
        human_like_delay()

        email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#usernameInput')))
        type_like_human(email_element,username)
        human_like_delay()

        domain = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#domainSelect'))))
        domain.select_by_index(1)
        human_like_delay()

        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
        next_btn.click()
        human_like_delay(min_delay=2,max_delay=5)

        try:
            email_error = driver.find_element(By.CSS_SELECTOR,"div#usernameInputError")
            if(email_error):
                email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#usernameInput')))
                type_like_human(email_element,username)
                human_like_delay()

                next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
                next_btn.click()

        
        except Exception as e:
            print("Email Does not Exist")

        password_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#Password')))
        type_like_human(password_element,password)
        
        human_like_delay()
        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
        next_btn.click()


        first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#firstNameInput')))
        type_like_human(first_name_element,first_name)
        human_like_delay()
        last_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#lastNameInput')))
        type_like_human(last_name_element,last_name)
        human_like_delay()

        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
        next_btn.click()
        human_like_delay()

        # country_dropdown = Select(driver.find_element(By.ID, "countryRegionDropdown"))
        # country_dropdown.select_by_index(random.randint(50,150))  
        human_like_delay()
        birth_month_dropdown = Select(driver.find_element(By.ID, "BirthMonth"))
        birth_month_dropdown.select_by_index(month) 
        human_like_delay()
        birth_day_dropdown = Select(driver.find_element(By.ID, "BirthDay"))
        birth_day_dropdown.select_by_index(day)
        human_like_delay()
        birth_year_input = driver.find_element(By.ID, "BirthYear")
        birth_year_input.clear()
        type_like_human(birth_year_input,str(year))
        human_like_delay()
        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
        next_btn.click()

        WebDriverWait(driver, timeout=300).until(EC.url_changes(driver.current_url))

        # input("Press Enter")


        human_like_delay()
        button = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))

        button.click()
        human_like_delay()
        button = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))

        if(button.text == "OK"):    
            print(button.text)
            button.click()
        try:
            no_button = wait.until(EC.element_to_be_clickable((By.ID, "declineButton")))
            no_button.click()
        except:
            pass

        return True





        # driver.get("https://outlook.com/?refd=account.microsoft.com&fref=home.card.outlook.cold")

        # WebDriverWait(driver, timeout=180).until(EC.url_changes(driver.current_url))

        # print(email)
        # print(password)

        


        # driver.quit()

    except :
        return False
    # finally:
    #     driver.quit()





