from flask import Flask
from views import views

app = Flask(__name__)
 
#Registering the blueprint created in views.py, secret key for session info needed for request. 
app.register_blueprint(views, url_prefix='/')
app.secret_key = 'secret'

#Start app if it is not imported
if __name__ == '__main__':
    app.run(debug=True)