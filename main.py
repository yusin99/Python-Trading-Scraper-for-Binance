# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import requests
# import time

# # Demo user
# url = 'https://www.binance.com/en/futures-activity/leaderboard?type=myProfile&tradeType=PERPETUAL&encryptedUid=696A4BE75E87B58631D36DE65555568C'
# source = requests.get(url).text

# # Path to the chrome driver
# service = Service("/Users/yusinsedrati/Desktop/Python web scrapper/chromedriver")
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
# driver.get(url)
# driver.find_element('')
# # soup = BeautifulSoup(source, 'lxml')

# # print(soup.prettify())
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

# Demo user
url = 'https://www.binance.com/en/futures-activity/leaderboard?type=myProfile&tradeType=PERPETUAL&encryptedUid=696A4BE75E87B58631D36DE65555568C'

# Configuring driver due to deprecated variable => DeprecationWarning: executable_path has been deprecated, please pass in a Service object
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service("/Users/yusinsedrati/Desktop/Python web scrapper/chromedriver") #Path to the driver (preferably into your project and add it to .gitignore)
driver = webdriver.Chrome(service=service,options=chrome_options)

# Displaying prettified first HTML content in terminal 
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())


# Page actions
driver.get(url)
reject_cookies_button = driver.find_element(By.ID,"onetrust-reject-all-handler")
reject_cookies_button.click()