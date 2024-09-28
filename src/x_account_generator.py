import os
import time
from src.humen_behaviour_function import type_like_human,human_like_delay,generate_human_name
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import random



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


def x_account_generator(driver,email,password,month,day,year_index,email_type):

    try:
        print('Infunction')
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            # Check if the URL of the tab starts with 'chrome-extension://'
            if driver.current_url.startswith("chrome-extension://"):
                # Close the tab
                driver.close()

        base_dir = os.getcwd() + r'\assets\Profile Images'
        profile_image_path = os.path.join(base_dir,random.choice(os.listdir(base_dir))) 
        # account_image = current_working_directory + "/assets/images.jpeg"
        # print(account_image)

        # wait = WebDriverWait(driver=driver,timeout=30)
        wait = WebDriverWait(driver=driver,timeout=30)

        driver.maximize_window()

        _, _, username = generate_human_name()
        print('Username')
        driver.execute_script(f"window.open('https://x.com', '_blank');")
        

        driver.switch_to.window(driver.window_handles[1])
        bottom_popup_cross = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="xMigrationBottomBar"]'))) 
        actions = ActionChains(driver)
        actions.move_to_element(bottom_popup_cross).click().perform()
        human_like_delay()
    
        # bottom_popup_cross.click()
        human_like_delay()

        create_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(.,"Create account")]')))
        actions.move_to_element(create_btn).click().perform()
        # create_btn.click()


        first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="name"]')))
        actions.move_to_element(first_name_element).click().perform()
        type_like_human(first_name_element,username)
        human_like_delay()

        email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
        actions.move_to_element(email_switch_button).click().perform()
        # email_switch_button.click()
        human_like_delay()

        email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
        actions.move_to_element(email_element).click().perform()
        type_like_human(email_element,email)
        human_like_delay(min_delay=1,max_delay=2)


        birth_month_dropdown = (driver.find_element(By.ID, "SELECTOR_1"))
        # birth_month_dropdown.click()
        actions.move_to_element(birth_month_dropdown).click().perform()
        
        # birth_month_dropdown.select_by_index(month) 
        human_like_delay(min_delay=1,max_delay=2)

        option = birth_month_dropdown.find_elements(By.TAG_NAME,"option")[month]
        option.click()
        # actions.move_to_element(option).click().perform()

        birth_day_dropdown = (driver.find_element(By.ID, "SELECTOR_2"))
        # birth_day_dropdown.click()
        actions.move_to_element(birth_day_dropdown).click().perform()
        # birth_month_dropdown.select_by_index(month) 
        human_like_delay(min_delay=1,max_delay=2)

        option = birth_day_dropdown.find_elements(By.TAG_NAME,"option")[day]
        option.click()
        # actions.move_to_element(option).click().perform()


        # birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
        # birth_day_dropdown.select_by_index(day)
        # human_like_delay()

        birth_year_input = (driver.find_element(By.ID, "SELECTOR_3"))
        # birth_year_input.click()
        actions.move_to_element(birth_year_input).click().perform()
        human_like_delay(min_delay=1,max_delay=2)
        option = birth_year_input.find_elements(By.TAG_NAME,"option")[year_index]
        # actions.move_to_element(option).click().perform()
        option.click()
        
        # birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
        # birth_year_input.select_by_value(str(year))

        human_like_delay(min_delay=1,max_delay=2)
        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
        # next_btn.click()
        actions.move_to_element(next_btn).click().perform()




        try:
            arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
            i = 0
            while (i>=60 or arkose_challenge):
                i+=1
                arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')
                time.sleep(5)
        except:
            print("Arkose Challenge Exit")

        # try:
        #     create_account_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='signupButton']")
        #     while(create_account_button):
        #         driver.get("https://x.com/i/flow/signup")

        #         human_like_delay()
        #         create_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Create account")]')))
        #         create_btn.click()


        #         first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="name"]')))
        #         type_like_human(first_name_element,"DexWireBot")
        #         human_like_delay()

        #         email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
        #         email_switch_button.click()
        #         human_like_delay()

        #         email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
        #         type_like_human(email_element,email)
        #         human_like_delay()
        #         time.sleep(2)
        #         try:
        #             error_message_element = driver.find_element(By.XPATH, "div[@aria-live='assertive']")
        #         except:
        #             error_message_element = False

        #         if(error_message_element):
        #             print("Email Already Exist")

        #         birth_month_dropdown = Select(driver.find_element(By.ID, "SELECTOR_1"))
        #         birth_month_dropdown.select_by_index(month) 
        #         human_like_delay()
        #         birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
        #         birth_day_dropdown.select_by_index(day)
        #         human_like_delay()
        #         birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
        #         birth_year_input.select_by_value(str(year))
        #         human_like_delay()
        #         next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
        #         next_btn.click()

        #         create_account_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='signupButton']")
            

        # except:
        #     print("Working Properly")


        human_like_delay(min_delay=5,max_delay=10)

        driver.switch_to.window(driver.window_handles[0])
        # driver.get("https://login.microsoftonline.com")

        # email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="email"]')))
        # type_like_human(email_element,email)
        # human_like_delay()

        # next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="submit"]')))
        # next_btn.click()
        # human_like_delay()

        # password_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="password"]')))
        # type_like_human(password_element,password)
        # human_like_delay()

        # signin_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
        # signin_btn.click()

        # try:
        #     human_like_delay()
        #     decline_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button#declineButton')))
        #     decline_btn.click()
        # except:   
        #     pass  
        if(email_type == "hotmail"):
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
                                        verification_code = (div_text.split()[1])
                                        int(div_text.split()[1])
                                    except:
                                        verification_code = (div_text.split()[2])
                                        int(div_text.split()[1])
                                    print("Extracted verification code:", verification_code)
                                    break
                        except:
                            pass

            driver.switch_to.window(driver.window_handles[1])

            if(not(verification_code)):
                buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
                for button in buttons:
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
                                    break
                        except:
                            pass
                
            
            print("verification_code =",verification_code)
            if(not(verification_code)):
                
                return False,'_'
            
        # input("Press Enter")
        if(email_type == "rambler"):
            # driver.refresh()
            time.sleep(5)
            mails_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.MailList-list-2L')))
            mails = mails_container.find_elements(By.CSS_SELECTOR,'div[draggable="true"]')
            verification_code = False
            for mail in mails:
                try:
                    verification_element = mail.find_element(By.CSS_SELECTOR,"div.ListItem-title-2m")
                    

                    if (str(verification_element.text).split()[3] == "X"):
                        # verification_code = verification_element.find_element(By.CSS_SELECTOR,"span.ListItem-subject-2M ").text
                        # print(verification_code)
                        verification_code = verification_element.text.split(" ")[0]
                except:
                    pass

            if(not(verification_code)):
                driver.switch_to.window(driver.window_handles[1])
                buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
                for button in buttons:
                    print((button.text).strip() == "Didn't receive email?")
                    if((button.text).strip() == "Didn't receive email?"):
                        button.click()

                resend_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="menuitem"]')))
                resend_email.click()

                time.sleep(60)
                driver.switch_to.window(driver.window_handles[0])
                driver.refresh()
                mails_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.MailList-list-2L')))
                mails = mails_container.find_elements(By.CSS_SELECTOR,'div[draggable="true"]')
                verification_code = False
                for mail in mails:
                    try:
                        verification_element = mail.find_element(By.CSS_SELECTOR,"div.ListItem-title-2m")
                        

                        if (str(verification_element.text).split()[3] == "X"):
                            # verification_code = verification_element.find_element(By.CSS_SELECTOR,"span.ListItem-subject-2M ").text
                            # print(verification_code)
                            verification_code = verification_element.text.split(" ")[0]
                    except:
                        pass
                if(not(verification_code)):
                    # driver.quit()
                    return False,'_'
            
        try:
            
            driver.switch_to.window(driver.window_handles[1])
            verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))
            # moving_cursor_and_click(driver,verification_element)
            actions.move_to_element(verification_element).click().perform()
            type_like_human(verification_element,str(verification_code))
            human_like_delay()
                # Locate and click the next button by its text
            next_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Next']]")))
                
                # Check if the button is enabled before clicking
            if next_btn.is_enabled():
                actions.move_to_element(next_btn).click().perform()
            # moving_cursor_and_click(driver,next_btn)
            # next_btn.click()
            # Switch to the active element, usually the challenge or input field
            time.sleep(5)
            arkose_challenge = driver.switch_to.active_element
            print("Initial active element tag:", arkose_challenge.tag_name)
            
            while arkose_challenge.tag_name in ["button", "iframe"]:
                arkose_challenge = driver.switch_to.active_element
                print("In Arkose Challenge loop, active element tag:", arkose_challenge.tag_name)
            
            print("Out of Arkose Challenge loop")
            
            # Wait before proceeding to next steps
            time.sleep(5)
            
            verification_element = driver.switch_to.active_element
            verification = verification_element.get_attribute('name')
            print("Verification element name:", verification)
            
            while (verification_element.get_attribute('name') == "verfication_code"):
                print("Verification Element:", verification_element)
                
                # Move to verification element and perform actions
                actions = ActionChains(driver)
                actions.move_to_element(verification_element).click().perform()
                
                # Type verification code
                type_like_human(verification_element, str(verification_code))
                human_like_delay()
                
                # Locate and click the next button by its text
                next_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Next']]")))
                
                # Check if the button is enabled before clicking
                if next_btn.is_enabled():
                    actions.move_to_element(next_btn).click().perform()
                else:
                    print("Next button is disabled")
                
                try:
                    time.sleep(5)
                    arkose_challenge = driver.switch_to.active_element
                    print("Next Arkose Challenge tag:", arkose_challenge.tag_name)
                    while arkose_challenge.tag_name in ["button", "iframe"]:
                        arkose_challenge = driver.switch_to.active_element
                        print("In Arkose Challenge loop, active element tag:", arkose_challenge.tag_name)
                except:
                    print("No Arkose Challenge found after verification step")
                
                time.sleep(10)
                verification_element = driver.switch_to.active_element
        except Exception as e:
                print("Verification Passed or an error occurred:", e)
        # try:
        #         email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
        #         if(email_switch_button):
        #             email_switch_button.click()
        #             human_like_delay()
        #             email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
        #             type_like_human(email_element,email)
        #             human_like_delay()
        #             time.sleep(2)
        #             error_message_element = driver.find_element(By.XPATH, "//div[@aria-live='assertive']//span[contains(text(), 'Email has already been taken.')]")
        #             if(error_message_element):
        #                 print("Email Already Exit")

        #             birth_month_dropdown = Select(driver.find_element(By.ID, "SELECTOR_1"))
        #             birth_month_dropdown.select_by_index(month) 
        #             human_like_delay()
        #             birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
        #             birth_day_dropdown.select_by_index(day)
        #             human_like_delay()
        #             birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
        #             birth_year_input.select_by_value(str(year))
        #             human_like_delay()
        #             next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
        #             next_btn.click()

        #             try:
        #                 arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
        #                 i = 0
        #                 while (i>=60 or arkose_challenge):
        #                     i+=1
        #                     arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')
        #                     time.sleep(5)
        #             except:
        #                 print("Arkose Challenge Exist")

        #             verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))
        #             type_like_human(verification_element,str(verification_code))
        #             human_like_delay()

        #             next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
        #             next_btn.click()
        #             try:
        #                 arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))

        #                 while (arkose_challenge):
        #                     arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')
        #             except:
        #                 print("Arkose Challenge Exist")

        #             try:
        #                 verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))
        #                 type_like_human(verification_element,str(verification_code))
        #                 human_like_delay()
        #                 next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
        #                 next_btn.click()
        #             except:
        #                 print("Verification Passed")

        # except:
        #     pass

        # input("Press Enter Before Password")

        password_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="password"]')))
        type_like_human(password_element,password)
        human_like_delay()

        try:
            signup_btn = driver.find_element(By.CSS_SELECTOR,'button[data-testid="LoginForm_Login_Button"]')
            print(signup_btn)
            signup_btn.click()
        except:
            print("In Exception")
            for button in buttons:
                print((button.text).strip().lower)
                print(((button.text).strip().lower == "sign up"))
                if((button.text).strip().lower == "sign up"):
                    button.click()

        
        human_like_delay()

        file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))
        file_input.send_keys(profile_image_path)
        human_like_delay()
        apply_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="applyButton"]')))
        apply_button.click()
        human_like_delay()
        next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSelectAvatarNextButton"]')))
        next_button.click()
        human_like_delay()

        username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="username"]'))).get_attribute('value')

        skip_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfEnterUsernameSkipButton"]')))
        skip_btn.click()
        human_like_delay()
        buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        for button in buttons:
            print(((button.text).strip().lower() == "skip for now"))
            print(((button.text).strip().lower() == "skip for now"))
            if((button.text).strip().lower() == "skip for now"):
                button.click()
    # Skip for now
        human_like_delay()
        try:
            interest_fields = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'li[role="listitem"]')))
            interest_fields = random.sample(interest_fields,6)
            for field in interest_fields:
                print(field.text)
                # if((field.text).strip().lower() == "gaming") or ((field.text).strip().lower() == "business and finance") or ((field.text).strip().lower() == "technology"):
                button = field.find_element(By.TAG_NAME,"button")
                try:
                    button.click()
                except:
                    pass

            human_like_delay()
            try:
                button = driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
                button.click()
            except:
                print("Exception BLock")
                buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
                for button in buttons:
                    print(((button.text).strip().lower() == "next"))
                    print(((button.text).strip().lower() == "next"))
                    if((button.text).strip().lower() == "skip for now"):
                        button.click()
                        human_like_delay()
            
            try:
                button = driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
                button.click()
            except:
                print("Exception BLock")
                buttons = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
                for button in buttons:
                    print(((button.text).strip().lower() == "next"))
                    print(((button.text).strip().lower() == "next"))
                    if((button.text).strip().lower() == "skip for now"):
                        button.click()

            human_like_delay()
            try:
                # forbes_follow_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[aria-describedby="id__swhlqfba9af"]')))
                # forbes_follow_btn.click()
                account_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="UserCell"]')))
                account_follow_btn =  account_btn.find_element(By.TAG_NAME,"button")
                account_follow_btn.click()
            except:
                # account_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="UserCell"]')))
                # account_follow_btn =  account_btn.find_element(By.TAG_NAME,"button")
                # account_follow_btn.click()
                pass

            human_like_delay()
            next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfURTUserRecommendationsNextButton"]')))
            next_btn.click()
            time.sleep(10)

            driver.switch_to.active_element
            # 
            ok_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
            ok_button.click()
        except:
            pass


    #    ====================== like comment & repost ===================================================

        try:
            driver.refresh()
            # posts_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'section[aria-labelledby="accessible-list-0"]')))
            # posts = posts_section.find_elements(By.CSS_SELECTOR,'div[data-testid="cellInnerDiv"]')
            posts = driver.find_elements(By.CSS_SELECTOR,'div[data-testid="cellInnerDiv"]')
            posts = random.sample(posts,random.randint(1,5))
            for post_container in posts:
                try:
                    post = post_container.find_element(By.CSS_SELECTOR,'article[role="article"]')
                    print("post_container = ",post_container)

                    like = post.find_element(By.CSS_SELECTOR,'button[data-testid="like"]')
                    print("like = ",like)
                    like.click()
                    human_like_delay()

                    retweet = post.find_element(By.CSS_SELECTOR,'button[data-testid="retweet"]')
                    retweet.click()
                    human_like_delay()
                    retweet_confirm  = driver.switch_to.active_element
                    retweet_confirm = driver.find_element(By.CSS_SELECTOR,'div[data-testid="retweetConfirm"]')
                    retweet_confirm.click()

                    human_like_delay(min_delay=3,max_delay=7)
                    try:
                        cross_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[aria-label="Close"]')))
                        cross_btn.click()
                    except:
                        pass

                    comments = [
                        "I completely agree with you on this one! 👍",
                        "Absolutely, couldn’t have said it better myself!",
                        "Yes, that’s exactly what I was thinking too!",
                        "You’re spot on with that observation!",
                        "Totally agree! This is so true!",
                        "Couldn’t agree more with your point here!",
                        "100% agree, you nailed it!",
                        "That’s exactly what I was going to say! Great minds think alike.",
                        "You’re absolutely right! I’m with you on this.",
                        "I’m on the same page as you. Well said!",
                        "I see where you’re coming from, but I have a different perspective.",
                        "I respect your opinion, but I have to disagree on this one.",
                        "Interesting point, but I’m not sure I agree with that.",
                        "I get what you’re saying, but I think there’s more to it.",
                        "I have a different take on this, but I appreciate your input.",
                        "I understand your view, but I see it a bit differently.",
                        "I see your point, but I have to disagree.",
                        "I respect your opinion, but I have to disagree.",
                        "That’s an interesting perspective, but I’m not sure I’m convinced.",
                        "I can see where you're coming from, but I don’t fully agree.",
                        "You hit the nail on the head with this one!",
                        "Yes, I couldn’t agree more!",
                        "This is exactly how I feel too!",
                        "Absolutely, I’m with you on this!",
                        "You’re right on target with that!",
                        "I agree 100%, you made a great point!",
                        "I’m in total agreement with you!",
                        "That’s a solid point, I’m with you!",
                        "Couldn’t have said it better myself, I agree!",
                        "I’m on board with what you’re saying!",
                        "I get your point, but I’m not sure I agree.",
                        "I can see where you’re coming from, but I disagree.",
                        "You’ve got a valid point, but I see it differently.",
                        "I understand your perspective, but I have a different view.",
                        "You make a good case, but I’m not convinced.",
                        "That’s an interesting thought, but I don’t fully agree.",
                        "I see what you mean, but I have a different opinion.",
                        "I respect your view, but I disagree on this one.",
                        "You’ve got a point, but I have to disagree.",
                        "I hear you, but I’m not sure I’m on the same page.",
                        "Well said! I completely agree with you.",
                        "I couldn’t agree with you more!",
                        "You’re absolutely right, great point!",
                        "I’m in full agreement with what you’ve said.",
                        "Yes, I totally see where you’re coming from!",
                        "You’re exactly right, I feel the same way.",
                        "I agree with you 100%, spot on!",
                        "I’m with you all the way on this.",
                        "You’ve expressed exactly what I was thinking.",
                        "I’m on the same wavelength as you, well said!",
                        "That’s a valid point, but I have to disagree.",
                        "I see your logic, but I have a different perspective.",
                        "I get what you’re saying, but I have a different opinion.",
                        "I see where you’re coming from, but I have to disagree.",
                        "That’s an interesting take, but I don’t fully agree.",
                        "I understand your reasoning, but I see it differently.",
                        "You’ve made a good point, but I disagree.",
                        "I respect your thoughts, but I have to differ.",
                        "I hear what you’re saying, but I see it differently.",
                        "I get your perspective, but I’m not on the same page.",
                        "Exactly, I was just thinking the same thing!",
                        "Yes, I totally agree with you.",
                        "That’s exactly how I see it too.",
                        "I’m in complete agreement with what you’ve said.",
                        "You’ve nailed it, I couldn’t agree more!",
                        "I’m on board with everything you’ve said.",
                        "You’re spot on, I completely agree!",
                        "Yes, I agree with you entirely!",
                        "I’m with you, you’ve got it right!",
                        "Absolutely, I’m in full agreement!",
                        "That’s a valid point, but I have a different view.",
                        "I see where you’re coming from, but I disagree.",
                        "You’ve got a good point, but I see it differently.",
                        "I get what you’re saying, but I don’t fully agree.",
                        "I understand your perspective, but I have a different opinion.",
                        "You make a strong case, but I have to disagree.",
                        "I see your reasoning, but I’m not convinced.",
                        "I hear what you’re saying, but I see it differently.",
                        "I respect your view, but I disagree on this one.",
                        "I get your point, but I’m not sure I’m with you.",
                        "You’re absolutely right, I agree completely.",
                        "I couldn’t agree more, you’re spot on.",
                        "Yes, that’s exactly what I was thinking.",
                        "You’ve hit the nail on the head, I agree!",
                        "I’m in full agreement with you.",
                        "That’s exactly how I feel too, well said!",
                        "You’ve expressed my thoughts perfectly, I agree.",
                        "I’m on the same page as you, no doubt!",
                        "You’re right on the money, I agree 100%!",
                        "I completely agree, you’re spot on.",
                        "I’m with you on this, you’ve got it right!"
                    ]


                    human_like_delay(min_delay=2,max_delay=5)
                    
                    comment = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[data-testid="reply"]')))
                    comment.click()
                    human_like_delay(min_delay=3,max_delay=5)

                    comment = random.choice(comments)
                    try:
                        text_input =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'br[data-text="true"]')))
                    except Exception as e:
                        text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-text="true"]')))
                        
                    actions = ActionChains(driver)
                    actions.move_to_element(text_input)
                    actions.click()
                    # actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE)
                    actions.send_keys(comment)
                    actions.send_keys(" ")
                    actions.perform()


                    human_like_delay(min_delay=3,max_delay=5)

                    tweet_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="tweetButton"]')))
                    tweet_button.click()
                    human_like_delay(min_delay=3,max_delay=7)

                    try:
                        cross_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[aria-label="Close"]')))
                        cross_btn.click()
                    except:
                        pass
                except:
                    pass
        except:
            pass
            
