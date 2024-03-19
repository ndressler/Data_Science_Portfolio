import json

def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: data.json not found")
        exit(1)
    except json.JSONDecodeError:
        print("Error: data.json is not valid JSON")
        exit(1)
