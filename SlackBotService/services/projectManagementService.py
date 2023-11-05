import requests
import os
from dotenv import load_dotenv
from data.team import getMemberByID
load_dotenv()

url = os.environ.get("API_URL")

class projectManagementService():
    def getAvailableTicket(message, user):
        user_profile = getMemberByID(user)
        payload = "{\"query\": \"I'm a "+ user_profile["job"]+". What cards can I work on ? Prioritize the one's in the current sprint backlog. Suggest ongoing tickets I could help with. Do not greet me, instead start your message with 'Here's some work for you'.\"}"
        response = requests.request("POST", url, data = payload).text.replace("\\n","\n")[1:-1]
        message = str("Hey there <@" + str(user) + "> ! :muscle: :sunglasses: \n" + str(response))
        return (message)
    def getStatus(user):
        payload = "{\"query\": \" Write me a status report on the ongoing cards, the cards left on the sprint backlog and recently completed cards, using the card name and link, and desc (stands for description). Explain in your assessment which cards should take priority, what challenges you think could be encountered to complete the card, and what team you think should take care of it (Engineering, design, business, etc...). End with a general assessment of the productivity of the team. Start with 'Status report of the day : DD/MM/YYYY', and end without offering further assistance, and instead with 'Good job team !'\"}"
        response = requests.request("POST", url, data = payload).text.replace("\\n","\n")[1:-1]
        message = str(response)
        message = message.replace('\"','"')
        return (message)
    def qa(user, query):
        payload = "{\"query\": \"" +query+ " \"}"
        response = requests.request("POST", url, data = payload).text.replace("\\n","\n")[1:-1]
        message = str(response)
        return (message)