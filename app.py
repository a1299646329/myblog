from flask import Flask, make_response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    result_text = {"statusCode": 200, "message": "hello, world"}
    return result_text


if __name__ == '__main__':
    app.run()
