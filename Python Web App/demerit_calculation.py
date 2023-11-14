def get_demerit_points(driving_speed, speed_limit, holiday_period=False):
    penalty_points = False

    if driving_speed>speed_limit:
        if 0<(driving_speed-speed_limit)<= 10:
            penalty_points = 10
        elif 20>=(driving_speed-speed_limit)>10:
            penalty_points = 20
        elif 30>=(driving_speed-speed_limit)>20:
            penalty_points = 30
        elif driving_speed-speed_limit > 30:
            penalty_points = 50

        if penalty_points:
            return (True, penalty_points) if (holiday_period and driving_speed-speed_limit>4) or (not(holiday_period) and (driving_speed-speed_limit>5)) else (False, penalty_points)   
    return (False, 0)


def validation(x, y):
    validity = []

    try:
        float(x), validity.append(True)
    except ValueError:    
        validity.append(False)
    try:
        int(y), validity.append(True)
    except ValueError:
        validity.append(False)

    return validity

def message(x, driving_speed, speed_limit):
    if x[1]:
        if x[0] == True:
            option = 'madatory'
        else:
            option = 'discretional'
        return f'The {option} penalty for driving at {driving_speed}km/h in a {speed_limit}km/h zone is {x[1]} points'
    return f'{driving_speed}km/h in a {speed_limit}km/h zone is not speeding.'
    
