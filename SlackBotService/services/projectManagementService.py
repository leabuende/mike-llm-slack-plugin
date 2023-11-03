import requests
import os
from dotenv import load_dotenv
from data.team import getMemberByID
load_dotenv()

url = os.environ.get("API_URL")

def linkFormatter(text):
    doc = etree.fromstring(markdown.markdown(body_markdown))
    for link in doc.xpath('//a'):
        
        print link.text, link.get('href')


class projectManagementService():
    def getAvailableTicket(message, user):
        user_profile = getMemberByID(user)
        payload = "{\"query\": \"I'm a "+ user_profile["job"]+". What cards can I work on ? Prioritize the one's in the current sprint backlog. Suggest ongoing tickets I could help with.\"}"
        response = requests.request("POST", url, data = payload).text.replace("\\n","\n")[1:-1]

        message = str("Hey there <@" + str(user) + "> ! I've got some work for you :muscle: :sunglasses: \n" + str(response))
        return (message)
    def getStatus(user):
        print(getMemberByID(user)["job"])
        return ("This is the status !")