from flask import render_template
from flask import request
from datetime import date
import datetime

from magparser import url_hash
from web.app import app
from web.app import load_items

@app.route('/')
def home():
    keys = list(url_hash.keys())
    topic = get_topic(request.args, keys)
    date_limit = get_datelimit(request.args)
    date_limit_2 = get_datelimit_2(request.args)
    filter_title = get_filter_title(request.args)

    return render_template('index.html', \
        items = load_items(url_hash[topic], date_limit, date_limit_2, filter_title),
        topics = keys,
        selected_topic = topic,
        date_limit=date_limit.strftime('%Y-%m-%d'),
        date_limit_2=date_limit_2.strftime('%Y-%m-%d'),
        filter_title=filter_title)

def get_topic(args, keys):
    if 'topics_select' in args:
        topic = args['topics_select']
    else:
        topic = keys[0]
    return topic

def get_datelimit(args):
    if 'date_limit' in args:
        date_limit = datetime.datetime.strptime(args['date_limit'], '%Y-%m-%d').date()
    else:
        date_limit = datetime.datetime.now() - datetime.timedelta(days=10)
        date_limit = date_limit.date()
    return date_limit

def get_datelimit_2(args):
    if 'date_limit_2' in args:
        date_limit_2 = datetime.datetime.strptime(args['date_limit_2'], '%Y-%m-%d').date()
    else:
        date_limit_2 = datetime.datetime.now()
        date_limit_2 = date_limit_2.date()
    return date_limit_2


def get_filter_title(args):
    if 'filter_title' not in args:
        return ''
    return args['filter_title']