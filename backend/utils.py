from bs4 import BeautifulSoup
import requests

def get_soup(url):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 \
        (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    
    req = requests.get(url, headers)
    return BeautifulSoup(req.content, 'html.parser')