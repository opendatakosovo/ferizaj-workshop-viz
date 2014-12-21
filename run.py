from flask import Flask
from flask import render_template, Response
import json
from urllib2 import urlopen

app = Flask(__name__)


@app.route('/')
def home():
    return 'Shiko kodin dhe ndjek instruksionet'


@app.route('/<string:komuna>')
def index(komuna):
    #Kur te navigojme ne /ferizaj duhet te na shfaqet Line Chart
    return render_template('index.html')


@app.route('/piechart')
def piechart():
    #TODO: Kthe render_template ne piechart.html dhe kthe rezultatin
    #Kerkesa duhet te behet ne API dhe te kthehet rezultati si JSON
    #Per kete eshte importuar libraria json dhe te perdoret metoda json.loads(rezultati)
    #para se te kthehet rezultati si parameter

    return "Rendero template dhe kthe nje variabel result"


@app.route('/<string:komuna>/monthly-summary/<int:viti>')
def merr_json(komuna, viti):
    #TODO: kthe nje Response te tipit application/json duke bere kerkese
    # ne API

    return "TODO"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
