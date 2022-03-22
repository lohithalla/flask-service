from flask import Flask
import requests
app = Flask(__name__)

@app.route('/service_a')
def hello_world():
    service_c_url = 'http://service-c/service_c'
    response = requests.get(service_c_url).text
    return 'Welcome to service_a: ---> ' + response
