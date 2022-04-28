from bs4 import BeautifulSoup
import requests

url = "https://www.sahibinden.com/satilik/istanbul"
page = requests.get(url)
print(page)


