from flask import Blueprint, render_template, request, url_for, redirect

views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template('index.html', value='this is a test')

@views.route('/profile')
def profile():
    
    # commented section takes argument from route eg /profile?name=ben
    args=request.args
    name=args.get('name')
    # will default to None on /profile route

    return render_template('index.html', value=name)

@views.route('/redirect')
def bad_path():
    return redirect(url_for("views.home"))