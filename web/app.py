from flask import Flask
app = Flask(__name__)

from magparser import Page

def load_items(base_url, date_limit, filter_title):
    parser = Page(base_url)
    current_page = 1
    items = []
    while current_page != None:
        for item in parser.get_items_from_page(current_page):
            if item.date >= date_limit:
                if filter_title != None and filter_title != "" and \
                    filter_title.replace(' ', '').lower() in \
                    item.title.replace(' ', '').lower():
                    items.append(item)
                elif filter_title == None or filter_title == "":
                    items.append(item)
            else:
                current_page = None
                break
        if current_page != None:
            current_page += 1
    return items