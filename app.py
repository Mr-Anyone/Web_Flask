from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
'''
This is the tutorial that I followed:
https://www.youtube.com/watch?v=xIgPMguqyws
Currently in https://www.youtube.com/watch?v=4nzI4RKwb5I
'''

@app.route('/')# THis is how you would direct the link, it means that www...../ is going to lad hello world function
def hello_world():
    return "<h1> Hi there You can suck my penis bitches! </h1> <p> This is from someone who is handsome</p>"

@app.route('/yo')# This is the same as above but it would load the yo function when you're going to www...../penis
def yo():
    return "<p> What is up this is the yo function </p>"

@app.route("/<name>") # THis would means that when you type anything that is not the above it will pass in name as parameter to the function user
def user(name):
    return "Hi " + name

@app.route("/admin")
def admin():
    return redirect(url_for("yo")) # This will redirect to the yo function if you type website/admin

@app.route("/what")
def what():
    return redirect(url_for("user", name="Hey")) # Redirect to the function user and pass in the parameter name as Hey

"""
This is how you would render_templete
"""
@app.route("/html")
def html():
    return render_template("index.html", name="name") # When in the rout it will load the html, passing in the variable name in the html file
# Look at index html and find {{name}} it is pass there

@app.route("/1")
def one():
    return render_template("1.html", variable=3) # redirecting to the page called 1.html

"""
This will be Template Inheritance
"""
@app.route("/2")
def two():
    return render_template("new.html") # Go to this fiel and bas.html to learn it=

"""
This is HTTP methods
The get method is  send information  to the website (not secure)
The Post method secure the get method

Goging to dispaly information to another page 
"""
@app.route("/login", methods=["POST", "GET"])# This means that the page could use these method in Flask when you open /login page
def login(): # Please import the request to check if the user is posting information or asking for html
    if request.method == "POST":
        user = request.form["nm"] # Go and read the login.html and there is something that is define as name="nm" after user post it to you will have it uder the user thing
        return redirect(url_for("loged", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def loged(usr):
    print(usr)
    return "<h1>" + usr + "</h1>"





if __name__ == '__main__':
    app.run()# Running the app
