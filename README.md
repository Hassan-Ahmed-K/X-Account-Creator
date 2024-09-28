# X Account Creator Bot with Email Creation and Proxy Support

## Overview

The **X Account Creator Bot** is an automated solution designed to streamline the creation of X (formerly Twitter) accounts using either **Hotmail** or **Rambler** email services. This bot automates both the email registration and X account creation processes, and even handles temporary phone number verification services for Rambler email accounts. The bot is equipped with a user-friendly GUI built using **Tkinter**, offering flexibility through various customization options, including proxy usage and country selection for temporary phone numbers.

## Key Features

### 1. Automated Email Creation
- **Hotmail Account Creation:** Automates the creation of Hotmail email accounts, managing everything from form-filling to CAPTCHA handling and account confirmation.
- **Rambler Account Creation:** Creates Rambler email accounts and integrates with a temporary phone number service for verification during the registration process.

### 2. Automated X (Twitter) Account Creation
- The bot can create X accounts using newly created Hotmail or Rambler emails, handling all aspects of the sign-up process, including username and password entry, as well as email verification.

### 3. Temporary Phone Number Integration
- **Rambler Email Verification:** Supports the use of temporary phone numbers for account verification. Users can select their preferred country for the phone number from a dropdown menu, ensuring seamless account creation across different regions.

### 4. Proxy Support
- A **proxy toggle feature** allows users to enable or disable proxy usage, reducing the risk of IP bans and avoiding regional restrictions.
- Users can configure the proxy directly from the GUI, and the bot will route all network traffic through the specified proxy.

## GUI Design

The GUI, built with **Tkinter**, is intuitive and provides easy access to all functionalities. The main interface includes the following options:

### Radio Buttons for Email and Account Creation:
- **Only Hotmail Email:** Automates only the creation of Hotmail email accounts.
- **Twitter Account with Hotmail:** Creates both a Hotmail email account and an X account using that email.
- **Only Rambler Email:** Automates the creation of Rambler email accounts, including phone verification using a temporary number.
- **Twitter Account with Rambler Email:** Creates both a Rambler email account and an X account, with phone verification for the email.

### Proxy Option:
- A **proxy toggle** button to enable/disable proxy usage during account creation.
- A **country dropdown** for selecting the region of the temporary number, allowing the bot to adapt to country-specific verification requirements.

## Workflow

1. **Account Creation Process:**
   - Based on the selected radio button, the bot creates either email accounts (Hotmail or Rambler), X accounts, or both. For Rambler email creation, the bot fetches a temporary phone number for verification.

2. **Proxy Support:**
   - If the proxy feature is enabled, all actions are routed through the selected proxy to safeguard the user's IP address and prevent account blocks.

3. **Country Selection for Temporary Numbers:**
   - Users can select their preferred country for temporary phone numbers, ensuring region-appropriate verification for Rambler email accounts.

## Technology Stack

- **Python**: The core programming language used for automation and scripting.
- **Tkinter**: Used to create the graphical user interface (GUI).
- **Selenium**: Handles browser automation for Hotmail, Rambler, and X account creation.
- **Proxy Support**: Ensures the bot works in restricted regions or prevents IP bans.
- **Temporary Phone Number API**: Integrated to provide phone numbers for Rambler email verification.

## Installation

To use this bot, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/X-Account-Creator-Bot.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

- Open the application and select the desired option from the radio buttons:
  - **Only Hotmail Email**
  - **Twitter Account with Hotmail**
  - **Only Rambler Email**
  - **Twitter Account with Rambler Email**

- If necessary, toggle proxy usage and select a country for temporary numbers.
- Start the account creation process, and the bot will handle everything from creating emails to verifying X accounts.
