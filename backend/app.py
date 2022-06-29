from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_caching import Cache

from topics import get_topics
from mags import get_mags

config = {
    'CORS_HEADERS': 'Content-Type',
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 600
}

app = Flask(__name__)
cors = CORS(app)
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/api/get_topics")
@cross_origin()
def getTopics():
    return jsonify(get_topics(cache))

@app.route("/api/get_mags")
@cross_origin()
def getMags():
    return jsonify(get_mags(request.args, cache))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)