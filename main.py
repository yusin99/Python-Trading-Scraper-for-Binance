from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# Demo user
url = 'https://www.binance.com/en/futures-activity/leaderboard?type=myProfile&tradeType=PERPETUAL&encryptedUid=696A4BE75E87B58631D36DE65555568C'

browser = webdriver.Chrome('/Users/yusinsedrati/Desktop/Python web scrapper/chromedriver')
browser.get(url)