import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.account_generator_bot import hotmail_account_creator
from src.x_account_generator import x_account_generator
import pandas as pd
import os
import threading
from src.humen_behaviour_function import random_date_generator,generate_username,generate_password,generate_email
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_proxy_from_webshare():
    try:
        response = requests.get(
            "https://ipv4.webshare.io/",
            proxies={
                "http": "http://p.webshare.io:9999/",
                "https": "http://p.webshare.io:9999/"
            }
        )
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text.strip() +":9999"
    except requests.RequestException:
        return None

def get_proxy_from_file(proxy_file_path):
    try:
        with open(proxy_file_path, 'r') as file:
            proxies = file.readlines()
        selected_proxy = random.choice(proxies).strip().split(":")[:2]
        return ":".join(selected_proxy)
    except (FileNotFoundError, IndexError):
        return None

stop_event = threading.Event()

def show_status_popup():
    """Create and return a popup window to display progress status."""
    popup = tk.Toplevel(root)
    popup.title("Status")
    popup.geometry("300x100")
    popup.configure(bg="#f0f0f0")
    
    # Set a label for displaying progress
    status_label = ttk.Label(popup, text="Progress...", style="TLabel")
    status_label.pack(expand=True, padx=10, pady=10)

    # Add a button to close the popup
    close_button = ttk.Button(popup, text="Close", command=popup.destroy, style="Stop.TButton")
    close_button.pack(pady=10)
    
    return popup, status_label

