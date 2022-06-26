from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/get_topics")
@cross_origin()
def getTopics():
    return jsonify(["All", "Computer", "Science"])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)