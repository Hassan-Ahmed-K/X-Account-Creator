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
    year = random.randint(1995,2010)
    year_index = random.randint(14,29)
    return month,day,year,year_index

def generate_username():
    adjectives = [
        'quick', 'lazy', 'sleepy', 'noisy', 'hungry', 
        'happy', 'sad', 'angry', 'brave', 'calm', 
        'eager', 'fierce', 'gentle', 'kind', 'proud',
        'clever', 'curious', 'daring', 'determined', 'dynamic',
        'friendly', 'funny', 'graceful', 'hardworking', 'honest',
        'imaginative', 'jovial', 'lively', 'loyal', 'mischievous',
        'patient', 'playful', 'polite', 'resourceful', 'sincere',
        'thoughtful', 'understanding', 'vibrant', 'witty', 'zealous',
        'adventurous', 'ambitious', 'artistic', 'athletic', 'bold',
        'charming', 'confident', 'considerate', 'courageous', 'diligent',
        'enthusiastic', 'faithful', 'fearless', 'generous', 'grateful',
        'helpful', 'hilarious', 'independent', 'inventive', 'joyful',
        'keen', 'meticulous', 'modest', 'observant', 'optimistic',
        'passionate', 'perceptive', 'persistent', 'reliable', 'resilient',
        'sociable', 'spirited', 'spontaneous', 'strategic', 'studious',
        'supportive', 'talented', 'tenacious', 'trustworthy', 'valiant',
        'versatile', 'vivacious', 'wise', 'zany', 'zealous',
        'radiant', 'adaptable', 'affectionate', 'amiable', 'bright'
    ]
    
    nouns = [
    'fox', 'dog', 'cat', 'mouse', 'frog', 
    'lion', 'tiger', 'bear', 'wolf', 'eagle', 
    'shark', 'whale', 'panda', 'koala', 'dolphin',
    'rabbit', 'deer', 'squirrel', 'otter', 'owl',
    'hawk', 'falcon', 'swan', 'peacock', 'penguin',
    'turtle', 'gecko', 'iguana', 'alligator', 'crocodile',
    'bat', 'beaver', 'buffalo', 'camel', 'cheetah',
    'chicken', 'chimpanzee', 'cobra', 'crab', 'crow',
    'dinosaur', 'duck', 'elephant', 'flamingo', 'giraffe',
    'goat', 'gorilla', 'hedgehog', 'hippopotamus', 'horse',
    'jaguar', 'kangaroo', 'lemur', 'leopard', 'lizard',
    'lynx', 'manatee', 'meerkat', 'moose', 'octopus',
    'ostrich', 'otter', 'parrot', 'platypus', 'porcupine',
    'quokka', 'raccoon', 'raven', 'reindeer', 'rhinoceros',
    'seal', 'skunk', 'sloth', 'sparrow', 'squid',
    'starfish', 'stork', 'swan', 'toucan', 'turkey',
    'turtle', 'vulture', 'walrus', 'wombat', 'yak',
    'zebra', 'anteater', 'armadillo', 'bison', 'caribou',
    'chinchilla', 'coyote', 'dingo', 'emu', 'gazelle'
    ]
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(1, 99)
    
    username = f"{adjective}.{noun}.{number}"
    return adjective, noun, username

def generate_email(length=9):

    characters = string.ascii_letters + string.digits
    username = random.choice(string.ascii_letters) + ''.join(random.choice(characters) for _ in range(length))
    return username


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password = password.replace('"','#')
    return password



# for _ in range(10):
#     print(email())