import random
from flask import Flask, request
import requests
from youtubedl import find_ydl_url

app = Flask(__name__)
#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/youtube", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        find_audio_url()
        print(output)
    return "ok", 200

if __name__ == "__main__":
    app.run(debug=True)
