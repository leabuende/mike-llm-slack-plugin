
from flask import Flask, Response, jsonify, request                                                                                                                                                                          
from slackeventsapi import SlackEventAdapter
import os
from threading import Thread
from slack import WebClient
import json

from services.projectManagementService import projectManagementService

# This `app` represents your existing Flask app
app = Flask(__name__)

greetings = ["hi", "hello", "hello there", "hey"]
status_commands = ["status"]
ticket_commands = ["ticket", "give me work", "what can I do"]


SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
slack_token = os.environ['SLACK_BOT_TOKEN']
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

slack_client = WebClient(slack_token)

@app.route("/")
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}


slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/slack/events", app
)  

@app.route("/post-message", methods = ['POST'])
def post_messsage():
    data = request.get_json()
    message = data['message']
    def send_reply(message):
        slack_client.chat_postMessage(channel='C062XM2M94P', text=message)
    thread = Thread(target=send_reply(message))
    thread.start()
    return Response(status=200)


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        user_id = message["user"]
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]
            print(command)
            # Insert logic here
            if any(item in command.lower() for item in greetings): # Test command
                message = (
                    "Hello <@%s>! :tada:"
                    % message["user"]  # noqa
                )
            if any(item in command.lower() for item in status_commands):
                message = projectManagementService.getStatus(user=user_id)
            if any(item in command.lower() for item in ticket_commands):
                message = projectManagementService.getAvailableTicket(message=command, user=user_id)
            slack_client.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)
