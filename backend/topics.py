from bs4 import BeautifulSoup
import requests
import re
import json

URL_1 = "http://www.ebook3000.com/"
URL_2 = "http://www.ebook3000.com/Magazine/Military/index.html"

def get_soup(url):
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 \
        (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    
    req = requests.get(url, headers)
    return BeautifulSoup(req.content, 'html.parser')

def get_categories(topics, soup):
    div = soup.find(text=re.compile('Categories')).parent.parent.parent
    for category in div.find_all("a"):
        url = category.get("href")
        name = category.find(text=True)
        if (name not in topics):
            topics[name] = url

def get_topics(cache):
    topics = {"All":"/"}
    
    if cache.get("topics") is not None:
        return json.loads(cache.get("topics"))
    
    soup = get_soup(URL_1)
    get_categories(topics, soup)
    
    soup = get_soup(URL_2)
    get_categories(topics, soup)

    cache.set("topics", json.dumps(topics), 0)

    return topics