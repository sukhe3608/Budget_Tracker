import json
import os 

DATA_PATH = 'data/budget.json'

def load_data():
    if not os.path.exists(DATA_PATH):
        return {"income": 0, "expenses": []}
    with open(DATA_PATH, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_PATH, 'w') as file:
        json.dump(data, file, indent=4)