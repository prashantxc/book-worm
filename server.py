"""
Flask server for libgenesis API
@author prashantxc
@licence MIT License
"""

from flask import Flask, jsonify

import get_book


app = Flask(__name__)

@app.route("/getTitle")
def get_title_result():
    """API end point for Book Request"""
    book_response = get_book.get_by_title()

    return jsonify({
        "news": book_response
    })

@app.route("/getAuthor")
def get_author_result():
    """API end point for Book Request"""
    book_response = get_book.get_by_author()

    return jsonify({
        "news": book_response
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