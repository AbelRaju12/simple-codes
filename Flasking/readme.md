simple code implementing flask

useful tips
-----------------

$env:FLASK_APP = "flaskblog.py" (To set flask)
flask run

$env:FLASK_DEBUG = 1  (To run in debug mode)
flask run

if __name__ == '__main__':
    app.run(debug=True)
#we can run app directly instead of flask run

return render_template('about.html', title = 'About page')
we can add variables like 'title' and call it in html like 
    {% if title %}
        <title> Flaskblog - {{ title }} </title>
    {% else %}
        <title> Flaskblog </title>
    {% endif %}

we can import contents of an html using {% extends name.html %}

{% block content %}{% endblock %} 
Here 'content' is user defined
