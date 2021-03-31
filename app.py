from flask import Flask
from twilio.twiml.voice_response import Play, VoiceResponse
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def answer_call():
    # Put your logic here
    # Use requests (or something else)
    # to grab an MP3 URL from an API/RSS Feed/whatever
    # for now, we just hard-code url with a random song
    url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3'
    
    response = VoiceResponse()
    response.play(url)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)