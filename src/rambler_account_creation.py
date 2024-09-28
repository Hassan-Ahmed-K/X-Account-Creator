from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
from src.humen_behaviour_function import human_like_delay,type_like_human,generate_email,generate_password
from src.sms_activation_service import *
import time
import random
import pandas as pd
from dotenv import load_dotenv
# import undetected_chromedriver as uc


def rambler_account_creation(driver,username,password,selected_country):
    try:
        # # Get current working directory

        country_info = {
                        "Netherlands": {"Country Code": 48, "Dial Code": 31},
                        "Russia": {"Country Code": 0, "Dial Code": 7},
                        "Germany": {"Country Code": 43, "Dial Code": 49},
                        "Moldova": {"Country Code": 85, "Dial Code": 373},
                        "Armenia": {"Country Code": 148, "Dial Code": 374},
                        "Israel": {"Country Code": 13, "Dial Code": 972},
                        "Azerbaijan": {"Country Code": 35, "Dial Code": 994},
                        "Estonia": {"Country Code": 34, "Dial Code": 372},
                        "USA": {"Country Code": 187, "Dial Code": 1},
                        "Uzbekistan": {"Country Code": 40, "Dial Code": 998},
                        "Georgia": {"Country Code": 128, "Dial Code": 995},
                        }
        load_dotenv()
        api_key = os.getenv('SMS_ACTIVATION_API_KEY')


        wait = WebDriverWait(driver=driver,timeout=30)


        driver.get("https://mail.rambler.ru")
        time.sleep(5)
       
        balance = sms_activation_balance(api_key)
        country_dial_code = country_info[selected_country]["Dial Code"]
        country_code = country_info[selected_country]["Country Code"]
        if(balance):
            service_and_cost = get_sms_activation_service_cost(api_key,country_code)
            if(service_and_cost):
                phone_number_and_order_id = get_sms_activation_number(api_key,country_code)
                if(phone_number_and_order_id):
                    phone_number, order_id = get_sms_activation_number(api_key,country_code)
                    print(phone_number)
                    phone_number = phone_number[len(str(country_dial_code)):]
                else:
                    print("There is phone Number Available Right Now")
                    return False

            else:
                print("There is no service available right now")
                return False
        else:
            print("Your Balance is Empty")
            return False
        

        
        print("email =",username )
        print("password =",password)
        print("balance =",balance)
        print("service_and_cost =",service_and_cost)
        print("country_dial_code =",country_dial_code)
        print("phone_number =",phone_number)
        print("order_id =",order_id)
        # input("Press Enter")
        print("Title = ",driver.title)
        
        # driver.switch_to.window(driver.window_handles[0])
        iframe = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"iframe")))
        
        driver.switch_to.frame(iframe)

        signup_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[data-cerber-id="login_form::main::register_link"]')))

        signup_btn.click()
        # driver.switch_to.window(driver.window_handles[0])
        
        # time.sleep(30)
        human_like_delay(min_delay=5,max_delay=7)
        username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#login')))
        type_like_human(username_input,username)
        human_like_delay()
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#newPassword')))
        type_like_human(password_input,password)
        human_like_delay()
        confirm_password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input#confirmPassword')))
        type_like_human(confirm_password_input,password)
        human_like_delay()
        country_code = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input.rui-Select-darkPlaceholder')))[-1]
        print(country_code.get_attribute('value'))
        # type_like_human(country_code,str(+1))
        # country_code.send_keys(+1)
        country_code.click()

        country_code_container = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.rui-Select-dropdownContainer.rui-RelativeOverlay-container')))[-1]
        time.sleep(1)
        country_code_drop_down = country_code_container.find_element(By.CSS_SELECTOR,"div.rui-RelativeOverlay-content")
        countries = country_code_drop_down.find_elements(By.CSS_SELECTOR, "*")
        for country in countries:
            try:
                dial_code = country.text.split("+")[1]
                if(dial_code ==str(country_dial_code)):
                    print(country.text)
                    country.click()
                    print("-" * 40)
                    break
            except:
                pass

        human_like_delay()

        phone_no = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#Rambler\\:\\:Id\\:\\:register_user_by_phone\\.phone')))
        type_like_human(phone_no,str(phone_number))

        login_btn = driver.find_element(By.XPATH, "//button[.//span[text()='Получить код']]")
        login_btn.click()

        try:
            h_captcha = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe')))
            captcha_solver_status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.captcha-solver'))).text
            i=0

            while((captcha_solver_status != "Captcha solved!")):
                if(i==30):
                    break
                captcha_solver_status = driver.find_element(By.CSS_SELECTOR,'div.captcha-solver').text
                time.sleep(3)
                i+=1

            login_btn = driver.find_element(By.XPATH, "//button[.//span[text()='Получить код']]")
            login_btn.click()
            # time.sleep(10)
                
        except:
            print("Pass the H_Captcha")
        time.sleep(10)
        
        msg_text = get_sms_activation_message(api_key,order_id=order_id)
        i=0
        while(msg_text == "STATUS_WAIT_CODE"):
            print(msg_text)
            time.sleep(10)
            msg_text = get_sms_activation_message(api_key,order_id=order_id)
            i+=1
            if(msg_text == "STATUS_CANCEL"):
                driver.quit()
                return False
            
            if(i== 10):
                resend_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.styles_mailReg__LtHOf')))
                print(resend_code.text)
                resend_code.click()
            if(i== 11):
                return False


        if(msg_text):
            print(msg_text)
            print(msg_text.split(":")[1])
            
            # driver.switch_to.window(driver.window_handles[1])
            otp_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[autocomplete="one-time-code"]')))
            type_like_human(otp_input,str(msg_text.split(":")[1]))
            login_btn = driver.find_element(By.XPATH, "//button[.//span[text()='Далее']]")
            login_btn.click()

        try:
            wrong_code = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'div.rui-FieldStatus-message')))[-1]
            print(wrong_code.text)
            if(wrong_code.text == "Неверный код, запросите код еще раз"):
                resend_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.styles_mailReg__LtHOf')))
                print(resend_code.text)
                resend_code.click()
                time.sleep(10)
                msg_text = get_sms_activation_message(api_key,order_id=order_id)
                while(msg_text == "STATUS_WAIT_CODE"):
                    print(msg_text)
                    time.sleep(10)
                    msg_text = get_sms_activation_message(api_key,order_id=order_id)
                    i+=1
                    if(msg_text == "STATUS_CANCEL"):
                        driver.quit()
                        return False
            
                    if(i== 10):
                        resend_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.styles_mailReg__LtHOf')))
                        print(resend_code.text)
                        resend_code.click()
                    if(i== 11):
                        return False

                if(msg_text):
                    print(msg_text.split(":")[1])
                
                    # driver.switch_to.window(driver.window_handles[1])
                    otp_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[autocomplete="one-time-code"]')))
                    type_like_human(otp_input,str(msg_text.split(":")[1]))
                    login_btn = driver.find_element(By.XPATH, "//button[.//span[text()='Далее']]")
                    login_btn.click()
        except:
            print("Otp Code is Correct")
        time.sleep(10)
        
        try:
            login_btn = driver.find_element(By.XPATH, "//button[.//span[text()='Далее']]")
            login_btn.click()
        except:
            pass

        time.sleep(10)
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"footer")))
        signup_btn = footer.find_element(By.CSS_SELECTOR,'a[data-cerber-id="registration_form::step_2::add_later"]')
        signup_btn.click()
       
        try:
            WebDriverWait(driver=driver,timeout=60).until(EC.url_changes("https://mail.rambler.ru/folder/INBOX"))
            popup_close_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button.styles-close-5S")))
            popup_close_btn.click()
        except:
            pass
        try:
            deleat_sms_activation_number(api_key,order_id)
        except:
            pass
        return True
    except Exception as e:
        print(e)
        return False

