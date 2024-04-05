import api2 as p
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify(message='Hello, World!')

@app.route('/rhyme')
def rhyme_endpoint():
    string = request.args.get('string')
    output = p.rhyme(string)
    return jsonify(output)

@app.route('/define')
def define_endpoint():
    string = request.args.get('string')
    output = p.define(string)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')



