from bs4 import BeautifulSoup
import requests

DEFAULT_URL = "http://www.ebook3000.com/index_%s.htm"

def get_topics(start_date, end_date):
    stop_search = False
    current_page = 1
    topics = ["All"]
    while(not stop_search):
        page_url = DEFAULT_URL % current_page

        headers = requests.utils.default_headers()
        headers.update({ 'User-Agent': 'Mozilla/5.0 \
            (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        
        req = requests.get(page_url, headers)

        soup = BeautifulSoup(req.content, 'html.parser')

        html_items = soup.find_all("div", {'class':'index_box'})

        for item in html_items:
            date = extract_date(item)
            
            if (date >= start_date and date <= end_date):
                topic = extract_topic(item)
                if topic not in topics:
                    topics.append(topic)
            else:
                stop_search = True

        current_page += 1

    return topics

def extract_date(html_item):
    txt = html_item.find('div', {'class': 'index_box_tools'}).find_all(text=True)[2]

    return format_date(txt[len('Date:')+1:-2])

def extract_topic(html_item):
    txt = html_item.find('div', {'class': 'index_box_tools'})\
        .find('a').find_all(text=True)[0]
    return txt

def format_date(date):
    date_parts = date.split(' ')
    return date_parts[2] + "-" + get_month(date_parts[1]) + "-" + date_parts[0]

def get_month(m_str):
    return {
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'
    }.get(m_str)