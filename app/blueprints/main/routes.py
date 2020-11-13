from flask import render_template
from .import bp as main

from app.models import User

# empty route/home route
@main.route('/', methods=['GET']) # listening for activity
def index():
    users = [
        User(1, 'Derek', 'Hawkins', 'derekh@codingtemple.com'),
        User(2, 'Ripal', 'Patel', 'ripalp@codingtemple.com'),
        User(3, 'Sam', 'Davitt', 'samd@codingtemple.com')
    ]

    context = {
        'users': users,
    }
    return render_template('main/index.html', **context)

@main.route('/about', methods=['GET'])
def about():
    return render_template('main/about.html')

@main.route('/contact', methods=['GET'])
def contact():
    return render_template('main/contact.html')