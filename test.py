# import os
# import time
# from src.humen_behaviour_function import type_like_human,human_like_delay,random_date_generator,generate_username,generate_password,scroll
# from selenium import webdriver
# from selenium.webdriver.support.ui import  WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import undetected_chromedriver as uc
# import requests
# import random
# import pandas as pd


# def get_proxy_from_webshare():
#     try:
#         response = requests.get(
#             "https://ipv4.webshare.io/",
#             proxies={
#                 "http": "http://p.webshare.io:9999/",
#                 "https": "http://p.webshare.io:9999/"
#             }
#         )
#         response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
#         return response.text.strip() +":9999"
#     except requests.RequestException:
#         return None

# def get_proxy_from_file(proxy_file_path):
#     try:
#         with open(proxy_file_path, 'r') as file:
#             proxies = file.readlines()
#         selected_proxy = random.choice(proxies).strip().split(":")[:2]
#         return ":".join(selected_proxy)
#     except (FileNotFoundError, IndexError):
#         return None

# # def moving_cursor_and_click(driver,element):
# #     if element.is_displayed():
# #         # Get the location of the element relative to the browser window
# #         element_location = element.location
# #         element_size = element.size

# #         # Get the browser window position on the screen
# #         window_position = driver.get_window_position()
# #         window_x = window_position['x']
# #         window_y = window_position['y']

# #         # Calculate the screen coordinates of the element
# #         element_x = window_x + element_location['x'] + element_size['width'] / 2
# #         element_y = window_y + element_location['y'] + element_size['height'] / 2

# #         # print(f"Element location (relative to browser): {element_location}, size: {element_size}")
# #         # print(f"Browser window position: {window_position}")
# #         # print(f"Calculated screen coordinates: ({element_x}, {element_y})")

# #         # Move to the element location with a duration to see the movement
# #         pyautogui.moveTo(element_x, element_y +150 , duration=2)  # 2 seconds duration to see the movement
# #         time.sleep(1)  # Wait for 1 second to see the cursor at the location
# #         pyautogui.click()

# #         # Print current mouse position
# #         current_position = pyautogui.position()
# #         print(f"Current mouse position: {current_position}")
# #     else:
# #         print("Element is not visible.")


# def x_account_generator():
#     current_working_directory = os.getcwd()

#     chrome_driver_path = os.path.join(current_working_directory, "chromedriver/chromedriver")
#     capsolver_extension_path = os.path.join(current_working_directory, "Extentions/capsolver_extention")
#     # captcha2_extension_path = os.path.join(current_working_directory, "Extentions/captcha2_extention")

#     if not os.path.isfile(chrome_driver_path):
#         raise FileNotFoundError(f"Chromedriver not found at {chrome_driver_path}")


#     if not os.path.isdir(capsolver_extension_path):
#         raise FileNotFoundError(f"Capsolver extension directory not found at {capsolver_extension_path}")
#     if not os.path.isfile(os.path.join(capsolver_extension_path, "manifest.json")):
#         raise FileNotFoundError(f"Manifest file not found in capsolver extension directory at {capsolver_extension_path}")


#     chrome_service = Service(executable_path=chrome_driver_path)
#     chrome_options = webdriver.ChromeOptions()

#     chrome_options.add_argument("--load-extension={0}".format(capsolver_extension_path))
#     chrome_options.add_argument("--disable-blink-features=WebRTC")
#     # chrome_options.add_argument("--auto-open-devtools-for-tabs")
#     chrome_options.headless = True
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

#     proxy_file_path = './assets/proxyscrape_premium_http_proxies.txt'
#     # proxy = get_proxy_from_webshare()
#     # print(proxy)

#     # if proxy is None:
#     proxy = get_proxy_from_file(proxy_file_path)

#     if proxy is None:
#         raise Exception("No valid proxy found.")

#     # proxy = '104.207.43.251:3128'
#     # chrome_options.add_argument(f'--proxy-server={proxy}')

#     driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
#     # driver = uc.Chrome(service=chrome_service, options=chrome_options)
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

#     first_name,last_name,username = generate_username()
#     # password = generate_password()
#     month,day,year,year_index = random_date_generator()

#     email = "qEWSBG7gcn@hotmail.com"
#     password = r"$:-s*6BrwAd9"
#     account_image = r"/home/hassan-ahmed-khan/Dex Shit/X Account Creator/assets/images.jpeg"

