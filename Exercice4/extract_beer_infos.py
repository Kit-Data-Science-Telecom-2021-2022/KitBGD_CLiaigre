import requests
from bs4 import BeautifulSoup
import re

def extract_beer_infos(url):
    
    r = requests.get(url)
    content = r.content.decode('utf-8')
    soup = BeautifulSoup(content, "html.parser")
    
    infos = {
        'name': None,
        'note': None,
        'price': None,
        'volume': None,
    }
    h = soup.find('h1')
    infos['name'] = h.text
    div = soup.find('div', attrs={'class': 'stars'})
    infos['note'] = int(div.attrs['data-percent'])
    span = soup.find('span', attrs={'class': 'price'})
    infos['price'] = float(re.search('\d+\D\d+', span.text.replace(',','.')).group(0))
    dd = soup.find('dd', attrs={'class': "small-6 medium-9 columns js-beer-volume"})
    infos['volume'] = int(re.search('\d+', dd.text).group(0))
    return infos