
from . import main
from flask import render_template,redirect, url_for, flash
from .forms import PostForm
from .. models import Post, User
from .. import db
from flask_login import login_required






@main.route('/')
def index():
    blogs = Post.query.order_by(Post.submited)
    return render_template('index.html', blog = blogs)




@main.route('/post', methods = ['GET', 'POST'])
@login_required
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