#     wait = WebDriverWait(driver=driver,timeout=30)

#     driver.maximize_window()


#     driver.execute_script(f"window.open('https://x.com', '_blank');")
    

#     # input("Press Enter")
#     time.sleep(5)


#     driver.switch_to.window(driver.window_handles[1])
#     bottom_popup_cross = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="xMigrationBottomBar"]'))) 
#     actions = ActionChains(driver)
#     actions.move_to_element(bottom_popup_cross).click().perform()
#     human_like_delay()
   
#     # bottom_popup_cross.click()
#     human_like_delay()

#     create_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(.,"Create account")]')))
#     actions.move_to_element(create_btn).click().perform()
#     # create_btn.click()


#     first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="name"]')))
#     actions.move_to_element(first_name_element).click().perform()
#     type_like_human(first_name_element,username)
#     human_like_delay()

#     email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
#     actions.move_to_element(email_switch_button).click().perform()
#     # email_switch_button.click()
#     human_like_delay()

#     email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
#     actions.move_to_element(email_element).click().perform()
#     type_like_human(email_element,email)
#     human_like_delay()


#     birth_month_dropdown = (driver.find_element(By.ID, "SELECTOR_1"))
#     # birth_month_dropdown.click()
#     actions.move_to_element(birth_month_dropdown).click().perform()
    
#     # birth_month_dropdown.select_by_index(month) 
#     human_like_delay(min_delay=1,max_delay=2)

#     option = birth_month_dropdown.find_elements(By.TAG_NAME,"option")[month]
#     option.click()
#     # actions.move_to_element(option).click().perform()

#     birth_day_dropdown = (driver.find_element(By.ID, "SELECTOR_2"))
#     # birth_day_dropdown.click()
#     actions.move_to_element(birth_day_dropdown).click().perform()
#     # birth_month_dropdown.select_by_index(month) 
#     human_like_delay(min_delay=1,max_delay=2)

#     option = birth_day_dropdown.find_elements(By.TAG_NAME,"option")[day]
#     option.click()
#     # actions.move_to_element(option).click().perform()


#     # birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
#     # birth_day_dropdown.select_by_index(day)
#     # human_like_delay()

#     birth_year_input = (driver.find_element(By.ID, "SELECTOR_3"))
#     # birth_year_input.click()
#     actions.move_to_element(birth_year_input).click().perform()
#     human_like_delay(min_delay=1,max_delay=2)
#     option = birth_year_input.find_elements(By.TAG_NAME,"option")[year_index]
#     # actions.move_to_element(option).click().perform()
#     option.click()
    
#     # birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
#     # birth_year_input.select_by_value(str(year))

#     human_like_delay()
#     next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
#     # next_btn.click()
#     actions.move_to_element(next_btn).click().perform()


 

#     try:
#         arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
#         i = 0
#         while (i>=60 or arkose_challenge):
#             i+=1
#             arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')
#             time.sleep(5)
#     except:
#         print("Arkose Challenge Exit")

#     # try:
#     #     create_account_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='signupButton']")
#     #     while(create_account_button):
#     #         driver.get("https://x.com/i/flow/signup")

#     #         human_like_delay()
#     #         create_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Create account")]')))
#     #         create_btn.click()


#     #         first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="name"]')))
#     #         type_like_human(first_name_element,"DexWireBot")
#     #         human_like_delay()

#     #         email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
#     #         email_switch_button.click()
#     #         human_like_delay()

#     #         email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
#     #         type_like_human(email_element,email)
#     #         human_like_delay()
#     #         time.sleep(2)
#     #         try:
#     #             error_message_element = driver.find_element(By.XPATH, "div[@aria-live='assertive']")
#     #         except:
#     #             error_message_element = False

#     #         if(error_message_element):
#     #             print("Email Already Exist")

#     #         birth_month_dropdown = Select(driver.find_element(By.ID, "SELECTOR_1"))
#     #         birth_month_dropdown.select_by_index(month) 
#     #         human_like_delay()
#     #         birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
#     #         birth_day_dropdown.select_by_index(day)
#     #         human_like_delay()
#     #         birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
#     #         birth_year_input.select_by_value(str(year))
#     #         human_like_delay()
#     #         next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
#     #         next_btn.click()

#     #         create_account_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='signupButton']")
        

#     # except:
#     #     print("Working Properly")


#     human_like_delay(min_delay=3,max_delay=7)

