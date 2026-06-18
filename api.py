from flask import Flask, jsonify
from database import get_all_devices

app = Flask(__name__)

@app.route("/")
def devices():
    response = jsonify(get_all_devices())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)