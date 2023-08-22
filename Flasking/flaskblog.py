from flask import Flask, render_template, url_for
app = Flask(__name__)

posts =[
    {
        'author': ' Gouri Varma',
        'title': 'My cooking recipes',
        'content': 'Blog content',
        'date_posted': 'April 29, 2023'                
    },
    {
        'author': ' Abel Raju',
        'title': 'My gaming life',
        'content': 'blog content',
        'date_posted': 'April 30, 2023'                
    }
]

@app.route("/")
@app.route("/home")
def Home():
    return render_template('home.html', posts = posts) #first posts is a variable
    # '''
    # <!doctype html>
    # <html>
    # </html>
    # '''

@app.route("/about")
def about():
    return render_template('about.html', title = 'About page')


if __name__ == '__main__': #we can run app directly instead of flask run
    app.run(debug=True)