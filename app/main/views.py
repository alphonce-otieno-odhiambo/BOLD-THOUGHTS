from werkzeug import useragents
from . import main
from flask import render_template,redirect, url_for, flash
from .forms import PostForm
from .. models import Post, User
from .. import db






@main.route('/')
def index():
    post = Post.query.all()
    return render_template('index.html', post = post)

@main.route('/post', methods = ['GET', 'POST'])
def post():
    post = PostForm()
    if post.validate_on_submit():
        post = Post( title = post.title.data, content = post.content.data)

        #Add to data base
        db.session.add(post)
        db.session.commit()
        flash('your post has been posted')
        return redirect(url_for('main.post'))
    return render_template('post.html',post = post)
    

    
  #return render_template( redirect(url_for('post.html')))
