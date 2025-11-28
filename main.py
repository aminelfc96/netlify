from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Task 2 - Deployed in render web service</h1>"


@app.route('/hello')
def submit():
    return f"<p>Hello</p>"

if __name__ == '__main__':
    app.run(debug=True)