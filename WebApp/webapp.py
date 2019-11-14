# Adapted from: https://www.palletsprojects.com/p/flask
# Run the app: env FLASK_APP=webapp.py flask run
import flask as fl

app = fl.Flask(__name__)

# Request default resource
@app.route('/')
def home():
    return app.send_static_file("recognise.html")

