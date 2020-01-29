from user_db import *
from flask import Flask, render_template, request, redirect
import json, requests
from flask_mail import Mail, Message	

app = Flask(__name__)

app.config.update(dict(
	DEBUG = True,
	MAIL_SERVER = 'smtp.gmail.com',
	MAIL_PORT = 587,
	MAIL_USE_TLS = True,
	MAIL_USE_SSL = False,
	MAIL_USERNAME = 'danilavajda@gmail.com',
	MAIL_PASSWORD = '9700170mts',
))

mail = Mail(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']

		add_user(name, email, message)

		msg = Message("Thank you for your message!",
					  sender="danilavajda@gmail.com",
					  recipients=[request.form['email']])
		msg.body = "text"
		mail.send(msg)

		submitted = True
		
		return render_template("landing.html", submitted = submitted)
	
	else:

		return render_template('landing.html')

@app.route('/Boston', methods = ['GET', 'POST'])
def boston():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']

		add_user(name, email, message)

		msg = Message("Thank you for your message!",
					  sender="danilavajda@gmail.com",
					  recipients=[request.form['email']])
		msg.body = "text"
		mail.send(msg)
		
		submitted = True

		return render_template("boston.html", submitted = submitted)

	else:
		
		return render_template('boston.html')

@app.route('/FV', methods = ['GET', 'POST'])
def fv():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']

		add_user(name, email, message)

		msg = Message("Thank you for your message!",
					  sender="danilavajda@gmail.com",
					  recipients=[request.form['email']])
		msg.body = "text"
		mail.send(msg)
		
		submitted = True
		
		return render_template("FV.html", submitted = submitted)

	else:

		return render_template('FV.html')

@app.route('/Albania', methods = ['GET', 'POST'])
def albania():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']

		add_user(name, email, message)

		msg = Message("Thank you for your message!",
					  sender="danilavajda@gmail.com",
					  recipients=[request.form['email']])
		msg.body = "text"
		mail.send(msg)
		
		submitted = True
		
		return render_template("Albania.html", submitted = submitted)

	else:

		return render_template('Albania.html')



if __name__ == '__main__':
	app.run(debug=True)