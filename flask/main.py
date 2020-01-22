from flask import Flask
import json

app = Flask(__name__)


@app.route("/item")
def hello():
    return json.dumps({"version": 0, "service": "flask"})
