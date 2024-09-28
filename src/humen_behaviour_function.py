import time
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



def human_like_delay(min_delay=1, max_delay=5):
    time.sleep(random.uniform(min_delay, max_delay))
    
def scroll(driver,element,down=True):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    if(down):
        actions.scroll_by_amount(0, 500)
    else:
        actions.scroll_by_amount(500,0)
    actions.perform()
    human_like_delay()
    

def type_like_human(element, text, min_delay=0.05, max_delay=0.3):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))
        
def random_date_generator():
    month = random.randint(1,12)
    day = random.randint(2,29)
    year = random.randint(1995,2004)
    year_index = random.randint(22,29)
    return month,day,year,year_index

def generate_human_name():
    first_names = [
        'John', 'Emma', 'Michael', 'Sophia', 'James', 
        'Olivia', 'Robert', 'Isabella', 'William', 'Mia', 
        'David', 'Charlotte', 'Richard', 'Amelia', 'Joseph', 
        'Benjamin', 'Evelyn', 'Daniel', 'Avery', 'Matthew', 
        'Henry', 'Eleanor', 'Samuel', 'Ella', 'Christopher', 
        'Aiden', 'Grace', 'Joshua', 'Hannah', 'Andrew',
        'Elizabeth', 'Alexander', 'Samantha', 'Logan', 'Victoria', 
        'Ryan', 'Lily', 'Liam', 'Aria', 'Noah',
        'Scarlett', 'Lucas', 'Aurora', 'Mason', 'Riley',
        'Jackson', 'Hazel', 'Elijah', 'Zoe', 'Caleb',
        'Brooklyn', 'Isaac', 'Lucy', 'Connor', 'Ruby',
        'Ethan', 'Stella', 'Jayden', 'Bella', 'Nathan',
        'Violet', 'Gabriel', 'Penelope', 'Aaron', 'Paisley',
        'Christian', 'Aurora', 'Jonathan', 'Savannah', 'Dylan',
        'Nora', 'Zachary', 'Luna', 'Isaiah', 'Addison'
    ]
    
    last_names = [
        'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 
        'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 
        'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 
        'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 
        'Lee', 'Perez', 'Thompson', 'White', 'Harris', 
        'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 
        'Walker', 'Young', 'Allen', 'King', 'Wright', 
        'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 
        'Green', 'Adams', 'Nelson', 'Baker', 'Hall',
        'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts',
        'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz',
        'Parker', 'Cruz', 'Edwards', 'Collins', 'Reed',
        'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook',
        'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed',
        'Bailey', 'Bell', 'Gonzales', 'Fisher', 'Kelley'
    ]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    number = random.randint(1, 99)
    
    username = f"{first_name} {last_name}"
    return first_name, last_name, username

def generate_email(length=9):

    characters = string.ascii_letters + string.digits
    username = random.choice(string.ascii_letters) + ''.join(random.choice(characters) for _ in range(length))
    return username


def generate_password(length=15):
    if length < 8 or length > 32:
        raise ValueError("Password length must be between 8 and 32 characters.")
    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)

    punctuation = "!@$%^&*()_-+"
    characters = string.ascii_letters + string.digits + punctuation

    remaining_length = length - 3 
    remaining_characters = ''.join(random.choice(characters) for _ in range(remaining_length))
    password = list(uppercase_letter + lowercase_letter + digit + remaining_characters)
    random.shuffle(password)
    return ''.join(password)



# for _ in range(10):
#     print(email())