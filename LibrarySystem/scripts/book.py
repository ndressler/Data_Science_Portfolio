import random
from typing import Dict, List
from scripts.functions import parse_date, save_to_csv, load_from_csv

class Books:
    """A class to represent a book in the library system"""
    def __init__(self, book_id: int, title: str, author: str, year: int, publisher: str, total_num_copies: int,
                 num_available_copies: int, publication_date: str) -> None:

        if not title or not author or not publisher or not publication_date:
            raise ValueError("Title, author, publisher, and publication date cannot be empty")
        if not isinstance(year, int) or not isinstance(total_num_copies, int) or not isinstance(num_available_copies, int):
            raise ValueError("Year, total number of copies, and number of available copies must be integers")

        self._book_id: int = book_id
        self._title: str = title.lower()
        self._author: str = author.lower()
        self._year: int = year
        self._publisher: str = publisher.lower()
        self._total_num_copies: int = total_num_copies
        self._num_available_copies: int = num_available_copies
        self._publication_date: str = publication_date

    @property
    def book_id(self) -> int:
        return self._book_id

    @book_id.setter
    def book_id(self, book_id: int) -> None:
        self._book_id = book_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        if not title:
            raise ValueError("Title cannot be empty")
        self._title = title.lower()

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        if not author:
            raise ValueError("Author cannot be empty")
        self._author = author.lower()


    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        if not str(year).isdigit():
            raise ValueError("Invalid input. Year should be a number.")
        self._year = int(year)

    @property
    def publisher(self) -> str:
        return self._publisher

    @publisher.setter
    def publisher(self, publisher: str) -> None:
        if not publisher:
            raise ValueError("Title cannot be empty")
        self._publisher = publisher.lower()

    @property
    def total_num_copies(self) -> int:
        return self._total_num_copies

    @total_num_copies.setter
    def total_num_copies(self, total_num_copies: int) -> None:
        if not str(total_num_copies).isdigit():
            raise ValueError("Invalid input. Total number of copies should be a number.")
        self._total_num_copies = int(total_num_copies)

    @property
    def num_available_copies(self) -> int:
        return self._num_available_copies

    @num_available_copies.setter
    def num_available_copies(self, num_available_copies: int) -> None:
        try:
            self._num_available_copies = int(num_available_copies)
            if self._num_available_copies > self._total_num_copies:
                raise ValueError("Invalid input. Number of available copies cannot be more than total copies.")
        except ValueError:
            raise ValueError("Invalid input. 'Number of available copies' should be a number.")

    @property
    def publication_date(self) -> str:
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date: str) -> None:
        self._publication_date = parse_date(publication_date)

class BookList:
    """A class to manage books in the library system"""
    def __init__(self) -> None:
        self._collection: Dict[int, Books] = {}

    def generate_unique_id(self):
        while True:
            new_id = random.randint(0, 9999)
            if new_id not in self.get_books():
                return new_id

    def get_books(self):
        return self._collection

    def add_book(self, title: str, author: str, year: int, publisher: str, total_num_copies: int,
                 num_available_copies: int, publication_date: str, book_id: int = None) -> None:
        try:
            if book_id is None:
                book_id = self.generate_unique_id()
            new_book = Books(book_id, title, author, year, publisher, total_num_copies, num_available_copies, publication_date)
            self._collection[new_book._book_id] = new_book
        except ValueError as e:
            raise ValueError(f"Invalid input. Please try again with valid data. Error: {e}")

    def update_book(self, book_id: int, title: str, author: str, year: int, publisher: str, total_num_copies: int,
                    num_available_copies: int, publication_date: str) -> None:
            if book_id in self._collection:
                book = self._collection[book_id]
                book.title = title
                book.author = author
                book.year = year
                book.publisher = publisher
                book.total_num_copies = total_num_copies
                book.num_available_copies = num_available_copies
                book.publication_date = publication_date
            else:
                raise ValueError(f"No book found with id {book_id}")

    def find_book(self, data: str, search_type: str) -> List[int]:
        data = data.lower()
        search_type = search_type.lower()

        search_mapping = {
            "title": lambda book: data in book.title.lower(),
            "author": lambda book: data in book.author.lower(),
            "publisher": lambda book: data in book.publisher.lower(),
            "publication date": lambda book: parse_date(data) == parse_date(book.publication_date)
        }

        if search_type not in search_mapping:
            raise KeyError("Invalid search type. Please provide a valid search type of either 'title, author, publisher or publication date'.")

        book_matches = [(book_id, book_item.title) for book_id, book_item in self._collection.items() if search_mapping[search_type](book_item)]
        return book_matches

    def remove_book(self, title: str) -> str:
        title = title.lower()
        for book_id, book_item in list(self._collection.items()):
            if book_item.title == title:
                del self._collection[book_id]
                return f"Book '{title}' has been removed from the collection."
        return f"Book with title '{title}' not found in the collection."

    def total_books_collection(self) -> int:
        return len(self._collection)

    def book_save_to_csv(self):
        data = []
        for book_id, book in self._collection.items():
            data.append({
                'id': book_id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'publisher': book.publisher,
                    'total_num_copies': book.total_num_copies,
                    'num_available_copies': book.num_available_copies,
                    'publication_date': book.publication_date
                })
        save_to_csv(data, 'data/books.csv', ['id', 'title', 'author', 'year', 'publisher', 'total_num_copies', 'num_available_copies', 'publication_date'])

    def book_load_from_csv(self):
        data = load_from_csv('data/books.csv')
        for row in data:
            self.add_book(row['title'], row['author'], int(row['year']), row['publisher'], int(row['total_num_copies']), int(row['num_available_copies']), row['publication_date'], int(row['id']))
