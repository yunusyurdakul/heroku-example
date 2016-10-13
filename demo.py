from flask import Flask
from flask import render_template
from flask import request
from algorithm import _findElementsBetween

import yaml
import string

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

		input3 = request.form['input3']
		input3 =  [str(x) for x in input3.splitlines()]
		app.logger.debug(input3)
		print 'input3: ' + str(input3)

		result = _findElementsBetween(int(input1), int(input2), input3)
		print result

		return render_template('compute.html', result=result)
