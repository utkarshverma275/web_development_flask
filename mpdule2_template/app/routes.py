from app import app
from flask import render_template
@app.route('/')
def home():
    return 'To be yourself in a world that is constantly trying to make you something else.\n Is a great achievement.'

@app.route('/index')
def index():
    user = {'username': 'Ralph Waldo Emerson'}
    return render_template('index.html', title='Home', user=user)
