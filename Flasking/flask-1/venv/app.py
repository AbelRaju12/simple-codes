from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route("/")
# @app.route("/health", methods = ["GET", "POST"])
def hello_world():    
    return {"message": "Hello World"}
    # return jsonify(message="Hello World")
    
    # res = make_response("<b>Helloo world</b>")
    # res.status_code = 200
    # return res
    
    
    # if requests.method == "GET": return jsonify(status="OK", method="GET"), 200
    # if requests.method == "POST": return jsonify(status="OKAY", method="POST"), 200
    
# @app.route("/network/<uuid:uuid>")
# def uuid(uuid):
#     res = requests.get("https://anotherapi/getnetwork/{uuid}.JSON")
#     if res.status_code == 200:
#         return {"message": res.JSON()}
#     elif res.status_code == 404:
#         return {"message": "Network not found"} 
#     else:
#         return {"message": "Something went wrong"}   