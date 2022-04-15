from flask import Flask
app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return {
        "status": "success",
        "message": "This is supposed to be my home page."
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
