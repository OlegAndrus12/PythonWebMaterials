import requests

from flask import Flask, render_template
from config import NEWS_API_KEY

app = Flask(__file__)

@app.route("/")
def index():
    url = f'https://newsapi.org/v2/everything?q=Trump&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])
    return render_template("index.html", articles=articles)





app.run(debug=True)