from app import app # this refers to app folder, then imports directly from __init__.py file the app instance of Flask class contained within
from flask import render_template


@app.route('/') # this creates a route to the page
def index():
    return render_template('index.html')
    # default folder accessed by render_template fn is a folder called 'templates', so have to name folder 'templates'


@app.route('/fav5') # this creates a different page
def test():
    fav_artists = ['Beatles', 'Led Zeppelin', 'Marvin Gaye', 'Stevie Wonder', 'Rolling Stones']
    same_variable_name = 'this variable will have the same key value pair'
    return render_template('fav5.html', artists=fav_artists, same_variable_name=same_variable_name)