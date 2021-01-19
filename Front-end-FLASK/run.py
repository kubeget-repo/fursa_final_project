import requests 
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
import os


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html',backendip=os.environ.get('backendip'))

@app.route('/log')
def log():
    return render_template('log.html',backendip=os.environ.get('backendip'))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
    
    #fetch_date()
    #sympols()
    pass
