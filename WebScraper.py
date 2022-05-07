import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://losangeles.craigslist.org/search/cta"

posts = []

for n in range(0, 5000, 120):
    params = {
        's':n
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print('API call failed')
        break

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)








