from flask import Flask
from flask import render_template
from flask import request
from algorithm import _findElementsBetween

import yaml

app = Flask(__name__)

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/compute', methods=['GET', 'POST'])
def compute():
	if request.method == 'GET':
		app.logger.debug('lol')
		return render_template('compute.html')
	else:
		input1 = request.form['input1']
		app.logger.debug(input1)
	
		print 'input1: ' + input1

		input2 = request.form['input2']
		app.logger.debug(input2)
		print 'input2: ' + input2

		result = _findElementsBetween(int(input1), int(input2), [10,'yunus',2,3,4,5,6])
		print result

		return render_template('compute.html', result=result)
