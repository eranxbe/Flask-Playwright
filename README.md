# Flask Playwright Test Automation

This project is a combination of knowledge in test automation, as well as self-study of python, combined together to create a flask application that can be used for web and API testing.

## Installation and Usage

To install and use flask-playwright follow these steps:
  1. Clone the repository 
  2. Install the requirements.txt: `pip install -r requirements.txt` 
  3. To run flask server app(./app): `python -m flask run --debugger`
  4. To run pytest-playwright tests (./test-automation): `python -m pytest -v`
  5. Allure reports system is implemented (can be seen at pytest.ini file), to access reports(./test-automation): `allure serve /reports`

## Endpoints

The app contains several endpoints that can be used for CRUD operations on a People model, as well as a form to perform UI tests.

## Test Automation

The test automation module contains an implementation created as a modular approach that helps maintain the code and keeps it simple.

## Future Plans

In the future, I plan on implementing other features such as React, CI/CD integration, and whatever will suit this project, so I'll be happy to accept suggestions and improvement ideas.

Thank you! :)
