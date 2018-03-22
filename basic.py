from flask import Flask, jsonify, request
app = Flask(__name__)
import datetime
import numpy as np
from main import *


@app.route("/api/heart_rate", methods=["POST"])
def user_data():
    r = request.get_json()
    email = r["user_email"]
    age = r["user_age"]
    hr = r["heart_rate"]
    time = datetime.datetime.now()
    try:
        user = add_heart_rate(email, hr, time)
    except:
        user = create_user(email, age, hr, time)

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_rate(email):
    data = user_data(email)
    return jsonify(data)

@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def avg_heart_rate(email):
    hr = hr_data(email)
    average = {
        "average_heart_rate": np.mean(hr)
    }
    return jsonify(average)

# @app.route("/api/heart_rate/interval_average", methods=["POST"])
# def int_avg(email):
