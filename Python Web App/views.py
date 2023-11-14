from flask import Blueprint, render_template, request, flash
from demerit_calculation import get_demerit_points, message, validation

#Blueprint created with routes @ views
views = Blueprint(__name__, 'views')

@views.route('/', methods=['POST', 'GET'])
def home():
    ''' Route for home page of demerit calculator. 

    Renders the home template and takes user input on web app, when user submits the information is calculated 
    using functions from demerit_calculation.py and will flash messages to the web app home page is user submitted
    information is invalid

    '''
    if request.method == 'POST':

        driving_speed = request.form['driving_speed']
        speed_limit = request.form['speed_limit']

        validity = validation(request.form['driving_speed'], request.form['speed_limit'])
        
        if all(validity):
            holiday_period = request.form.get('holiday_period')
            return render_template('calculation.html', calculation=message(get_demerit_points(float(driving_speed), int(speed_limit), holiday_period), driving_speed, speed_limit))

        # Flash Messages
        elif not(any(validity)):
            flash('Driving speed must be type int or float. Speed limit must be type int.')
        elif validity[0] == True:
            flash('Speed limit must be type int.')
        else:
            flash('Driving speed must be type int or float.')

    # Default when not method POST
    return render_template('home.html')

@views.app_errorhandler(404)
def bad_path(error):
    '''Bad route handler, will return an html template informing the user and automatically redirect them
    back to the home page.'''
    return render_template('bad_url_path.html')