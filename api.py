from flask import Flask, jsonify
from database import get_all_devices
import subprocess

app = Flask(__name__)

@app.route("/")
def devices():
    response = jsonify(get_all_devices())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/nmap/<ip>", methods=["GET"])
def nmap_scan(ip):
    try:
        result = subprocess.run(
            ["nmap", "-T5", ip],
            capture_output=True,
            text=True,
        )
        response = jsonify({"output": result.stdout, "error": result.stderr})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as err:
        response = jsonify({"error": str(err), "output": ""})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)