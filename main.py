from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return f"<title>Mohamed Amine Taieb</title><h1>Task 2 - Deployed in render web service</h1>"


@app.route('/hello')
def submit():
    return jsonify(message="Hello")

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=10000)

