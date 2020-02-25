from app import app

'''
@app.route decorator creates an association between the URLs given as argument and the function. In this example
we have three pairs of functions and decorators which associate the URLs ('/') ; ('/about') and ('/index') to the 
functions home , about and index. This means that when the web browser requests any of these URLs, Flask is going
to invoke these functions and pass the return value to browser as a response
'''


@app.route('/')
def home():
    return 'Hello Home Page'

@app.route('/about')
def about():
    return 'This is about learning flask'

@app.route('/index')
def index():
    return '- module1 \n- module2 \n- module3 \n.\n.\n.\n- module18'