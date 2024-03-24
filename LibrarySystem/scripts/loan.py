import secrets
from datetime import datetime, timedelta
from scripts.book import BookList
from scripts.user import UserList
from scripts.functions import save_to_csv, load_from_csv
from typing import Dict, List

class Loans:
    """A class to represent a loan in the library system"""
    def __init__(self,loan_code: str,  book_id: str, username: str, book_list: BookList, user_list: UserList) -> None:
        self._loan_code: str = loan_code
        self._book_list = book_list
        self._user_list = user_list
        self._book_id: str = book_id
        self._username: str = username
        self._loan_date: datetime = datetime.today()
        self._return_date: datetime = datetime.today() + timedelta(days=10)

    @property
    def loan_code(self) -> str:
        return self.loan_code

    @loan_code.setter
    def loan_code(self, loan_code: int) -> None:
        self.loan_code = loan_code

    @property
    def book_id(self) -> str:
        return self._book_id

    @book_id.setter
    def book_id(self, book_id: str) -> None:
        if book_id not in self._book_list.get_books():
            raise ValueError(f"The Book ID {book_id} is not in the library's collection.")
        else: self._book_id = book_id

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        if username not in self._user_list.get_users():
            raise ValueError(f"The username {username} is not registered at the library.")
        self._username = username

    @property
    def loan_date(self) -> datetime:
        return self._loan_date

    @loan_date.setter
    def loan_date(self, loan_date):
        if isinstance(loan_date, datetime):
            self._loan_date = loan_date
        else:
            self._loan_date = datetime.strptime(loan_date, "%d-%m-%Y %H:%M:%S")
        self._return_date = self._loan_date + timedelta(days=10)

    @property
    def return_date(self) -> datetime:
        return self._return_date

    @return_date.setter
    def return_date(self, return_date: datetime) -> None:
        try:
            self._return_date = datetime.strptime(return_date, "%d-%m-%Y %H:%M:%S")
        except ValueError:
            raise ValueError("Invalid return date format. Please provide a date in the format 'DD-MM-YYY HH:MM:SS'.")

class LoanList:
    """A class to manage loans of the library system"""
    def __init__(self) -> None:
        self.collection: Dict[str, Loans] = {}

    def generate_unique_code(self):
        while True:
            new_code = secrets.token_hex(3)
            if new_code not in self.get_loans():
                return new_code

    def get_loans(self) -> Dict[str, Loans]:
        return self.collection

    def add_loan(self, loan_code: str, book_id: str, username: str, book_list: BookList, user_list: UserList) -> None:
        try:
            if loan_code is None:
                loan_code = self.generate_unique_loan()
            if username not in user_list.get_users().keys() or book_id not in book_list.get_books().keys():
                raise ValueError("User or book not found in the collection.")
            book = book_list.get_books()[book_id]
            if book.get_num_available_copies() <= 0:
                raise ValueError(f"The book with ID {book_id} is currently not available.")
            new_loan = Loans(book_id, username, book_list, user_list)
            self.collection[new_loan.loan_code] = new_loan
            book.set_num_available_copies(book.get_num_available_copies() - 1)
        except ValueError as e:
            raise ValueError(f"Invalid input. Please try again with valid data. Error: {e}")

    def find_loan(self, data: str, search_type: str) -> List[str]:
        data = data.lower()
        search_type = search_type.lower()

        search_map = {
            "username": lambda username: data in username.lower(),
            "book_id": lambda book_id: data in book_id.lower()
            }

        if search_type not in search_map:
            raise KeyError("Invalid search type. Please provide a valid search type of either 'username' or 'book_id'.")
        return [loan_code for loan_code, loan_item in self.collection.items() if data.lower() in getattr(loan_item, search_map[search_type]).lower()]

    def remove_loan(self, book_id: str, loan_code: str, book_list: BookList) -> None:
        book = book_list.collection.get(book_id)
        if not book:
            raise ValueError(f"The book with ID {book_id} is not in the library's collection.")
        try:
            del self.collection[loan_code]
            book.set_num_available_copies(book.get_num_available_copies() + 1)
        except KeyError:
            print(f"Input error. The loan number {loan_code} is already no longer active.")

    def late_loans(self) -> None:
        late_loans = [k for k, v in self.collection.items() if v.return_date < datetime.now()]
        if not late_loans:
            print("There are no currently late loans.")
        else:
            print(f"Here are the codes for overdue loans:\n{late_loans}")

    def total_loans(self) -> int:
        return len(self.collection)

    def loan_save_to_csv(self):
        data = []
        for loan_code, loan in self.collection.items():
            data.append({
                'loan_code': loan_code,
                'book_id': loan.book_id,
                'username': loan.username,
                'loan_date': loan.loan_date.strftime("%d-%m-%Y %H:%M:%S"),
                'return_date': loan.return_date.strftime("%d-%m-%Y %H:%M:%S"),
            })
        save_to_csv(data, 'data/loans.csv', ['loan_code', 'book_id', 'username', 'loan_date', 'return_date'])

    def loan_load_from_csv(self, book_list, user_list):
        data = load_from_csv('data/loans.csv')
        for row in data:
            loan = Loans(row['book_id'], row['username'], book_list, user_list)
            loan.loan_date = row['loan_date']
            loan.return_date = datetime.strptime(row['return_date'], "%d-%m-%Y %H:%M:%S")
            self.collection[row['loan_code']] = loan
