import requests 
from flask import Flask,render_template,request
api_url='http://backend:5000/'
import json 

def sympols():
    r = requests.get(api_url)
    rates= r.json()
  
    return "".join(list(map(lambda e : "<option value=\""+e+"\">"+e+"</option>" ,rates)))

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html',rates=sympols())

@app.route('/calc')
def calc():
    from_rate= request.args.get('fromrate')
    to_rate= request.args.get('torate')
    amount= request.args.get('amount')
    r = requests.post(api_url+"calc",{'fromrate':from_rate,'torate':to_rate,'amount':amount})
    jtotal=json.loads(r.json())
    return render_template('index.html',rates=sympols(),total= str(jtotal['total']))

@app.route('/log')
def log():
    r = requests.get(api_url+"log")
    jrows=r.json()
    rows="".join(list(map(lambda e: """<tr>
                        <th scope="row">{0}</th>
                        <td>{1}</td>
                        <td>{2}</td>
                    </tr>""".format(e[0],e[1],e[2]),jrows)))
    return render_template('log.html',rows=rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
    #fetch_date()
    #sympols()
    pass
