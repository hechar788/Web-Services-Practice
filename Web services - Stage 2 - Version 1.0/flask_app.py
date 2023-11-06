from flask import Flask, redirect, url_for
from views import views


app = Flask(__name__)

# Used to encrypt session information
app.secret_key = 'secret'

app.register_blueprint(views, url_prefix="/")



#runs web app
if __name__ == '__main__':
    app.run(debug=True, port=8080)
    