import requests
import pandas as pd
from Env import keys
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart






def crypto_rates(base_currency = 'USD', assests = 'bitcoin,ethereum,xrp' ):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
    'slug': assests,
    'convert': base_currency    
    }

    headers = keys.headers

    response = requests.get(url, params=parameters, headers=headers)

    data = list(response.json()['data'].keys())

    
    crypto_dict = {}

    for i in data:
        crypto_dict[response.json()['data'][i]['name']] = response.json()['data'][i]['quote'][base_currency]['price']
        
        
    return crypto_dict




def setAlert(subject, body, to_email):

     
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "mohamedamino0316@gmail.com"
    from_password = keys.APP_PASSWORD 


    
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(from_email, from_password)  
        text = message.as_string()  
        server.sendmail(from_email, to_email, text)  
        server.quit()  
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


while True:

    data = crypto_rates()

    crypto_currency = list(data.keys())
    crypto_value = list(data.values())

    message = ""

    for i in range(len(crypto_currency)):
        message += f"The Crypto Currency: {crypto_currency[i]} is valued at {crypto_value[i]} USD\n"

    setAlert("CRYPTO PRICE ALERT", message, "mohamedamino0316@gmail.com")

    sleep(86400)

    
    






