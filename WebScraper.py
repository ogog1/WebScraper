import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}


url = "https://losangeles.craigslist.org/search/cta"

posts = []

for n in range(0, 5000, 120):
    params = {
        's':n
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        print('API call failed')
        break

soup = BeautifulSoup(response.content, 'html.parser')

if soup.find('pre', {'id':'moon'}:
    break