#     driver.switch_to.window(driver.window_handles[0])
#     driver.get("https://login.microsoftonline.com")

#     email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="email"]')))
#     type_like_human(email_element,email)
#     human_like_delay()

#     next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="submit"]')))
#     next_btn.click()
#     human_like_delay()

#     password_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="password"]')))
#     type_like_human(password_element,password)
#     human_like_delay()

#     signin_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
#     signin_btn.click()

#     try:
#         human_like_delay()
#         decline_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button#declineButton')))
#         decline_btn.click()
#     except:   
#         pass  

#     driver.get("https://outlook.com/?refd=account.microsoft.com&fref=home.card.outlook.cold")
#     time.sleep(5)
#     human_like_delay()

#     main_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"]')))
#     email_container = main_div.find_element(By.CSS_SELECTOR,"div.customScrollBar")
#     email_container = email_container.find_element(by=By.TAG_NAME,value="div")
#     emails = email_container.find_elements(By.TAG_NAME, 'div')

#     verification_code = False
#     for div in emails:
#         try:
#             div_text = div.text
#             if (div_text.startswith('X')):
#                     try:
#                         verification_code = int(div_text.split()[1])
#                     except:
#                         verification_code = int(div_text.split()[2])
#                     break
#         except:
#             pass

#     if(not(verification_code)):
    
#         side_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#folderPaneDroppableContainer')))
#         parent_container = side_bar.find_element(By.CSS_SELECTOR, f'div[aria-labelledby="primaryMailboxRoot_{email}"]')
#         junk_email_element = parent_container.find_element(By.CSS_SELECTOR,'div[data-folder-name="junk email"]')

#         # Create an action chain to move to the element and click it
#         actions = ActionChains(driver)
#         actions.move_to_element(junk_email_element).click().perform()

#         main_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"]')))
#         email_container = main_div.find_element(By.CSS_SELECTOR,"div.customScrollBar")
#         email_container = email_container.find_element(by=By.TAG_NAME,value="div")
#         emails = email_container.find_elements(By.TAG_NAME, 'div')
#         for div in emails:
#                 try:
#                     div_text = div.text
#                     if (div_text.startswith('X')):
#                             try:
#                                 verification_code = int(div_text.split()[1])
#                             except:
#                                 verification_code = int(div_text.split()[2])
#                             print("Extracted verification code:", verification_code)
#                             break
#                     print("=================================================================")
#                 except:
#                     pass

#     driver.switch_to.window(driver.window_handles[1])

#     if(not(verification_code)):
#         buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
#         for button in buttons:
#             print(button.text)
#             print((button.text).strip() == "Didn't receive email?")
#             if((button.text).strip() == "Didn't receive email?"):
#                 button.click()

#         resend_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="menuitem"]')))
#         resend_email.click()

#         time.sleep(60)
#         driver.switch_to.window(driver.window_handles[0])

#         driver.get("https://outlook.com/?refd=account.microsoft.com&fref=home.card.outlook.cold")

#         main_div = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="listbox"]')))
#         email_container = main_div.find_element(By.CSS_SELECTOR,"div.customScrollBar")
#         email_container = email_container.find_element(by=By.TAG_NAME,value="div")
#         emails = email_container.find_elements(By.TAG_NAME, 'div')
#         for div in emails:
#                 try:
#                     div_text = div.text
#                     if (div_text.startswith('X')):
#                             try:
#                                 verification_code = int(div_text.split()[1])
#                             except:
#                                 verification_code = int(div_text.split()[2])
#                             print("Extracted verification code:", verification_code)
#                             break
#                     print("=================================================================")
#                 except:
#                     pass
#         driver.switch_to.window(driver.window_handles[1])
    
#     print("verification_code =",verification_code)
#     if(not(verification_code)):
#         driver.quit()
#         exit()

#     try:
        
#         verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))
#         # moving_cursor_and_click(driver,verification_element)
#         actions.move_to_element(verification_element).click().perform()
#         type_like_human(verification_element,str(verification_code))
#         human_like_delay()
#             # Locate and click the next button by its text
#         next_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Next']]")))
            
#             # Check if the button is enabled before clicking
#         if next_btn.is_enabled():
#             actions.move_to_element(next_btn).click().perform()
#         # moving_cursor_and_click(driver,next_btn)
#         # next_btn.click()
#         # Switch to the active element, usually the challenge or input field
#         time.sleep(5)
#         arkose_challenge = driver.switch_to.active_element
#         print("Initial active element tag:", arkose_challenge.tag_name)
        
