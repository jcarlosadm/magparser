from bs4 import BeautifulSoup
import datetime

class Ebook3000Item:
    def __init__(self, html):
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
        
        base = "http://www.ebook3000.com"
        self.image = base + html.find('div', {'class': 'list_box_lit'}).find('img')['src']
        self.link = base + html.find('div', {'class': 'list_box_title'}).find('a')['href']