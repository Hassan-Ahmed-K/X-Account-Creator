import requests





def sms_activation_balance(api_key):

    
    # api_key = "45b6f4c598eef3ca1c26d303cb7e3334"
    # Print the API keys to verify (optional)
    print(f"API Key: {api_key}")

    base_url = "https://sms-activation-service.com/stubs/handler_api"
    action = "getBalance"
    lang = "en"  # You can change this to "ru" if needed

    # Construct the full URL with parameters
    url = f"{base_url}?api_key={api_key}&action={action}&lang={lang}"

    # Make the GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        balance = response.text
        if(balance =="0.00"):
            return False
        else:
           return balance
    else:
        return False


def get_sms_activation_service_cost(api_key,country_code):
    base_url = "https://sms-activation-service.com/stubs/handler_api"
    action = "getServicesAndCost"
    country = country_code  
    operator = "any" 
    service = "tc" 
    lang = "en"  

    url = f"{base_url}?api_key={api_key}&action={action}&country={country}&operator={operator}&service={service}&lang={lang}"

    response = requests.get(url)
    if response.status_code == 200:
        service_cost_info = response.text
        # print(f"Service and Cost Information: {service_cost_info}")
        return service_cost_info
    else:
        # print(f"Failed to retrieve service cost information. Status code: {response.status_code}")
        return False

def get_sms_activation_number(api_key,country_code):
    base_url = "https://sms-activation-service.com/stubs/handler_api"
    action = "getNumber"
    country = country_code
    # country = 0
    operator = "any"
    service = "tc"
    lang = "en" 

    # Construct the full URL with parameters
    url = f"{base_url}?api_key={api_key}&action={action}&country={country}&operator={operator}&service={service}&lang={lang}"

    # Make the GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        number_id = response.text.split(":")
        order_id = number_id[1]
        number = number_id[2]
        return number, order_id
    else:
        return False

def get_sms_activation_message(api_key,order_id):

    # Define the base URL and parameters
    base_url = "https://sms-activation-service.com/stubs/handler_api"
    action = "getStatus"
    lang = "en"  # Language, "en" for English

    # Construct the full URL with parameters
    url = f"{base_url}?api_key={api_key}&action={action}&id={order_id}&lang={lang}"
    response = requests.get(url)

    if response.status_code == 200:
        status_response = response.text
        # print(f"Status Update Response: {status_response}")
        return status_response
    else:
        return False
    


def deleat_sms_activation_number(api_key,order_id):
        # Define the base URL and parameters
    base_url = "https://sms-activation-service.com/stubs/handler_api"
    id = order_id  # Replace with the actual order ID
    status = 6  
    lang = 'en'  # Language set to English

    # Construct the full URL with parameters
    url = f"{base_url}?api_key={api_key}&action=setStatus&id={id}&status={status}&lang={lang}"
    response = requests.get(url)

    if response.status_code == 200:
        status_response = response.text
        # print(f"Status Update Response: {status_response}")
        return status_response
    else:
        return False
    

