# adapted from: 
# https://abndistro.com/post/2019/01/20/using-flask-to-deploy-predictive-models/

# app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world 1\n'

# adapted from https://palletsprojects.com/p/flask/
@app.route('/hello')
def hello():
    name = request.args.get("name", "World 2")
    return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    app.run()