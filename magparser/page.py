from bs4 import BeautifulSoup
import requests

from magparser.item import Item

class Page:
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
            items.append(Item(html_item, self.base_url[self.base_url.index('http:'): \
                self.base_url.index('.com') + len('.com')]))
        
        return items