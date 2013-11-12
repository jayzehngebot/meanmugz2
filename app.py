import os, datetime, lob
from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template
app = Flask(__name__)   # create our flask app

lob.api_key = 'test_ac623e7bdd0d113f7824746f5d239b0bf1a'

objects = {}
objects['mug'] = {
		'image' : 'mug.gif',
		'user' : 'gnarly',
		'available' : True	
}


# this is our main page
@app.route("/", methods=["GET","POST"])
def index():
	if request.method =="POST":

		user_name = request.form.get('user_name')

		app.logger.debug(user_name) 

		address_line1 = request.form.get('address01')
		address_line2 = request.form.get('address02')
		city = request.form.get('city')
		state = request.form.get('state')
		zipcode = request.form.get('zip')

		address = lob.Address.create(name=user_name, address_line1=address_line1, address_line2=address_line2,
		                             address_city=city, address_state=state, address_country='US',
		                             address_zip=zipcode)

		print address.to_dict()

		return render_template("success.html")

	else:
	# pisa.CreatePDF("main.html","main.pdf")
		
        # render the template, pass in the animals dictionary refer to it as 'animals'
		return render_template("main.html")

# this is the 2nd route - can be access with /page2
@app.route("/verify-address")
def page2():
	return "<h2>Welcome to page 2</h2><p>This is just amazing!</p>"


# new route will accept both a GET and POST request from the client (web browser)
@app.route("/formzone", methods=["GET","POST"])
def simpleform():

	# Did the client make a POST request?
	if request.method == "POST":

		# get the form data submitted and store it in a variable
		user_name = request.form.get('user_name', 'Tim Berners-Lee')

		# return custom HTML using the user submitted data
		return "<html><body><h3>Hello %s! What an interesting name.</h3><br><a href='/form'>back to form</a></body><html>" % user_name

	else:

		# client made a GET request for '/form'
		# return a simple HTML form that POSTs to itself
		return """<html><body>
		<form action="/form" method="POST">
			What's your name? <input type="text" name="user_name" id="user_name"/>
			<input type="submit" value="submit it"/>
		</form>
		</body></html>"""

# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)