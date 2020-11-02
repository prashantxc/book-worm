"""
Flask server for libgenesis API
@author prashantxc
@licence MIT License
"""

from flask import Flask, jsonify

import get_book as getBook


app = Flask(__name__)

@app.route("/getBook")
def get_url_result():
    """API end point for Book Request"""
    news_response = getBook.get_by_title()

    return jsonify({
        "news": news_response
    })

# Test API
@app.route("/ok")
def ohkay():
    return jsonify({
        "ok": True
    })

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port="8000")