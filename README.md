# Crypto-price-alert

Little passion project I wrote over a weekend to practice my python skills.

# Set Up API Key and Email Credentials
Create a file named Env.py in the project directory and define your API key and Gmail app password:
python
Copy code
# Env.py
class keys:
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'your_coinmarketcap_api_key'
    }
    APP_PASSWORD = 'your_gmail_app_password'
