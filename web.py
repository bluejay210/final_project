from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)

import giphypop
g = giphypop.Giphy()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/results')
def results():
	search_result = request.values.get('input')
	results = g.search(search_result)
	media = []

	for result in results:
		media.append(result.media_url)

	return render_template('results.html', media=media)


app.run(debug=True)

