from Application import app
from flask import render_template
from flask.ext.security import login_required
from flask.ext.classy import FlaskView, route

# Classy index example.

class Index(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')


    @route('/protected')
    @login_required
    def protected(self):
    	return render_template('index.html', 
    		content='This is a protected view')

Index.register(app)
