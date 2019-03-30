"""
@author Gatsby Lee
@since 2018-10-28
"""
from flask import Flask, request
from cloud_function import pingback

app = Flask(__name__)


@app.route('/')
def pingback_service():
    return pingback(request)


if __name__ == '__main__':
    app.run()
