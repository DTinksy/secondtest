import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


url = 'https://zvukipro.com/dendy/751-muzyka-i-zvuki-iz-igry-kontra-na-dendi.html'
headers = {
    'Accept': '*/*',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.732 YaBrowser/23.11.1.732 Yowser/2.5 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text
#print(src)
with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)
