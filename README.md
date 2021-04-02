# POC for Twilio

## Installation

- Clone this repo `git clone git@github.com:wbur/call-for-audio.git`
- Get into the new dir: `cd call-for-audio`
- Set up a venv (preferably ~python 3.8) `python3 -m venv venv`
- Activate venv: `. venv/bin/activate`
- Install via requirements: `pip install -r requirements.txt`
- Start the server: `python app.py`
- API should be live at `http://127.0.0.1:5000/`

## Add project / deploy to Heroku

- Make sure you have a Heroku account
- Create a new Heroku project with <HEROKU PROJECT NAME>
- Get into the new (local) dir: `cd call-for-audio`
- Log in to Heroku: `heroku login -i`
- Add remote: `heroku git:remote -a <HEROKU PROJECT NAME>`
- Push to Heroku: `git push heroku master`
- More info at: https://stackabuse.com/deploying-a-flask-application-to-heroku/

## Connecting to Twilio

- Sign up for Twilio
- Strongly suggest a paid, non-trial account (it's pretty darn cheap)
- Buy a phone number
- Use your new Heroku URL as the Twilio webhook
- Try it out ny calling your new number!
- This tutorial should help: https://www.twilio.com/docs/voice/tutorials/how-to-respond-to-incoming-phone-calls-python
