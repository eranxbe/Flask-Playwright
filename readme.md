This project is a combination of knowledge in test automation, as well as self-study of python, combined together to crete a flask application that can be used for web and api testing.

To install and use flask-playwright follow these steps:
	1. clone the repository
	2. install the requirements.txt: pip install -r requirements.txt
	3. since this project is still locally runned, run on different terminals these commands:
		flask server (./app): python -m flask run --debugger
		pytest-playwright tests(./test-automaiton): python -m pytest -v


The app contains several endpoints that can be used for CRUD operations on a People model, as well as a form to perform UI tests. The test automation module contains an implementation created as a modular approach that helps maintaining the code and keeping it simple. 

In the future I plan on implementing other features such as react, CI/CD integration and whatever will suit this project, so I'll be happy to accept suggestions and improvement ideas.

Thank you! :)
