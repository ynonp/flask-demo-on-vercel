from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return { "text": "Hello WOrld" }

@app.route('/about')
def about():
    return 'About'
