from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main_page():
    """
    To Make A Two Button
    <p><input type="submit" name = "b1" value="Submit"></p>
    <p><input type="submit" name="b1" value="Login_In_Page"></p>

    Type would have change!
    PS: THIS SHOULD BE UNDER FORM TAG LOOK AT TALK.HTML FOR MORE TEXT
    """
    if request.method == "POST": # Checking if the user is posting or getting
        user = request.form['nm']
        if request.form['b1'] == "Login_In_Page": # This is how you would have a button define the name as b1 then set the vaule meaning if you press the button
            print("Hey")
            return redirect(url_for("login")) # Redirecting to that url
        elif request.form['b1'] == "Submit":
            return render_template("Talk.html") # Retruns the same page

    else:
        return render_template("Talk.html") # Render the templete if it is get


"""
These are session, a way to quickly access information mate!!!
As soon as someone leave the session would leave as well mate!!!
"""
app.permanent_session_lifetime = timedelta(minutes=1) #Storing the session data for 5 days, form tiem import time delta
app.secret_key = "HI" #You have to define a secrete key in order to use session

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        """
        This is how you would setup some session data, you have to import session from flask
        This is how you would store data from html that has a input tag with name user and password
        """
        user, passowrd = request.form['user'], request.form['Password'] # You woudl have to do this
        session['user'] = user #Session is a dicentory, deffing the user as the request
        session['password'] = passowrd #Session is a dicentory, deffing the user as the request
        print(session['user'])
        return redirect(url_for("user", user=user))
    else:
        if 'user' in session and 'password' in session: # THis is how you would check if something is in the session
            return redirect(url_for("user", user=session['user']))
        else:
            return render_template("login.html")

@app.route("/<user>")
def user(user):
    '''
    Sessions makes sure you logged in before entering the page
    '''
    if 'user' in session:
        return f"<h1>  Hey You're Logged in. User:  {user}</h1>" # if logged in then print this mesage
    else:
        return redirect(url_for("main_page")) # If not logged in then return to main page
"""
THis is how you would be LOGGING OUT
"""
@app.route("/logout")
def logout():
    session.pop('user', None)
    session.pop('password', None)
    return redirect(url_for("login")) # This is how you would log out


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) #Running on that such that when the network could access