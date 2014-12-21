from flask import Flask
from flask import render_template, Response
import json
from urllib2 import urlopen

app = Flask(__name__)


@app.route('/')
def home():
    return 'Add municipality in the Url'


@app.route('/<string:komuna>')
def index(komuna):
    return render_template('index.html')


@app.route('/piechart')
def piechart():
    url = "http://0.0.0.0:5030/prokurimi"

    result = urlopen(url).read()
    json_result = json.loads(result)

    return render_template('piechart.html', result=json_result)


@app.route('/<string:komuna>/monthly-summary/<int:viti>')
def merr_json(komuna, viti):
    url = "http://0.0.0.0:5030/%s/monthly-summary/%d" % (komuna, viti)

    result = urlopen(url).read()

    resp = Response(
        response=result, mimetype='application/json')

    return resp


if __name__ == '__main__':
    app.run(debug=True)
