from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return {"message": "Hello World"}
    return jsonify(message="Hello World")