#         while arkose_challenge.tag_name in ["button", "iframe"]:
#             arkose_challenge = driver.switch_to.active_element
#             print("In Arkose Challenge loop, active element tag:", arkose_challenge.tag_name)
        
#         print("Out of Arkose Challenge loop")
        
#         # Wait before proceeding to next steps
#         time.sleep(10)
        
#         verification_element = driver.switch_to.active_element
#         verification = verification_element.get_attribute('name')
#         print("Verification element name:", verification)
        
#         while (verification_element.get_attribute('name') == "verfication_code"):
#             print("Verification Element:", verification_element)
            
#             # Move to verification element and perform actions
#             actions = ActionChains(driver)
#             actions.move_to_element(verification_element).click().perform()
            
#             # Type verification code
#             type_like_human(verification_element, str(verification_code))
#             human_like_delay()
            
#             # Locate and click the next button by its text
#             next_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Next']]")))
            
#             # Check if the button is enabled before clicking
#             if next_btn.is_enabled():
#                 actions.move_to_element(next_btn).click().perform()
#             else:
#                 print("Next button is disabled")
            
#             try:
#                 time.sleep(5)
#                 arkose_challenge = driver.switch_to.active_element
#                 print("Next Arkose Challenge tag:", arkose_challenge.tag_name)
#                 while arkose_challenge.tag_name in ["button", "iframe"]:
#                     arkose_challenge = driver.switch_to.active_element
#                     print("In Arkose Challenge loop, active element tag:", arkose_challenge.tag_name)
#             except:
#                 print("No Arkose Challenge found after verification step")
            
#             time.sleep(10)
#             verification_element = driver.switch_to.active_element
#     except Exception as e:
#             print("Verification Passed or an error occurred:", e)
#     # try:
#     #         email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
#     #         if(email_switch_button):
#     #             email_switch_button.click()
#     #             human_like_delay()
#     #             email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
#     #             type_like_human(email_element,email)
#     #             human_like_delay()
#     #             time.sleep(2)
#     #             error_message_element = driver.find_element(By.XPATH, "//div[@aria-live='assertive']//span[contains(text(), 'Email has already been taken.')]")
#     #             if(error_message_element):
#     #                 print("Email Already Exit")

#     #             birth_month_dropdown = Select(driver.find_element(By.ID, "SELECTOR_1"))
#     #             birth_month_dropdown.select_by_index(month) 
#     #             human_like_delay()
#     #             birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
#     #             birth_day_dropdown.select_by_index(day)
#     #             human_like_delay()
#     #             birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
#     #             birth_year_input.select_by_value(str(year))
#     #             human_like_delay()
#     #             next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
#     #             next_btn.click()

#     #             try:
#     #                 arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
#     #                 i = 0
#     #                 while (i>=60 or arkose_challenge):
#     #                     i+=1
#     #                     arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')
#     #                     time.sleep(5)
#     #             except:
#     #                 print("Arkose Challenge Exist")

#     #             verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))
#     #             type_like_human(verification_element,str(verification_code))
#     #             human_like_delay()

#     #             next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
#     #             next_btn.click()
#     #             try:
#     #                 arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))

#     #                 while (arkose_challenge):
#     #                     arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')
#     #             except:
#     #                 print("Arkose Challenge Exist")

#     #             try:
#     #                 verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))
#     #                 type_like_human(verification_element,str(verification_code))
#     #                 human_like_delay()
#     #                 next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
#     #                 next_btn.click()
#     #             except:
#     #                 print("Verification Passed")

#     # except:
#     #     pass

#     # input("Press Enter Before Password")

#     password_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="password"]')))
#     type_like_human(password_element,password)
#     human_like_delay()

#     try:
#         signup_btn = driver.find_element(By.CSS_SELECTOR,'button[data-testid="LoginForm_Login_Button"]')
#         print(signup_btn)
#         signup_btn.click()
#     except:
#         print("In Exception")
#         for button in buttons:
#             print((button.text).strip().lower)
#             print(((button.text).strip().lower == "sign up"))
#             if((button.text).strip().lower == "sign up"):
#                 button.click()

    
#     human_like_delay()

