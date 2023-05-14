from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)

@app.route("/<token>/<chat_id>/<text>")
def hello_world(token, chat_id, text):
    try:
        request_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
        response = requests.get(request_url)
        return make_response(jsonify({}), 200)
    except Exception as e:
        return make_response(jsonify({'error': e}), 500)

app.run()