from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT'])
def index():
    data = dict(message="success")
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
