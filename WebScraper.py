import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

base_url = "https://losangeles.craigslist.org/search/cta"

posts = []

for n in range(0, 5000, 120):
    params = {
        's':n
    }

    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code != 200:
        print('API call failed')
        break

    soup = BeautifulSoup(response.content, 'html.parser')

    if soup.find('pre',{'id':'moon'}):
        break

    search_results = soup.find('ul', {'class':'rows','id':'search-results'})
    listings = search_results.find_all('li', 'result-row')

    post_url = []
    for listing in listings:
        url = listing.a['href']

        response_post = requests.get(url, headers=headers)
        post_soup = BeautifulSoup(response_post.content, 'html.parser')
        post_detail = post_soup.find('div', 'mapAndAttrs')
        model = post_detail.find('span').text

        result_info = listing.div
        post_id = result_info.h3.a['id']

        location = result_info.find('span', 'result-hood').text.\
            replace('(','').\
            replace(')','').strip()

        price = result_info.find('span', 'result-price').text

        posts.append([post_id, model, price, location])
        time.sleep(0.5)

df = pd.DataFrame(posts, columns=['post id', 'car', 'price', 'location'])
df.to_csv('LA cars.csv', index=False)






