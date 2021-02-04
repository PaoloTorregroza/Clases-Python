from flask import Flask
import utils

app = Flask(__name__)

dataBase = utils.readJson()


@app.route("/")
def hello_world():
    return "<h1>Hola</h1>"


@app.route("/persona/<int:id>")
def get_person(id):
    return dataBase[id]