#     file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))
#     file_input.send_keys(account_image)
#     human_like_delay()
#     apply_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="applyButton"]')))
#     apply_button.click()
#     human_like_delay()
#     next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSelectAvatarNextButton"]')))
#     next_button.click()
#     human_like_delay()
#     username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="username"]'))).get_attribute('value')
#     print(username)
#     skip_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfEnterUsernameSkipButton"]')))
#     skip_btn.click()
#     human_like_delay()
#     buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
#     for button in buttons:
#         print(((button.text).strip().lower() == "skip for now"))
#         print(((button.text).strip().lower() == "skip for now"))
#         if((button.text).strip().lower() == "skip for now"):
#             button.click()
# # Skip for now
#     human_like_delay()
#     interest_fields = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'li[role="listitem"]')))
#     for field in interest_fields:
#         print(field.text)
#         if((field.text).strip().lower() == "gaming") or ((field.text).strip().lower() == "business and finance") or ((field.text).strip().lower() == "technology"):
#             button = field.find_element(By.TAG_NAME,"button")
#             button.click()

#     human_like_delay()
#     try:
#         button = driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
#         button.click()
#     except:
#         print("Exception BLock")
#         buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
#         for button in buttons:
#             print(((button.text).strip().lower() == "next"))
#             print(((button.text).strip().lower() == "next"))
#             if((button.text).strip().lower() == "skip for now"):
#                 button.click()
#                 human_like_delay()
#     try:
#         button = driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
#         button.click()
#     except:
#         print("Exception BLock")
#         buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
#         for button in buttons:
#             print(((button.text).strip().lower() == "next"))
#             print(((button.text).strip().lower() == "next"))
#             if((button.text).strip().lower() == "skip for now"):
#                 button.click()

#     human_like_delay()
#     try:
#         forbes_follow_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[aria-describedby="id__swhlqfba9af"]')))
#         forbes_follow_btn.click()
#     except:
#         account_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="UserCell"]')))
#         account_follow_btn =  account_btn.find_element(By.TAG_NAME,"button")
#         account_follow_btn.click()

#     human_like_delay()
#     next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfURTUserRecommendationsNextButton"]')))
#     next_btn.click()
#     time.sleep(5)

#     driver.switch_to.active_element
#     # 
#     ok_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
#     ok_button.click()

#     try:
#         text_input =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'br[data-text="true"]')))
#     except Exception as e:
#         text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-text="true"]')))
        
    
        
#     print("===================================================")   
#     print("Tesxt Input = ",text_input)
#     print("===================================================")
    
#     if(text_input):
#         human_like_delay()

#         actions = ActionChains(driver)
#         actions.move_to_element(text_input)
#         actions.click()
#         actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE)
#         actions.send_keys("Hello Everyone")
#         actions.perform()

#         human_like_delay(min_delay=0.5, max_delay=2)
                
#         post_tweet = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')))
#         post_tweet.click()

#         human_like_delay(min_delay=3,max_delay=7)
#         try:
#             driver.get("https://x.com/logout")
            
#             human_like_delay()
#             # logout_button.click()
#             confirmation_dialog_css = "div[data-testid='confirmationSheetDialog']"
#             confirmation_button_css = "button[data-testid='confirmationSheetConfirm']"
#             wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, confirmation_dialog_css)))
#             confirmation_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, confirmation_button_css)))
#             human_like_delay()
#             confirmation_button.click()
#             WebDriverWait(driver, timeout=100).until(EC.url_changes(driver.current_url))
#         except:
#             pass

#     driver.quit()

#     account_detail = [[username, password, email, password, ""]]

#     if os.path.exists("./assets/accounts.csv") and os.path.getsize("./assets/accounts.csv") > 0:
#         try:
#             df = pd.read_csv("./assets/accounts.csv")
#             account = pd.DataFrame(account_detail, columns=["Username", "TwitterPassword", "Email", "Email Password", "2FA Token"])
#             df = pd.concat([df, account], ignore_index=True)
#         except pd.errors.EmptyDataError:
#             df = pd.DataFrame(account_detail, columns=["Username", "TwitterPassword", "Email", "Email Password", "2FA Token"])
#     else:
#         df = pd.DataFrame(account_detail, columns=["Username", "TwitterPassword", "Email", "Email Password", "2FA Token"])

#     df = df.drop_duplicates(subset=["Email"], keep="first")
#     df.to_csv("./assets/accounts.csv", index=False)


# x_account_generator()


div_text = "040542 is your X verification code"
verification_code = (div_text.split())
int(div_text.split()[1])

print(verification_code)


