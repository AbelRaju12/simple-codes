from flask import Flask, render_template, request

app = Flask("Testing out Flask")

app.route("/")
def getSampleHtml():
    return render_template('sample.html')

@app.route('/user/< username >', methods = ['GET'])
def greetUser(username):
    return render_template("greeting.html", username = username)

@app.route('user', methods = ['GET'])
def greetUseronreq():
    username = request.args.get("username")
    return render_template("greeting.html", username = username)

if __name__ == "__main__": 
    app.run(debug=True)
    