def run_function():
    num_accounts = num_accounts_var.get()
    account_type = account_var.get()
    proxy_flag = proxy_flag_var.get()

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

    proxy = get_proxy_from_file(proxy_file_path)

    if proxy is None:
        raise Exception("No valid proxy found.")

    if(proxy_flag == "on"):
        chrome_options.add_argument(f'--proxy-server={proxy}')



   


    if not num_accounts.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid number of accounts.")
        return

    num_accounts = int(num_accounts)
    if account_type == "none":
        messagebox.showerror("Input Error", "Please select an account type.")
        return

    # Create and show the status popup
    popup, status_label = show_status_popup()

    if account_type == "email":
        try:
            no_accounts = 0
            status_label.config(text=f"0 of {num_accounts} Email generated")
            root.update_idletasks()
            # accounts = []
            

            while no_accounts < num_accounts:
                print(stop_event.is_set())
                if stop_event.is_set():
                    break

                # proxy_file_path = './assets/proxyscrape_premium_http_proxies.txt'
        
                # proxy = get_proxy_from_file(proxy_file_path)

                # if proxy is None:
                #     raise Exception("No valid proxy found.")

                first_name,last_name,_ = generate_username()
                password = generate_password()
                username = generate_email()
                month,day,year,year_index = random_date_generator()
                email =  username + "@hotmail.com"

                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
                driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

                status = hotmail_account_creator(driver,first_name,last_name,username,password,month,day,year)
                driver.quit()
                if(status):
                    no_accounts += 1 
                    status_label.config(text=f"{no_accounts} of {num_accounts} accounts generated")
                    root.update_idletasks()
                    account_detail = [[email, password]]

                    # Check if the CSV file exists and is not empty
                    if os.path.exists("./assets/hotmail_account.csv") and os.path.getsize("./assets/hotmail_account.csv") > 0:
                        try:
                            # Read the existing CSV file
                            df = pd.read_csv("./assets/hotmail_account.csv")
                            # Create a DataFrame for the new account details
                            new_account = pd.DataFrame(account_detail, columns=["Email", "Email Password"])
                            # Concatenate the existing DataFrame with the new account details
                            df = pd.concat([df, new_account], ignore_index=True)
                        except pd.errors.EmptyDataError:
                            # Handle case where CSV file is empty
                            df = pd.DataFrame(account_detail, columns=["Email", "Email Password"])
                    else:
                        # Handle case where CSV file does not exist or is empty
                        df = pd.DataFrame(account_detail, columns=["Email", "Email Password"])

                    # Remove duplicates based on the "Email" column
                    df = df.drop_duplicates(subset=["Email"], keep="first")

                    # Save the updated DataFrame back to the CSV file
                    df.to_csv("./assets/hotmail_account.csv", index=False)
                else:
                    print("Account Creation Failed")

            popup.destroy()
            messagebox.showinfo("Status", f"{no_accounts} Email (Hotmail) accounts generated")
            
        except Exception as e :
            pass

    elif account_type == "twitter":
        try:
            no_accounts = 0
            status_label.config(text=f"0 of {num_accounts} accounts generated")
            root.update_idletasks()
            # accounts = []
            

            while no_accounts < num_accounts:
                if stop_event.is_set():
                    break

                # proxy_file_path = './assets/proxyscrape_premium_http_proxies.txt'
                # proxy = get_proxy_from_webshare()

                # if proxy is None:
                # proxy = get_proxy_from_file(proxy_file_path)

                # if proxy is None:
                #     raise Exception("No valid proxy found.")
                
                first_name,last_name,_ = generate_username()
                username = generate_email() 
                password = generate_password()
                month,day,year,year_index = random_date_generator()
                email =username + "@hotmail.com"

                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
                driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

                status = hotmail_account_creator(driver,first_name,last_name,username,password,month,day,year)
                if(status):
                    status,username =  x_account_generator(driver,username,email,password,month,day,year_index)
                    driver.quit()
                    if(status):
                        try:
                            # df = pd.read_csv("./assets/accounts.csv")
                            no_accounts += 1
                            status_label.config(text=f"{no_accounts} of {num_accounts} accounts generated")
                            root.update_idletasks()
                            account_detail = [[username, password, email, password, ""]]

                            if os.path.exists("./assets/accounts.csv") and os.path.getsize("./assets/accounts.csv") > 0:
                                try:
                                    df = pd.read_csv("./assets/accounts.csv")
                                    account = pd.DataFrame(account_detail, columns=["Username", "TwitterPassword", "Email", "Email Password", "2FA Token"])
                                    df = pd.concat([df, account], ignore_index=True)
                                except pd.errors.EmptyDataError:
                                    df = pd.DataFrame(account_detail, columns=["Username", "TwitterPassword", "Email", "Email Password", "2FA Token"])
                            else:
                                df = pd.DataFrame(account_detail, columns=["Username", "TwitterPassword", "Email", "Email Password", "2FA Token"])

                            df = df.drop_duplicates(subset=["Email"], keep="first")
                            df.to_csv("./assets/accounts.csv", index=False)
                        except Exception as e:
                            print(e)
            
            popup.destroy()
            messagebox.showinfo("Status", f"{no_accounts} accounts generated")
            
        except:
            print(e)

    driver.quit()

def run_function_in_thread():
    stop_event.clear()
    threading.Thread(target=run_function).start()

def stop_function():
    stop_event.set() 
    messagebox.showinfo("Function Status", "Function stopped After this Iteration")


root = tk.Tk()
root.title("DEX-Bot")
root.configure(bg="#f0f0f0")
# root.geometry("600x800")

# Set window icon
icon_path = r"./assets/twitter_x.ico"
img = Image.open(icon_path)
tk_img = ImageTk.PhotoImage(img)
root.wm_iconphoto(True, tk_img)

# Header bar
header_bar = tk.Frame(root, bg="#F0F0F0")
header_bar.grid(row=0, column=0, columnspan=3, sticky='ew')

# Twitter icon in header
twitter_icon_image = Image.open("./assets/Twitter X Icon PNG.jpeg")
twitter_icon_image = twitter_icon_image.resize((60, 50))  # Resize the image if needed
twitter_icon = ImageTk.PhotoImage(twitter_icon_image)
twitter_icon_label = tk.Label(header_bar, image=twitter_icon, bg="#f0f0f0")
twitter_icon_label.pack(side="left")

