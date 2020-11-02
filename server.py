"""
Flask server for time.com "The Brief" section API
@author prashantxc
@licence MIT License
"""

from flask import Flask, jsonify


app = Flask(__name__)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port="8000")