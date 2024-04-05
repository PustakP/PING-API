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
    return jsonify(output=output)

@app.route('/define')
def define_endpoint():
    string = request.args.get('string')
    output = p.define(string)
    return jsonify(output=output)

@app.route('/synonym')
def synonym_endpoint():
    string = request.args.get('string')
    output = p.synonym(string)
    return jsonify(output=output)

@app.route('/antonym')
def antonym_endpoint():
    string = request.args.get('string')
    output = p.antonym(string)
    return jsonify(output=output)

@app.route('/joke')
def joke_endpoint():
    string = request.args.get('string')
    output = p.joke(string)
    return jsonify(output=output)

@app.route('/owo')
def owo_endpoint():
    string = request.args.get('string')
    output = p.owo(string)
    return jsonify(output=output)

@app.route('/celebrity')
def celebrity_endpoint():
    string = request.args.get('string')
    output = p.celebrity(string)
    return jsonify(output=output)

@app.route('/chatgpt')
def chatgpt_endpoint():
    initialMessage = request.args.get('initialMessage')
    exampleString = request.args.get('exampleString')
    expectedOutput = request.args.get('expectedOutput')
    string = request.args.get('string')
    output = p.chatgpt(initialMessage, exampleString, expectedOutput, string)
    return jsonify(output=output)

@app.route('/anime_suggestion')
def anime_suggestion_endpoint():
    string = request.args.get('string')
    output = p.anime_suggestion(string)
    return jsonify(output=output)

@app.route('/adjective')
def adjective_endpoint():
    string = request.args.get('string')
    output = p.adjective(string)
    return jsonify(output=output)

@app.route('/pickupLine')
def pickupLine_endpoint():
    string = request.args.get('string')
    output = p.pickupLine(string)
    return jsonify(output=output)

@app.route('/astrologer')
def astrologer_endpoint():
    string = request.args.get('string')
    output = p.astrologer(string)
    return jsonify(output=output)

if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')
