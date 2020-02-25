from magparser import Ebook3000Page
from magparser import Ebook3000Urls

parser = Ebook3000Page(Ebook3000Urls.SCIENCE)
items = parser.get_items_from_page(1)

for item in items:
    print(item.title)