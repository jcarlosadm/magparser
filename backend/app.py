from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from datetime import date, timedelta, datetime
from topics import get_topics

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/get_topics")
@cross_origin()
def getTopics():
    start_date = request.args.get('startDate', default = date.today() - timedelta(days=5), \
        type = to_date).strftime("%Y-%m-%d")
    end_date = request.args.get('endDate', default = date.today(), type = to_date)\
        .strftime("%Y-%m-%d")

    # TODO: use cache
    return jsonify(get_topics(start_date, end_date))

def to_date(dateString):
    return datetime.strptime(dateString, "%Y-%m-%d").date()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)