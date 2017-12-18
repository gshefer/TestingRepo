#!flask/bin/python
from flask import Flask


app = Flask(__name__)

@app.route('/yehoachin2')
def yehoachin()
    return 'yehoachin3'


@app.route('/yehoyachin')
def yehoyachin():
    return 'yehoyachin!'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
