from flask import Flask
from flask import render_template
app = Flask(__name__)
from flask import Flask, jsonify
# Python Dictionary
data = {
    "name": "Jack",
    "age": 99,
    "city": "My house",
    "is_student": False,
    "hobbies": ["cooking", "coding"]
}

@app.route("/")
def hello_world():
    return "<marquee><p>Hello, ITE!</p></marquee>"

@app.route("/jason")
def saluda():
    return data

@app.route("/json")
def saludajson():
    return jsonify(data)

@app.route("/pagina")
@app.route("/pagina/<name>")
def pagina(name=None):
    return render_template('pagina.html', person=name)