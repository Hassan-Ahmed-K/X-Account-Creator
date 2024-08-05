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
import pyautogui



current_working_directory = os.getcwd()

chrome_driver_path = os.path.join(current_working_directory, "chromedriver/chromedriver")
capsolver_extension_path = os.path.join(current_working_directory, "Extentions/capsolver_extension")

if not os.path.isfile(chrome_driver_path):
    raise FileNotFoundError(f"Chromedriver not found at {chrome_driver_path}")


if not os.path.isdir(capsolver_extension_path):
    raise FileNotFoundError(f"Capsolver extension directory not found at {capsolver_extension_path}")
if not os.path.isfile(os.path.join(capsolver_extension_path, "manifest.json")):
    raise FileNotFoundError(f"Manifest file not found in capsolver extension directory at {capsolver_extension_path}")


chrome_service = Service(executable_path=chrome_driver_path)
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--load-extension={0}".format(capsolver_extension_path))
# chrome_options.add_argument("--disable-blink-features=WebRTC")
# chrome_options.add_argument("--auto-open-devtools-for-tabs")


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.maximize_window()

first_name,last_name,username = generate_username()
# password = generate_password()
month,day,year = random_date_generator()

email = "wise.crab.80@hotmail.com"
password = r"FN\M8'_~$^Ag"
account_image = r"/home/hassan-ahmed-khan/Dex Shit/X Account Creator/assets/images.jpeg"

wait = WebDriverWait(driver=driver,timeout=30)

# driver.maximize_window()


driver.execute_script(f"window.open('https://x.com', '_blank');")

driver.switch_to.window(driver.window_handles[1])
bottom_popup_cross = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="xMigrationBottomBar"]'))) 
human_like_delay()
bottom_popup_cross.click()
# human_like_delay()

create_btn = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(.,"Create account")]')))
create_btn.click()

first_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[autocomplete="name"]')))
type_like_human(first_name_element,username)

email_switch_button = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Use email instead")]')))
email_switch_button.click()

# email_switch_button.click()
# human_like_delay()

modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[aria-labelledby="modal-header"]')))
location = modal.location
modal_y = location['y']
# 


email_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[autocomplete="email"]')))
size = email_element.size
# search_bar = wait.until(EC.presence_of_element_located((By.NAME, 'q')))

# Ensure the element is visible
if email_element.is_displayed():
    # Get the location of the element relative to the browser window
    element_location = email_element.location
    element_size = email_element.size

    time.sleep(5)

    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")

    # Get the browser window position on the screen
    window_position = driver.get_window_position()
    window_x = window_position['x']
    window_y = window_position['y']

    # Calculate the screen coordinates of the element
    element_x = window_x + element_location['x'] + element_size['width'] / 2
    element_y = window_y + element_location['y'] + element_size['height'] / 2

    print(f"Element location (relative to browser): {element_location}, size: {element_size}")
    print(f"Browser window position: {window_position}")
    print(f"Calculated screen coordinates: ({element_x}, {element_y})")

    # Move to the element location with a duration to see the movement
    pyautogui.moveTo(element_x, element_y +150 , duration=2)  # 2 seconds duration to see the movement
    time.sleep(1)  # Wait for 1 second to see the cursor at the location
    pyautogui.click()

    # Print current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")
else:
    print("Element is not visible.")

type_like_human(email_element,email)
human_like_delay()



birth_month_dropdown = Select(driver.find_element(By.ID, "SELECTOR_1"))
birth_month_dropdown.select_by_index(month) 
human_like_delay()
birth_day_dropdown = Select(driver.find_element(By.ID, "SELECTOR_2"))
birth_day_dropdown.select_by_index(day)
human_like_delay()
birth_year_input = Select(driver.find_element(By.ID, "SELECTOR_3"))
birth_year_input.select_by_value(str(year))
human_like_delay()
next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-testid="ocfSignupNextLink"]')))
next_btn.click()



try:
    arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
    i = 0
    while (i>=60 or arkose_challenge):
        i+=1
        arkose_challenge = driver.find_element(By.CSS_SELECTOR,'iframe#arkoseFrame')

except:
    print("Arkose Challenge Exit")

verification_code = 444555

verification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="verfication_code"]')))

