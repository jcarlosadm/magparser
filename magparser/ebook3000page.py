from bs4 import BeautifulSoup
import requests

from magparser.ebook3000item import Ebook3000Item

class Ebook3000Page:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_items_from_page(self, page):
        url = self.base_url % page
        
        headers = requests.utils.default_headers()
        headers.update({ 'User-Agent': 'Mozilla/5.0 \
            (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

        req = requests.get(url, headers)

        soup = BeautifulSoup(req.content, 'html.parser')

        html_items = soup.find_all("div", {'class':'list_box'})

        items = []
        for html_item in html_items:
            items.append(Ebook3000Item(html_item))
        
        return items