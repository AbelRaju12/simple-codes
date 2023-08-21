from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def Home():
    return "<h1> Home  Page </h1>"

@app.route("/about")
def about():
    return "<h2>About page</h2>"


if __name__ == '__main__': #we can run app directly instead of flask run
    app.run(debug=True)