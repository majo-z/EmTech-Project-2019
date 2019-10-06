# adapted from: 
# https://abndistro.com/post/2019/01/20/using-flask-to-deploy-predictive-models/

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!\n'

if __name__ == '__main__':
    app.run()