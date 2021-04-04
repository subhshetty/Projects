from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def helloWorld(name):
    return f"<h1> Hello {name}!</h1>"