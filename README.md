# heart_rate_databases_introduction
This mini-project is a web service where one can post user data with email, age, and heart rate and get all their recorded measurements, average heart rate, and average heart rate since a specified time via a post request.

The `User` class uses the MongoDB data model. Docker was used to run the MongoDB program.

## Modules
- `models.py`: MongoDB data model for `User`
- `main.py`: Contains functions to create/add `User` data and find measurements and averages given an email
- `basic.py`: Contains POST and GET requests
- `test_main.py`: Unit testing use pytest to test functions found in `main.py`
