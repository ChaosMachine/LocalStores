from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import hashlib



def init_app():
    app = Flask(__name__)
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        return app
    from .plotlydash.dashboard import init_dashboard
    init_dashboard(app)
    print("initialized")
    # Change this to your secret key (can be anything, it's for extra protection)
    

    # http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
   
