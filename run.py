from flask import Flask
from flask import render_template, Response
from urllib2 import urlopen

# Create the flask app.
app = Flask(__name__)


@app.route('/')
def home():
	return 'Add municipality in the Url'

@app.route('/<string:komuna>')
def index(komuna):
	return render_template('index.html')

@app.route('/<string:komuna>/monthly-summary/<int:viti>')
def merr_json(komuna, viti):
    url = "http://0.0.0.0:5030/%s/monthly-summary/%d" % (komuna, viti)

    result = urlopen(url).read()

    # Build response object.
    resp = Response(
        response=result, mimetype='application/json')

    # Return response.
    return resp
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
