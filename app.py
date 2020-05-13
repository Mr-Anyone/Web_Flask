from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Hi there You can suck my penis bitches! </h1> <p> This is from someone who is handsome</p>"


if __name__ == '__main__':
    app.run()
