from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return '<h2>On Test Route</h2>'

    