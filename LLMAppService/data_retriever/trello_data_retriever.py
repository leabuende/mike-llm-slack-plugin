import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

trello_key = os.environ.get("TRELLO_KEY")
trello_token = os.environ.get("TRELLO_TOKEN")
board_id = os.environ.get("TRELLO_BOARD_ID")

def format_previous_data():
    obj = []
    with open('../data/trello_board.jsonl') as f:
        for line in f:
            data = json.loads(line)
            obj.append(data)
    return obj

def compare_lists(old, new):
    cards_to_check = new["cards"]
    identical_found = False
    if(len(old) > 0):
        for item in old:
            data = json.loads(item["list"])
            if cards_to_check == data["cards"]:
                identical_found = True
                break
    return identical_found

def send_request():
    res = requests.get('https://api.trello.com/1/boards/'+ board_id +'/lists?key=' + trello_key + '&token=' + trello_token)
    response = json.loads(res.text)
    with open('../data/trello_board.jsonl', 'a') as datafile:
        for list_item in response:
            cards_res = requests.get('https://api.trello.com/1/lists/'+ list_item["id"] +'/cards?key=' + trello_key + '&token=' + trello_token)
            cards_array = json.loads(cards_res.text)
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            list_object =  {"name": list_item["name"], "last_updated": now, "cards": cards_array}
            entry = {"list": str(list_object)}
            json.dump(entry, datafile)
            datafile.write('\n')

send_request()
    


