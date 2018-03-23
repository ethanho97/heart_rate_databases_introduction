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
    try:
        user = add_heart_rate(email, hr, time=datetime.datetime.now())
    except:
        user = create_user(email, age, hr, time=datetime.datetime.now())
        return "User data created"
    return "User data updated"

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def user_heart_rate(user_email):
    data = get_data(user_email)
    return jsonify(data)

@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def user_avg_heart_rate(user_email):
    hr = hr_data(user_email)
    average = {
        "average_heart_rate": np.mean(hr)
    }
    return jsonify(average)

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def user_int_avg():
    r = request.get_json()
    email = r["user_email"]
    ref_time = r["heart_rate_average_since"]
    int_avg = {
        "interval average since time": interval_data(email, ref_time)
    }
    return jsonify(int_avg)
