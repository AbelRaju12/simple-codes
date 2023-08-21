from flask import Flask

app = Flask("My first app")

@app.route('/') # not specified implies GET
def hello():
    return 'Hello World'

if __name__ == "__main__":  #default unless explicitly changed
    app.run(debug=True)