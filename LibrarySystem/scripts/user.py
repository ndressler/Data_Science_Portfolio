from scripts.functions import parse_date, save_to_csv, load_from_csv
from typing import Dict, List
import re

class Users:
    """A class to represent a user of the library system"""
    def __init__(self, username: str, firstname: str, surname: str, house_number: str,
                 street_name: str, postcode: str, email_address: str, date_birth: str) -> None:
        self._username: str = username
        self._firstname: str = firstname
        self._surname: str = surname
        self._house_number: str = house_number
        self._street_name: str = street_name
        self._postcode: str = postcode
        self._email_address: str = email_address
        self._date_birth: str = date_birth

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, new_username: str) -> None:
        if not new_username:
            raise ValueError("Username cannot be empty")
        self._username = new_username

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, new_firstname: str) -> None:
        if not new_firstname:
            raise ValueError("Firstname cannot be empty")
        self._firstname = new_firstname

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, new_surname: str) -> None:
        if not new_surname:
            raise ValueError("Surname cannot be empty")
        self._surname = new_surname


    @property
    def house_number(self) -> str:
        return self._house_number

    @house_number.setter
    def house_number(self, new_house_number: str) -> None:
        if not new_house_number.isdigit():
            raise ValueError("New house number must contain only numbers.")
        self._house_number = new_house_number

    @property
    def street_name(self) -> str:
        return self._street_name

    @street_name.setter
    def street_name(self, new_street_name: str) -> None:
        self._street_name = new_street_name

    @property
    def postcode(self) -> str:
        return self._postcode

    @postcode.setter
    def postcode(self, new_postcode: str) -> None:
        if not new_postcode.isdigit():
            raise ValueError("New postcode must contain only numbers, without letters or special characters.")
        self._postcode = new_postcode

    @property
    def email_address(self) -> str:
        return self._email_address

    @email_address.setter
    def email_address(self, new_email_address: str) -> None:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, new_email_address):
            raise ValueError(f"Invalid email address: {new_email_address}")
        self._email_address = new_email_address

    @property
    def date_birth(self) -> str:
        return self._date_birth

    @date_birth.setter
    def date_birth(self, new_date_birth: str) -> None:
        parse_date(new_date_birth)
        self._date_birth = new_date_birth

    def __str__(self) -> str:
        return f"User({self.username}, {self.firstname}, {self.surname}, {self.house_number}, {self.street_name}, {self.postcode}, {self.email_address}, {self.date_birth})"

class UserList:
    """A class to manage users of the library system"""
    def __init__(self) -> None:
        self._collection: Dict[str, Users] = {}

    def get_users(self):
        return self._collection

    def add_user(self, username: str, firstname: str, surname: str, house_number: str, street_name: str,
                 postcode: str, email_address: str, date_birth: str) -> None:
        if username in self._collection:
            raise ValueError(f"User with username {username} already exists.")
        new_user = Users(username, firstname, surname, house_number,
                         street_name, postcode, email_address, date_birth)
        self._collection[new_user.username] = new_user

    def update_user(self, username: str, firstname: str, surname: str, house_number: str,
                    street_name: str, postcode: str, email_address: str, date_birth: str) -> None:
            if username in self._collection:
                user = self._collection[username]
                user.username = username
                user.firstname = firstname
                user.surname = surname
                user.house_number = house_number
                user.street_name = street_name
                user.postcode = postcode
                user.email_address = email_address
                user.date_birth = date_birth
            else:
                raise ValueError(f"No user found with username {username}")

    def find_user(self, data: str, search_type: str) -> List[int]:
        data = data.lower()
        search_type = search_type.lower()

        search_mapping = {
            "username": lambda user: data in user.username,
            "firstname": lambda user: data in user.firstname.lower(),
            "surname": lambda user: data in user.surname.lower()}

        if search_type not in search_mapping:
            raise KeyError("Invalid search type. Please provide a valid search type of either 'username, firstname or surname'.")

        user_matches = [(user, user_item.firstname, user_item.surname) for user, user_item in self._collection.items() if search_mapping[search_type](user_item)]
        return user_matches

    def remove_user(self, firstname: str) -> str:
        firstname = firstname.lower()
        user_matches = [username for username, user in self._collection.items() if user.firstname and user.firstname.lower() == firstname]
        if len(user_matches) == 1:
            username_delete = user_matches[0]
            del self._collection[username_delete]
            return f"User '{firstname}' has been deleted from the collection."
        elif len(user_matches) > 1:
            make_list = '\n'.join(user_matches)
            username_delete = input(f"The following users matched the first name inputed:\n{make_list}\nPlease enter the username that you wish to delete: ")
            del self._collection[username_delete]
            return f"User '{username_delete}' has been removed from the collection."
        raise ValueError(f"User with first name '{firstname}' not found in the collection.")

    def total_users_collection(self) -> int:
        return len(self._collection)

    def get_user(self, username: str) -> Users:
        if username not in self._collection:
            raise ValueError(f"Input error. Username {username} not found.")
        return self._collection[username]

    def user_save_to_csv(self):
        data = []
        for username, user in self._collection.items():
            data.append({
                'username': user.username,
                'firstname': user.firstname,
                'surname': user.surname,
                'house_number': user.house_number,
                'street_name': user.street_name,
                'postcode': user.postcode,
                'email_address': user.email_address,
                'date_birth': user.date_birth,
            })
        save_to_csv(data, 'data/users.csv', ['username', 'firstname', 'surname', 'house_number', 'street_name', 'postcode', 'email_address', 'date_birth'])

    def user_load_from_csv(self):
        data = load_from_csv('data/users.csv')
        for row in data:
            self.add_user(row['username'], row['firstname'], row['surname'], row['house_number'], row['street_name'], row['postcode'], row['email_address'], row['date_birth'])
