from bs4 import BeautifulSoup
import requests
import datetime

class Item:
    def __init__(self, html, base):
        self.html = html

        self.title = html.find("div", {'class': 'list_box_title'}).find('a').find(text=True)
        
        self.file_url = html.find('div', {'class': 'list_box_info'}).find(text=True)
        self.file_url = self.file_url[self.file_url.index('http:'):self.file_url.index('...')] \
            .strip()

        self.date = None
        arr_with_date = html.find('div', {'class':'list_box_tools'}).find_all(text=True)
        for item in arr_with_date:
            if 'Date' in item:
                self.date = item.strip()
                break
        
        if self.date != None:
            date_index = int(self.date.index('Date:')+len('Date:'))
            self.date = datetime.datetime.strptime(self.date[date_index:date_index+11].strip(), \
                "%d %b %Y").date()
        
        #self.image = base + html.find('div', {'class': 'list_box_lit'}).find('img')['src']
        self.image = self.get_google_img(self.title)
        self.link = base + html.find('div', {'class': 'list_box_title'}).find('a')['href']

    def get_google_img(self, query):
        """
        gets a link to the first google image search result
        :param query: search query string
        :result: url string to first result
        """
        url = "https://www.google.com/search?q=" + str(query) + "&source=lnms&tbm=isch"
        headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

        html = requests.get(url, headers=headers).text

        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find("img",{"class":"t0fcAb"})

        if not image:
            return 
        return image['src']