# ===============================================================================================
        

        try:
            try:
                text_input =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'br[data-text="true"]')))
            except Exception as e:
                text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-text="true"]')))
                
            
                
            print("===================================================")   
            print("Tesxt Input = ",text_input)
            print("===================================================")
            
            if(text_input):
                human_like_delay()

                actions = ActionChains(driver)
                actions.move_to_element(text_input)
                actions.click()
                actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE)
                actions.send_keys("Hello Everyone")
                actions.perform()

                human_like_delay(min_delay=0.5, max_delay=2)
                        
                post_tweet = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')))
                post_tweet.click()

                human_like_delay(min_delay=3,max_delay=7)
                try:
                    driver.get("https://x.com/logout")
                    
                    human_like_delay()
                    # logout_button.click()
                    confirmation_dialog_css = "div[data-testid='confirmationSheetDialog']"
                    confirmation_button_css = "button[data-testid='confirmationSheetConfirm']"
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, confirmation_dialog_css)))
                    confirmation_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, confirmation_button_css)))
                    human_like_delay()
                    confirmation_button.click()
                    WebDriverWait(driver, timeout=100).until(EC.url_changes(driver.current_url))
                except:
                    pass
        except:
            pass
            

        return True,username
    except Exception as e:
        print('Last Exception')
        return False,'_'