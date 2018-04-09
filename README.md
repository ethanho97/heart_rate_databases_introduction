# heart_rate_databases_introduction &middot; [![Build Status](https://travis-ci.org/ethanho97/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/ethanho97/heart_rate_databases_introduction)[![Documentation Status](https://readthedocs.org/projects/ethanho97-heart-rate-databases-introduction/badge/?version=latest)](http://ethanho97-heart-rate-databases-introduction.readthedocs.io/en/latest/?badge=latest)

This mini-project is a web service where one can post user data containing email, age, and heart rate and get all their recorded measurements, average heart rate, and average heart rate since a specified time via a post request.

MongoDB is the database program used and Docker is used to run it. The `User` class uses the MongoDB data model which can be found in `models.py`. `main.py` contains all the functions which are used to actually store and retrieve data while `basic.py` is what manages the POST and GET requests. The `models.py` and `main.py` skeleton codes were made by [Suyash Kumar](https://github.com/suyashkumar).

Use `pip install -r requirements.txt` to get all the packages necessary to run this.



## Modules
- `models.py`: MongoDB data model for `User`
- `main.py`: Contains functions to create/add `User` data and find measurements and averages given an email
- `basic.py`: Contains POST and GET requests
- `test_main.py`: Unit testing using pytest to test functions found in `main.py`
