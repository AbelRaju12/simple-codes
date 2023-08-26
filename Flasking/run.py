from flaskblog import app #will import from __init__ file

if __name__ == '__main__': #we can run app directly instead of flask run
    app.run(debug=True)