if verification_element.is_displayed():
    # Get the location of the element relative to the browser window
    element_location = verification_element.location
    element_size = verification_element.size

    time.sleep(5)

    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")

    # Get the browser window position on the screen
    window_position = driver.get_window_position()
    window_x = window_position['x']
    window_y = window_position['y']

    # Calculate the screen coordinates of the element
    element_x = window_x + element_location['x'] + element_size['width'] / 2
    element_y = window_y + element_location['y'] + element_size['height'] / 2

    print(f"Element location (relative to browser): {element_location}, size: {element_size}")
    print(f"Browser window position: {window_position}")
    print(f"Calculated screen coordinates: ({element_x}, {element_y})")

    # Move to the element location with a duration to see the movement
    pyautogui.moveTo(element_x, element_y +150 , duration=2)  # 2 seconds duration to see the movement
    time.sleep(1)  # Wait for 1 second to see the cursor at the location
    pyautogui.click()

    # Print current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")
else:
    print("Element is not visible.")

type_like_human(verification_element,str(verification_code))
human_like_delay()
print("Verification Element = ",verification_element)

next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
if next_btn.is_displayed():
    # Get the location of the element relative to the browser window
    element_location = next_btn.location
    element_size = next_btn.size

    time.sleep(5)

    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")

    # Get the browser window position on the screen
    window_position = driver.get_window_position()
    window_x = window_position['x']
    window_y = window_position['y']

    # Calculate the screen coordinates of the element
    element_x = window_x + element_location['x'] + element_size['width'] / 2
    element_y = window_y + element_location['y'] + element_size['height'] / 2

    print(f"Element location (relative to browser): {element_location}, size: {element_size}")
    print(f"Browser window position: {window_position}")
    print(f"Calculated screen coordinates: ({element_x}, {element_y})")

    # Move to the element location with a duration to see the movement
    pyautogui.moveTo(element_x, element_y +150 , duration=2)  # 2 seconds duration to see the movement
    time.sleep(1)  # Wait for 1 second to see the cursor at the location
    pyautogui.click()

    # Print current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")
else:
    print("Element is not visible.")
# next_btn.click()
try:
    arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
    while (arkose_challenge):
        arkose_challenge = driver.find_element((By.CSS_SELECTOR,'iframe#arkoseFrame'))
except:
    pass


verification_element = driver.switch_to.active_element

if verification_element.is_displayed():
    # Get the location of the element relative to the browser window
    element_location = verification_element.location
    element_size = verification_element.size

    time.sleep(5)

    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")

    # Get the browser window position on the screen
    window_position = driver.get_window_position()
    window_x = window_position['x']
    window_y = window_position['y']

    # Calculate the screen coordinates of the element
    element_x = window_x + element_location['x'] + element_size['width'] / 2
    element_y = window_y + element_location['y'] + element_size['height'] / 2

    print(f"Element location (relative to browser): {element_location}, size: {element_size}")
    print(f"Browser window position: {window_position}")
    print(f"Calculated screen coordinates: ({element_x}, {element_y})")

    # Move to the element location with a duration to see the movement
    pyautogui.moveTo(element_x, element_y +150 , duration=2)  # 2 seconds duration to see the movement
    time.sleep(1)  # Wait for 1 second to see the cursor at the location
    pyautogui.click()

    # Print current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")
else:
    print("Element is not visible.")

type_like_human(verification_element,str(verification_code))
human_like_delay()
print("Verification Element = ",verification_element)

next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[role="button"]')))
if next_btn.is_displayed():
    # Get the location of the element relative to the browser window
    element_location = next_btn.location
    element_size = next_btn.size

    time.sleep(5)

    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")

    # Get the browser window position on the screen
    window_position = driver.get_window_position()
    window_x = window_position['x']
    window_y = window_position['y']

    # Calculate the screen coordinates of the element
    element_x = window_x + element_location['x'] + element_size['width'] / 2
    element_y = window_y + element_location['y'] + element_size['height'] / 2

    print(f"Element location (relative to browser): {element_location}, size: {element_size}")
    print(f"Browser window position: {window_position}")
    print(f"Calculated screen coordinates: ({element_x}, {element_y})")

    # Move to the element location with a duration to see the movement
    pyautogui.moveTo(element_x, element_y +150 , duration=2)  # 2 seconds duration to see the movement
    time.sleep(1)  # Wait for 1 second to see the cursor at the location
    pyautogui.click()

    # Print current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")
else:
    print("Element is not visible.")
# next_btn.click()
try:
    arkose_challenge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'iframe#arkoseFrame')))
    while (arkose_challenge):
        arkose_challenge = driver.find_element((By.CSS_SELECTOR,'iframe#arkoseFrame'))
except:
    pass



input("press ENter")

