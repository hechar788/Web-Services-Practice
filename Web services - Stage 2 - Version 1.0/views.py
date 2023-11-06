from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from time import *
import json

views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template('index.html', value='Return')

@views.route('/profile', methods=['POST', "GET"])
def profile():

    # Takes argument from route eg /profile?name=ben
    #args=request.args
    #name=args.get('name', '')
    # name variable will default to an empty string on /profile route, name variable must be passed in render_template to be accessible in html doc
    #e.g. return render_template('profile.html', value=name)
 
    # Request finds method used e.g 'POST' or 'GET'

    # If the method used when profile route is accessed is 'POST' it will take the user information submitted in the html form
    if request.method == 'POST':
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("views.user"))
    

    return render_template('profile.html')

@views.route('/user')
def user():
    if 'user' in session:
        user=session['user']
        return f'<center><h1>{user}</h1></center>'
    return redirect(url_for('views.profile'))

@views.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        if not request.method == 'POST':
            return render_template('logout.html')
    return redirect(url_for('views.profile'))

@views.app_errorhandler(404)
def handle_exception(e):
    return redirect(url_for('views.profile'))