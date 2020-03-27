import smtplib
import random
import string
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui

#Webdriver setup

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors --noerrdialogs --disable-infobars")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

#SMTP Setup

SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587

with open("gmail address.txt") as myfile:
    GMAIL_USERNAME = "".join(line.rstrip() for line in myfile)
    
with open("gmail password.txt") as myfile:
    GMAIL_PASSWORD = "".join(line.rstrip() for line in myfile)
 
class Emailer:
    def sendmail(self, recipient, subject, content):
         
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Set subject and content

        sender = Emailer()
        with open("coinjar email.txt") as myfile:
            sendTo = "".join(line.rstrip() for line in myfile)   
        emailSubject = "BTCBot started"
        emailContent = "BTCBot started at: " + time.ctime()
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit


while SMTP_PORT == 587:
    print("BTCBot 0.4")
    driver.get("https://secure.coinjar.com/users/sign_in")
    sleep(1)
    
    with open("coinjar email.txt") as myfile:
        coinjar_email = "".join(line.rstrip() for line in myfile)
    with open("coinjar password.txt") as myfile:
        coinjar_password = "".join(line.rstrip() for line in myfile)
        
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/input").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/input").send_keys(coinjar_email)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/input").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/input").send_keys(coinjar_password)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/button").click()
    sleep(1)
    
    
