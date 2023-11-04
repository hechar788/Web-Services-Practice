from flask import Blueprint, render_template, request, url_for, redirect

views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template('index.html', value='Return')

@views.route('/profile')
def profile():
    
    # Takes argument from route eg /profile?name=ben

    args=request.args
    name=args.get('name', '')

    # name variable will default to an empty string on /profile route
 
    return render_template('profile.html', value=name)

@views.route('/redirect')
def bad_path():
    return redirect(url_for("views.home"))