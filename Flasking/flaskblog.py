from flask import Flask, render_template, url_for
from forms import Registrationform, Loginform

app = Flask(__name__)

app.config['SECRET_KEY'] = '2eb7321528e3ca028390d27ed0e1e720'

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
  
@app.route("/about")
def about():
    return render_template('about.html', title = 'About page')

@app.route('/register')
def register():
    form = Registrationform()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = Loginform()
    return render_template('login.html', title = 'Loginr', form = form)

if __name__ == '__main__': #we can run app directly instead of flask run
    app.run(debug=True)