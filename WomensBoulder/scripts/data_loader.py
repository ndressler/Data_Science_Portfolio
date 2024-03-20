import json
import os


def load_data():
    json_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'data.json')
    try:
        with open(json_data_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: data.json not found")
        exit(1)
    except json.JSONDecodeError:
        print("Error: data.json is not valid JSON")
        exit(1)
