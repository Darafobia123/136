from flask import Flask,jsonify,request
from data import data
app = Flask(__name__)

@app.route("/")
def func():
    return jsonify({
        "data":data,
        "message":"success"

    })
@app.route("/star")
def funct():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data":star_data,
        "message":"success"
    })
app.run(debug=True)