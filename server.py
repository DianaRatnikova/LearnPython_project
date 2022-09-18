from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world from server.py!"

if __name__ == "__main__":
    app.run(debug=True)