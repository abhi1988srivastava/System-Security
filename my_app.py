import flask
from flask import request

# Create the application.
APP = flask.Flask(__name__)



@APP.route('/index_easy')
def index_easy():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_easy.html')

@APP.route('/index_hard')
def index_hard():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_hard.html')

@APP.route('/index_hardest')
def index_hardest():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_hardest.html')


@APP.route('/another_link')
def another_link():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('another_link.html')


@APP.route('/link1')
def link1():
    return flask.render_template('link1.html')

@APP.route('/link2')
def link2():
    return flask.render_template('link2.html')

@APP.route('/link3')
def link3():
    return '<html><body>I am of no use buoy..just a bad link </html>'

@APP.route('/move_ahead1')
def move_ahead1():
    return flask.render_template('move_ahead1.html')

@APP.route('/move_ahead2')
def move_ahead2():
    return flask.render_template('move_ahead2.html')

@APP.route('/access_link2')
def access_link2():
    return flask.render_template('access_link2.html')

@APP.route('/info_link2')
def info_link2():
    return flask.render_template('info_link2.html')

@APP.route('/register')
def register():
    return flask.render_template('register.html')


@APP.route('/create_easy')
def create_easy():
    return flask.render_template('login_easy.html')

@APP.route('/create_hard')
def create_hard():
    return flask.render_template('login_hard.html')

@APP.route('/create_hardest')
def create_hardest():
    return flask.render_template('login_hardest.html')


@APP.route('/loginEasy', methods=['POST'])
def loginEasy():
    user=None
    passw=None
    #forms=request.form
    user=request.form['username']
    passw=request.form['password']
    if passw=="password":
        return flask.render_template('valid.html') 
    else:
        return flask.render_template('invalid.html')
    
    
@APP.route('/loginHard', methods=['POST'])
def loginHard():
    user=None
    passw=None
    #forms=request.form
    user=request.form['username']
    passw=request.form['password']
    if passw=="Username53cur17y":
        return flask.render_template('valid.html') 
    else:
        return flask.render_template('invalid.html')


@APP.route('/loginHardest', methods=['POST'])
def loginHardest():
    user=None
    passw=None
    #forms=request.form
    user=request.form['username']
    passw=request.form['password']
    if passw=="51nc3NOW" and user=="admin":
        
        return flask.render_template('valid.html') 
    else:
        return flask.render_template('invalid.html')
    

if __name__ == '__main__':
    #APP.debug=True
    APP.run(debug=True)
