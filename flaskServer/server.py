from flask import Flask,jsonify, render_template
from flask_pymongo import PyMongo
import random

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'python-test'
app.config['MONGO_URI'] = 'mongodb://<username>:<password>@ds123926.mlab.com:23926/python-testing'

mongo = PyMongo(app)

@app.route('/add')
def add():
    data = mongo.db.data
    data.insert({'value': '1'})
    return "Data inserted!"


@app.route('/random')
def randomize():
    x = random.randint(0, 10)
    randomNum = mongo.db.data
    randomNum.insert({'Data' : x})

    return str(x) + " Inserted"

@app.route('/star', methods=['GET'])
def get_all_stars():
    data = mongo.db.data
    output = []
    for s in data.find():
        output.append(s["Data"])
    print(output)
    return render_template('index.html', output=output)
if __name__ == '__main__':
    app.run(debug=True)

