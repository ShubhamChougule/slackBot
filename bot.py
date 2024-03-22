import os
import re  # Import the re module for regular expressions
from slack_bolt import App

# Set your Slack Bot User OAuth Token directly as an environment variable
slack_bot_token = "xapp-1-A06QVPQ3CBC-6858528695841-408e14159a4381ce2c6185920bcd4efccbe48d83ed935b8eca38a516a3d123ce"

app = App(token=slack_bot_token)

@app.command("/twotruthsandalie")
def start_game(ack, say, command):
    ack()
    say(f"Hey <@{command['user_id']}>! Let's play Two Truths and a Lie.\nSend me your two truths and a lie separated by commas.")

@app.message(re.compile("two truths and a lie", re.IGNORECASE))
def receive_statements(message, say):
    say("Send me your two truths and a lie separated by commas.")

@app.message(re.compile("guess the lie", re.IGNORECASE))
def guess_the_lie(message, say):
    statements = message["text"][message["text"].index(':')+1:].strip()
    lie = random.choice(statements.split(',')).strip()
    say(f"I think the lie is: {lie}")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
