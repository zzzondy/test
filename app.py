from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Ты лох'


if __name__ == '__main__':
    app.run()
