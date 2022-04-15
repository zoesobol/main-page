from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>This is supposed to be my home page.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
