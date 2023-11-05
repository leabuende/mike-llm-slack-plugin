import requests
import os
from dotenv import load_dotenv
from data.team import getMemberByID
load_dotenv()

url = os.environ.get("API_URL")

class projectManagementService():
    def getAvailableTicket(message, user):
        user_profile = getMemberByID(user)
        payload = "{\"query\": \"I'm a "+ user_profile["job"]+". What cards can I work on ? Prioritize the one's in the current sprint backlog. Suggest ongoing tickets I could help with.\"}"
        response = requests.request("POST", url, data = payload).text.replace("\\n","\n")[1:-1]
        message = str("Hey there <@" + str(user) + "> ! I've got some work for you :muscle: :sunglasses: \n" + str(response))
        return (message)
    def getStatus(user):
        payload = "{\"query\": \" Write me a status report on the ongoing cards, the cards left on the sprint backlog and recently completed cards. Explain which cards should take priority.\"}"
        response = requests.request("POST", url, data = payload).text.replace("\\n","\n")[1:-1]
        message = str("Good work team ! Here's your daily status report \n" + str(response))
        return (message)