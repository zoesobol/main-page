from flask import Flask
app = Flask(__name__, static_folder='frontend/build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api/hello")
def hello():
    return {
        "status": "success",
        "message": "This is supposed to be my home page."
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
