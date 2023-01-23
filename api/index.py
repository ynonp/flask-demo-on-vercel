from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'some new text'

@app.route('/about')
def about():
    return 'About'