# Create a style for the widgets
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 10,"bold"))
style.configure("TButton", background="#007BFF", foreground="white", font=("Arial", 12, "bold"))
style.configure("TEntry", padding=(5, 2), foreground="black")
style.configure("Header.TLabel", font=("Arial", 12, "bold"))
style.configure("Info.TLabel", font=("Arial", 10, "bold"))
style.configure("Custom.TCheckbutton", foreground="black", background="#f0f0f0", font=("Arial", 10, "bold"))
style.configure("NameEntry.TEntry", padding=(5, 5), foreground="black", background="white")
style.configure("Start.TButton", foreground="white", background="#4CAF50", font=('Arial', 12, 'bold'))
style.map("Start.TButton", background=[("active", "#4CAF50")])
style.configure("Stop.TButton", foreground="white", background="#FF5722", font=('Arial', 12, 'bold'))
style.map("Stop.TButton", background=[("active", "#FF5722")])
style.configure("Tab.TFrame", background="#f0f0f0")
style.configure("TRadiobutton", background="#f0f0f0", foreground="black", font=("Arial", 10))
style.configure('TNotebook', background="#f0f0f0", borderwidth=2, relief="solid", height=0, width=0)



# Frame to hold checkboxes
checkbox_frame = ttk.Frame(root, style='TFrame')
checkbox_frame.grid(row=1, column=0, sticky='w', padx=20, pady=10)

num_accounts_label = ttk.Label(checkbox_frame, text="Select Type Of The Account:", style="TLabel")
num_accounts_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Email and Twitter radio buttons
account_var = tk.StringVar(value="twitter")

email_radio = ttk.Radiobutton(checkbox_frame, text="Only Email (Hotmail)", variable=account_var, value="email", style="Custom.TRadiobutton")
email_radio.grid(row=1, column=0, sticky='w', padx=5, pady=5)

twitter_radio = ttk.Radiobutton(checkbox_frame, text="Twitter (Email With Twitter)", variable=account_var, value="twitter", style="Custom.TRadiobutton")
twitter_radio.grid(row=1, column=1, sticky='w', padx=5, pady=5)

# Frame to hold input widgets
input_frame = ttk.Frame(root, style='TFrame')
input_frame.grid(row=2, column=0, sticky='w', padx=20, pady=10)
# Number of accounts input
num_accounts_var = tk.StringVar()
num_accounts_label = ttk.Label(input_frame, text="Number of Accounts:", style="TLabel")
num_accounts_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

num_accounts_entry = ttk.Entry(input_frame, textvariable=num_accounts_var, style="NameEntry.TEntry")
num_accounts_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')


proxy_frame = ttk.Frame(root, style='TFrame')
proxy_frame.grid(row=3, column=0, sticky='w', padx=20, pady=10)

proxy_label = ttk.Label(proxy_frame, text="Select Proxy On or Off", style="TLabel")
proxy_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

proxy_flag_var = tk.StringVar(value="off")

onn_radio = ttk.Radiobutton(proxy_frame, text="On", variable=proxy_flag_var, value="on" , style="Custom.TRadiobutton")
onn_radio.grid(row=1, column=0, sticky='w', padx=0, pady=5)

off_radio = ttk.Radiobutton(proxy_frame, text="Off", variable=proxy_flag_var, value= "off" , style="Custom.TRadiobutton")
off_radio.grid(row=1, column=1, sticky='w', padx=0, pady=5)

# Frame to hold buttons
button_frame = ttk.Frame(root, style='TFrame')
button_frame.grid(row=4, column=0, sticky='w', padx=20, pady=10)

# Start and Stop buttons
start_button = ttk.Button(button_frame, text="Start", style="Start.TButton", command=run_function_in_thread)
start_button.grid(row=0, column=0, padx=10, pady=20, sticky='w')

stop_button = ttk.Button(button_frame, text="Stop", style="Stop.TButton", command=stop_function)
stop_button.grid(row=0, column=1, padx=10, pady=20, sticky='w')


# Run the application
root.mainloop()
