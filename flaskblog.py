from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello Flask!</h1>"

@app.route("/about")
def about():
    return "<h6>About Page</h6>"


if __name__ == '__main__':
    app.run(debug=True)
