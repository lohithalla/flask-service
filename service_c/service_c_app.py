from flask import Flask
app = Flask(__name__)

@app.route('/service_c')
def hello_world():
    return 'Welcome to service_c'
