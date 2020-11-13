from flask import render_template
from .import bp as blog
from app.models import Post

@blog.route('/', methods=['GET'])
def index():
    """
    [GET] /blog
    """
    posts = [
        Post(1, 'This is the first blog post.'),
        Post(2, 'This is the second blog post.'),
        Post(3, 'This is the third blog post.')
    ]
    context = {
        'posts': posts
    }
    return render_template('blog/index.html', **context)

@blog.route('/<int:id>')
def single(id):

    """
    [GET] /blog/1
    """
    Post(1, 'This is the first blog post.'),
    Post(2, 'This is the second blog post.'),
    Post(3, 'This is the third blog post.')

    for p in Post._instances:
        if p.id == id:
            post = p
    return render_template('blog/single.html', post=post)