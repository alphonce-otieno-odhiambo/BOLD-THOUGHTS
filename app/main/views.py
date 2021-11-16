from . import main
from flask import render_template,redirect, url_for



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/post')
def post():

    
    return render_template( redirect(url_for('post.html')))
