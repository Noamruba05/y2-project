from flask import Flask, jsonify, request, render_template
import random
from database import *

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def home():
	return render_template('home.html',users=query_all())

@app.route('/singup', methods=['GET', 'POST'])
def singup():
  if request.method == 'GET':
    return render_template("singup.html")
  else:
    full_name = request.form['full_name']
    username = request.form['username']
    password = request.form['password']
    bio = request.form['bio']
    if get_user_by_username(username) == None:
      create_user(username,password,full_name,bio)
      return home()
    else:
      return render_template("singup.html", errormsg = "hurrdurr username exists")
      

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template("login.html")
  else:
    username = request.form['username']
    password = request.form['password']
    create_user(username,password,full_name,bio)
    return home()

@app.route('/art')
def art():
  return render_template("art.html")


    






if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),debug=True  # Randomly select the port the machine hosts on.
	)