import requests 
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
import mysql.connector
import os
from datetime import datetime

api_url='http://data.fixer.io/api/'
api_key='access_key=d451b7e4294ef3a882f30badd546f344'

mydb = mysql.connector.connect(
  host= "mysql",
  user="root",
  password="root",
  database="mydb"
)
mycursor=mydb.cursor()

def init_db():
    sql= """
    CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log TEXT NOT NULL,
    created_at TEXT NOT NULL
    );
    """
    #sql="DROP TABLE logs"
    mycursor.execute(sql)
    mydb.commit()

def get_logs():
    mycursor.execute(""" SELECT  *  FROM logs order by id desc """)
    data= mycursor.fetchall()
    return data;



def sympols():
    r = requests.get(api_url+"symbols?"+api_key)
    rates= r.json()["symbols"].keys()
    return list(rates)

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return jsonify(sympols())

@app.route('/calc',methods = ['POST'])
def calc():
    from_rate= request.form.get('fromrate')
    to_rate= request.form.get('torate')
    amount= request.form.get('amount')

    r = requests.get(api_url+"latest?"+api_key+"&base="+from_rate+"&symbols="+to_rate)
    total=(float(r.json()["rates"][to_rate])*float(amount))

    mycursor.execute("INSERT INTO logs (log,created_at) VALUES('{2} convert from {0} to {1} amount {3}, total: {4}','{5}')".format(from_rate,to_rate,request.remote_addr,amount,total,datetime.now()))
    mydb.commit()

    return jsonify('{ "total" : '+str(total)+'}')

@app.route('/log')
def log():
    return jsonify(get_logs())

if __name__ == "__main__":
    init_db()
    #get_logs()
    app.run(host="0.0.0.0",port=5000)
    pass
