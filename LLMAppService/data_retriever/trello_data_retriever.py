import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

trello_key = os.environ.get("TRELLO_KEY")
trello_token = os.environ.get("TRELLO_TOKEN")
board_id = os.environ.get("TRELLO_BOARD_ID")


def send_request():
    res = requests.get('https://api.trello.com/1/boards/'+ board_id +'/lists?key=' + trello_key + '&token=' + trello_token)
    response = json.loads(res.text)
    with open('../data/trello_board.jsonl', 'w') as datafile:
        for list_item in response:
            cards_res = requests.get('https://api.trello.com/1/lists/'+ list_item["id"] +'/cards?key=' + trello_key + '&token=' + trello_token)
            cards_array = json.loads(cards_res.text)
            entry = {'list': list_item["name"], 'cards': cards_array}
            json.dump(entry, datafile)
            datafile.write('\n')

send_request()
    


