from flask import Flask, render_template,request
from newsapi import NewsApiClient
import requests

app = Flask(__name__)
api_key = "5bcddbf8c4214d30a06df66cb535e8a4" 

newsapi = NewsApiClient(api_key=api_key)

@app.route('/')
def index():
    top_headlines = newsapi.get_top_headlines(country='in', language='en', page_size=10)
    articles = top_headlines['articles']
    return render_template('index.html', articles=articles)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        search_results = newsapi.get_everything(q=query, language='en', page_size=10)
        articles = search_results['articles']
    else:
        articles = []
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
