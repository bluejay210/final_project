from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)

import giphypop
g = giphypop.Giphy()

# Main Page
@app.route('/')
def index():
	return render_template('index.html')

# Project Group Introduction Page
@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/results')
def results():
	search_result = request.values.get('input')
	results = g.search(search_result)
	media = []

	try: 
		for result in results:
			media.append(result.media_url)
			message = "Search Results for"
			keyword = request.args.get('input')
		return render_template('results.html', search_result=media, message=message, keyword=keyword)
	except:
		media = []
		message = "Nothing Found"
		return render_template('results.html', search_result=media, message=message)


app.run(debug=True)

