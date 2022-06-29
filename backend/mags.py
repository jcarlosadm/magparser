from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup

from utils import get_soup

DEFAULT_URL = "http://www.ebook3000.com/index_%s.htm"
MAX_PAGE = -1

def to_date(dateString):
    if dateString is None or dateString == "":
        return None
    return datetime.strptime(dateString, "%Y-%m-%d").date()

def process_args(args):
    if args.get('startDate') is None or args.get('startDate') == 'null' \
        or args.get('startDate') == '':
        start_date = None
    else:
        start_date = args.get('startDate', type = to_date).strftime("%Y-%m-%d")
    
    if args.get('endDate') is None or args.get('endDate') == 'null' \
        or args.get('endDate') == '':
        end_date = None
    else:
        end_date = args.get('endDate', type = to_date).strftime("%Y-%m-%d")

    return {
        'selected_topic': args.get('selectedTopic', default= 'All', type = str),
        'start_date': start_date,
        'end_date': end_date,
        'search_term': args.get('searchTerm', default='', type = str).lower(),
        'current_page': args.get('currentPage', default=1, type = int),
        'max_content_per_page': args.get('maxContentPerPage', default=10, type = int)
    }

def get_url(page):
    return DEFAULT_URL % page

def get_mag_info(mag_html):
    return_obj = {}

    return_obj['title'] = mag_html.find('div', {'class': 'index_box_title'}).find('a').find(text=True)
    return_obj['category'] = mag_html.find('div', {'class':'index_box_tools'}).find('a').find(text=True)
    return_obj['date'] = format_date(mag_html.find('div', {'class':'index_box_tools'}).find_all(text=True)[-1][len('Date:')+1:-2])
    return_obj['img'] = "http://www.ebook3000.com" + mag_html.find('div', {'class':'index_box_lit'}).find('img').get('src')
    return_obj['post_url'] = "http://www.ebook3000.com" + mag_html.find('div', {'class': 'index_box_title'}).find('a').get('href')
    
    infos = mag_html.find('div', {'class': 'index_box_info'}).find(text=True).strip().split("|")
    
    return_obj['language'] = infos[0].strip()
    return_obj['pages'] = infos[1].strip()[0:(-1)*(len("pages")+1)]
    
    if len(infos) >= 4:
        return_obj['type'] = infos[2].strip()
        index_to_use = 3
    else:
        return_obj['type'] = ''
        index_to_use = 2
    
    size = infos[index_to_use].strip()
    return_obj['size'] = size[0:size.index('MB')].strip() + ' MB'

    url = infos[index_to_use].strip()
    return_obj['download_url'] = url[url.index('http'):-3].strip()

    return return_obj


def validate_topic(mag_html, obj_args):
    if obj_args['selected_topic'] == "All":
        return True
    category = mag_html.find('div', {'class':'index_box_tools'}).find('a').find(text=True)
    return obj_args['selected_topic'] == category

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

def format_date(date):
    date_parts = date.split(' ')
    return date_parts[2] + "-" + get_month(date_parts[1]) + "-" + date_parts[0]

def validate_dates(mag_html, obj_args):
    if obj_args['start_date'] is None and obj_args['end_date'] is None:
        return True
    txt = mag_html.find('div', {'class':'index_box_tools'}).find_all(text=True)[-1]
    date = format_date(txt[len('Date:')+1:-2])
    return (obj_args['start_date'] is None or date >= obj_args['start_date']) \
        and (obj_args['end_date'] is None or date <= obj_args['end_date'])

def validate_search_terms(mag_html, obj_args):
    if obj_args['search_term'] is None or obj_args['search_term'] == ''\
        or obj_args['search_term'] == 'null':
        return True
    title = mag_html.find('div', {'class': 'index_box_title'}).find('a').find(text=True)\
        .lower()
    terms = obj_args['search_term'].split(' ')
    return any(term in title for term in terms)

def validate_mag(mag_html, obj_args):
    return validate_topic(mag_html, obj_args) and validate_dates(mag_html, obj_args) \
        and validate_search_terms(mag_html, obj_args)

def get_mags(args, cache):
    obj_args = process_args(args)
    mags = []

    current_page = 1
    start_get_n = ((int(obj_args['current_page']) - 1) * \
        int(obj_args['max_content_per_page'])) + 1
    max_n = start_get_n + int(obj_args['max_content_per_page']) - 1
    count_n = 0
    while(len(mags) < int(obj_args['max_content_per_page']) and (MAX_PAGE < 0 or current_page <= MAX_PAGE)):
        url = get_url(current_page)

        if cache.get(url) is not None:
            html = cache.get(url)
            soup = BeautifulSoup(html,"html.parser")
        else:
            soup = get_soup(url)
            html = str(soup)
            cache.set(url, html)

        mags_html = soup.find_all("div", {"class": "index_box"})
        for mag_html in mags_html:
            if validate_mag(mag_html, obj_args):
                count_n += 1
                if count_n >= start_get_n and count_n <= max_n:
                    mags.append(get_mag_info(mag_html))

        current_page += 1

    return mags