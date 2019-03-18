from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello/<name>")
def func(name):
    return f'hello {name}'



@app.route('/time')
def time():
    now = datetime.datetime.now()
    return str(now)
if __name__ == '__main__':
    app.run(debug=True)