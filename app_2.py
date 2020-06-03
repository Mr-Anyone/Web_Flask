from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        user = request.form['nm']

        return "user"
    else:
        print("Yo Someone is not doing something ")
        return render_template("Talk.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0") #Running on that such that when the network could access