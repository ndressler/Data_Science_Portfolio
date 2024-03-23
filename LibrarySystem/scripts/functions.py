from dateutil.parser import parse
from datetime import datetime
import csv

def parse_date(date_string):
    while True:
        try:
            return parse(date_string, dayfirst=True).date()
        except:
            return "Invalid input. Remember to use the European date format."

def get_valid_input(prompt, validation_function, error_message):
    while True:
        user_input = input(prompt).strip()
        if validation_function(user_input):
            return user_input
        else:
            print(error_message)

def get_valid_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            day, month, year = map(int, date_input.split('-'))
            date_object = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
            return date_object.strftime('%d-%m-%Y')
        except ValueError:
            print("Invalid input. Remember to use the date format (DD-MM-YYYY).")
            
def save_to_csv(data, filename, fieldnames):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

def load_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
