import random
import secrets
from datetime import datetime, timedelta

class Books:
    """
    A class used to represent a book in the library.

    Attributes:
        book_id (int): a randomly generated book ID from 0 to 9999.
        title (str): the title of the book.
        author (str) : the author of the book.
        year (int): the year of publication of the book.
        publisher (str): the publisher of the book.
        total_num_copies (int): Total number of copies of the book.
        num_available_copies (int): Number of available copies of the book.
        publication_date (datetime): Date of publication of the book.

    Methods:
        set_title(title): set the title of the book.
        set_author(author): set the author of the book.
        set_year(year): set the year of publication of the book.
        set_publisher(publisher): set the publisher of the book.
        set_total_num_copies(total_num_copies): set the total number of copies of the book.
        set_num_available_copies(num_available_copies): set the number of available copies of the book.
        set_publication_date(publication_date): set the publication date of the book.
        get_title():returns the title of the book.
        get_author(): returns the author of the book.
        get_year(): returns the year of publication of the book.
        get_publisher(): returns the publisher of the book.
        get_total_num_copies(): returns the total number of copies of the book.
        get_num_available_copies(): returns the number of available copies of the book.
        get_publication_date(): returns the publication date of the book.

    Notes:
        - The 'book_id' attribute is randomly generated and unique for each book.
        - Methods like 'set_title' and 'set_author' perform transformations on the input values.
        - The 'set_total_num_copies' method ensures the input is a valid integer.
        - The 'set_num_available_copies' method enforces the relationship between available and total copies.
        - The 'set_publication_date' method converts input date formats to 'dd/mm/yyyy'.
        - Methods like 'get_title' and 'get_author' provide direct access to attribute values.
        - This class provides a comprehensive structure for managing book details in a library.
    """

    def __init__(self, title, author, year, publisher, total_num_copies,
                 num_available_copies, publication_date):
        self.book_id = random.randint(0, 9999)  # generate random id
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.total_num_copies = total_num_copies
        self.num_available_copies = num_available_copies
        self.publication_date = publication_date

    # methods to set book attributes
    def set_title(self, title):
        self.title = title.lower()

    def set_author(self, author):
        try:
            # make sure the authors name only contains letters
            if author.isalpha():
                self.author = author.lower()
            else:
                raise ValueError("Invalid name. Author's name must contain only letters.")
        except ValueError as e:
            print(f"Input error: {e}")

    def set_year(self, year):
        try:
            # make sure it is an integer by converting input
            year = int(year)
            self.year = year
        except ValueError:
            print("Invalid input. Year should be a number.")
            return

    def set_publisher(self, publisher):
        self.publisher = publisher.lower()

    def set_total_num_copies(self, total_num_copies):
        try:
            # check if input give is a number (integer)
            total_num_copies = int(total_num_copies)
            self.total_num_copies = total_num_copies
        except ValueError:
            print("Invalid input. Total number of copies should be a number.")
            return

    def set_num_available_copies(self, num_available_copies):
        try:
            # check if input give is a number (integer)
            num_available_copies = int(num_available_copies)
            # number of available copies should logically be the same
            # or lower than the total number of copies
            if num_available_copies <= self.total_num_copies:
                self.num_available_copies = num_available_copies
            else:
                print(
                    "Invalid input. Number of available copies cannot be more than total copies."
                )
        except ValueError:
            print("Invalid input. 'Number of available copies' should be a number.")
            return

    def set_publication_date(self, publication_date):
        try:
            # converts the input to datetime
            input_date = datetime.strptime(publication_date, "%d/%m/%Y")
            self.publication_date = input_date
        except ValueError:
            print("Invalid input. Date should be in 'dd/mm/yyyy' format.")
            return

    # methods to return book attributes
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_total_num_copies(self):
        return self.total_num_copies

    def get_num_available_copies(self):
        return self.num_available_copies

    def get_publication_date(self):
        return self.publication_date

class BookList:
    """
    A class used to manage the collection of books in the library.

    Attributes:
        collection (dict): a dictionary that stores all books created using the Books class,
            using Books instances as values and the title as key.

    Methods:
        add_book(title, author, year, publisher, total_num_copies, num_available_copies, publication_date):
            adds a new book to the collection using provided attributes.
        find_book(data, search_type): searches for books in the collection
            based on search criteria that can be either title, author, publisher or publication_date.
        remove_book(title): deletes a book from the collection dictionary based on its title.
        total_books_collection(): returns the total number of books stored in the collection.

    Notes:
        - The `add_book` method creates a new instance of the `Books` class and adds it to the collection.
        - The `find_book` method allows searching for books based on various search criteria.
        - The `remove_book` method deletes a book from the collection based on its title.
        - The `total_books_collection` method returns the count of books in the collection.
        - The search in `find_book` is case-insensitive to prevent errors due to alternating case.
        - When searching by publication date, the input should be in 'dd mm yyyy' format.
        - Invalid inputs, such as incorrect dates, will be caught and appropriate messages will be displayed.
        - Invalid search types in `find_book` will result in an error message.
    """

    def __init__(self):
        # create dictionary to store all books from library
        self.collection = {}

    # add new book to the collection
    def add_book(self, title, author, year, publisher, total_num_copies,
                 num_available_copies, publication_date):
        try:
            # add new book to the library collection using the Books class
            new_book = Books(title, author, year, publisher, total_num_copies,
                            num_available_copies, publication_date)
            # add new book to dictionary
            self.collection[new_book.book_id] = new_book
        except ValueError:
            print("Invalid input. Please try again to input valid data.")
            return

    # search for book in the collection
    def find_book(self, data, search_type):
        # list with all matches for search
        book_matches = []
        # make sure there is no case-insensitive problem by converting the input into lowercase
        data = data.lower()
        search_type = search_type.lower()

        try:
            for book_id, book_item in self.collection.items():
                # find book from title
                # make sure the search does not have any errors from alternating case
                if search_type == "title" and data in book_item.title.lower(
                ):
                    book_matches.append(book_id)
                # find books from author
                # make sure the search does not have any errors from alternating case
                if search_type == "author" and data in book_item.author.lower():
                    book_matches.append(book_id)
                # find books from publisher
                # make sure the search does not have any errors from alternating case
                if search_type == "publisher" and data in book_item.publisher.lower():
                    book_matches.append(book_id)
                # find books from publishing date
                if search_type == "publication_date":
                    try:
                        input_date = datetime.strptime(data, "%d/%m/%Y")
                        if input_date.date() == book_item.publication_date.date():
                            book_matches.append(book_id)
                        else:
                            raise ValueError("Invalid input. Date should be in 'dd mm yyyy' format.")
                    except ValueError as e:
                        print(f"Input error: {e}")
            if not book_matches:
                print("There are no matches for this search, please try again.")
            else:
                return book_matches

        except KeyError:
            print(
                "Invalid search type. Please provide a valid search type of either 'title, author, publisher or publication_date'."
            )

    # remove book from collection by title
    def remove_book(self, title):
        try:
            title = title.lower()
            for book_item in self.collection.values():
                if book_item.title == title:
                    del self.collection[book_item.book_id]
                    return print(f"Book '{title}' has been removed from the collection.")
            raise KeyError
        except KeyError:
            return print(f"Book with title '{title}' not found in the collection.")

    # total number of books stored in the collection
    def total_books_collection(self):
        return len(self.collection)

class Users:
    """
    A class representing a user of the library.

    Attributes:
        username (str): the username of the library user.
        firstname (str): the first name of the library user.
        surname (str): the last name of the library user.
        house_number (int): the house number of the library user's address.
        street_name (str): the street name of the library user's address.
        postcode (int): the postcode of the library user's address.
        email_address (str): the email address of the library user.
        date_birth (datetime): the date of birth of the library user in 'dd/mm/yyyy' format.

    Methods:
        get_username(): returns the username of the library user.
        get_firstname(): returns the first name of the library user.
        get_surname(): returns the last name of the library user.
        get_house_number(): returns the house number of the library user's address.
        get_street_name(): returns the street name of the library user's address.
        get_postcode(): returns the postcode of the library user's address.
        get_email_address(): returns the email address of the library user.
        get_date_birth(): returns the date of birth of the library user.
        edit_username(new_username): updates the username of the library user.
        edit_firstname(new_firstname): updates the first name of the library user.
        edit_surname(new_surname): updates the last name of the library user.
        edit_house_number(new_house_number): updates the house number of the library user's address.
        edit_street_name(new_street_name): updates the street name of the library user's address.
        edit_postcode(new_postcode): updates the postcode of the library user's address.
        edit_email_address(new_email_address): updates the email address of the library user.
        edit_date_birth(new_date_birth): updates the date of birth of the library user.

    Note:
        - The methods that update attributes perform input validation to ensure proper data types and formats.
        - Some methods may raise ValueError if input does not meet validation requirements.
        - Use the provided methods to retrieve and update information about the library user.
    """

    def __init__(self, username, firstname, surname, house_number, street_name,
                 postcode, email_address, date_birth):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email_address = email_address
        self.date_birth = date_birth

    # returning methods for all attributes
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email_address(self):
        return self.email_address

    def get_date_birth(self):
        return self.date_birth

    # updating methods for all attributes
    def edit_username(self, new_username):
        self.username = new_username

    def edit_firstname(self, new_firstname):
        try:
            # check is name provided contains only letters
            if new_firstname.isalpha():
                self.firstname = new_firstname.lower()
            else:
                raise ValueError("New firstname must contain only letters.")
        except ValueError as e:
            print(f"Input error: {e}")

    def edit_surname(self, new_surname):
        try:
            # check is name provided contains only letters
            if new_surname.isalpha():
                self.surname = new_surname.lower()
            else:
                raise ValueError("New surname must contain only letters.")
        except ValueError as e:
            print(f"Input error: {e}")

    def edit_house_number(self, new_house_number):
        try:
            # check if the input only contains numbers
            new_house_number = int(new_house_number)
            self.house_number = new_house_number
        except ValueError:
            print("Input error. New house number must contain only numbers.")
            return

    def edit_street_name(self, new_street_name):
        self.street_name = new_street_name

    def edit_postcode(self, new_postcode):
        try:
            # check if the input only contains numbers
            new_postcode = int(new_postcode)
            self.postcode = new_postcode
        except ValueError:
            print(
                "Input error. New postcode must contain only numbers, without letters or special characters."
            )
            return

    def edit_email_address(self, new_email_address):
        try:
            # make sure the email is complete, checking for '@' and '.'
            if '@' in new_email_address and '.' in new_email_address:
                self.email_address = new_email_address
            else:
                raise ValueError("This email address is not valid, check if you email contains the '@' and '.' characters.")
        except ValueError as e:
            print(f"Input error: {e}")

    def edit_date_birth(self, new_date_birth):
        try:
            # converts the input to datetime
            #new_date_birth = datetime.strptime(new_date_birth, "%d/%m/%Y")
            self.date_birth = new_date_birth
            return
        except ValueError:
            print("Invalid input. Date of birth should be in 'dd/mm/yyyy' format.")
            return

class UserList:
    """
    A class used to manage the collection of library users.

    Attributes:
        collection (dict): a dictionary that stores all users created using the Users class,
            using Users instances as values and the username as the key.

    Methods:
        add_user(username, firstname, surname, house_number, street_name, postcode, email_address, date_birth):
            adds a new user to the collection using provided attributes.
        remove_user(firstname): removes a user from the collection dictionary based on their first name.
        total_users_collection(): returns the total number of users stored in the collection.
        get_username_values(username): returns all attributes of a user by their username.

    Notes:
        - The `add_user` method creates a new instance of the `Users` class and adds it to the collection.
        - The `remove_user` method deletes a user from the collection based on their first name.
        - The `total_users_collection` method returns the count of users in the collection.
        - The `get_username_values` method retrieves all attributes of a user based on their username.
        - When removing a user, if multiple users share the same first name, the user is asked to specify the username.
        - Invalid inputs or usernames not found will be handled with appropriate error messages.
    """

    def __init__(self):
        self.collection = {}

    # add new user to the collection
    def add_user(self, username, firstname, surname, house_number, street_name,
                 postcode, email_address, date_birth):
        # add new user of the library in the collection using the Users class
        new_user = Users(username, firstname, surname, house_number,
                         street_name, postcode, email_address, date_birth)
        # add new user to dictionary
        self.collection[new_user.username] = new_user

    # remove user from collection by first name
    def remove_user(self, firstname):
        # list with all matches for search
        user_matches = []
        # make sure there is no case-insensitive rpoblem by converting the input into lowercase
        firstname = firstname.lower()

        try:
            # find username from frist name from collection
            # append to list all the usernames that have the first name inputed
            for username, user in self.collection.items():
                if user.firstname == firstname:
                    user_matches.append(username)
            if len(user_matches) == 1:
                del self.collection[user_matches[0]]
                return print(f"User '{firstname}' has been deleted from the collection.")
            # ask for user to specify the user if more than one match the first name inputed
            if len(user_matches) > 1:
                print(f"The following users matched the first name inputed:\n{user_matches}.\nPlease enter the username that you wish to delete.")
                username_delete = input()
                del self.collection[username_delete]
                return print(f"User '{username_delete}' has been removed from the collection.")
            else:
                raise ValueError(f"User with first name '{firstname}' not found in the collection.")
        except KeyError as e:
            print(f"Input error: {e}")

    # total number of users stored in the collection
    def total_users_collection(self):
        return len(self.collection)

    # return all attributes of user by username
    def get_username_values(self, username):
        try:
            # iterate the key and get all values
            user = self.collection.get(username)
            if user:
                return user  # Return the User object
            else:
                print(f"Input error. Username {username} not found.")
                return None
        except KeyError:
            print(f"Input error. Username {username} not found.")
            return

class Loans:
    """
    A class used to represent a loan of a book from the library.

    Attributes:
        loan_code (str): A unique token representing the loan.
        book_id (int): The ID of the borrowed book.
        username (str): The username of the user borrowing the book.
        loan_date (datetime): The date when the book was borrowed.
        return_date (datetime): The date when the book is expected to be returned.

    Methods:
        get_book_id(): Returns the ID of the borrowed book.
        get_username(): Returns the username of the user borrowing the book.
        get_loan_date(): Returns the date when the book was borrowed.
        get_return_date(): Returns the date when the book is expected to be returned.
        set_book_id(book_id): Sets the ID of the borrowed book after validating its existence in the library's collection.
        set_username(username): Sets the username of the user borrowing the book after validating their registration.
        set_loan_date(loan_date): Manually sets the start date of the loan in 'dd/mm/yyyy hh:mm:ss' format.
        set_return_date(return_date): Manually sets the return date of the loan in 'dd/mm/yyyy hh:mm:ss' format.

    Notes:
        - The loan_code is generated using the secrets module to ensure uniqueness.
        - The default return_date is set to 10 days from the current date.
        - Methods that set attributes validate inputs against the library's collections (books and users).
        - Manual setting of loan and return dates allows flexibility in recording loan details.
    """

    def __init__(self, book_id, username):
        self.loan_code = secrets.token_hex(3)
        self.book_id = book_id
        self.username = username
        self.loan_date = datetime.now()
        self.return_date = datetime.now() + timedelta(days=10)

    # methods to return loan attributes
    def get_book_id(self):
        return self.book_id

    def get_username(self):
        return self.username

    def get_loan_date(self):
        return self.loan_date

    def get_return_date(self):
        return self.return_date

    # methods to set loan attributes
    def set_book_id(self, book_id):
        try:
            # make sure the book exists on the library's list of books
            if book_id in [k for k in book_list.collection.keys()]:
                self.book_id = book_id
            else:
                raise ValueError(f"The Book ID {book_id} is not in the library's collection.")
        except ValueError as e:
            print(f"Input error: {e}")

    def set_username(self, username):
        try:
            # make sure the user exists on the library's list of users
            if username in [k for k in user_list.collection.keys()]:
                self.book_id = username
            else:
                raise ValueError(f"The username {username} is not registered at the library.")
        except ValueError as e:
            print(f"Input error: {e}")

    def set_loan_date(self, loan_date):
        # this method is for manually setting the start date of the loan
        try:
            # converts the input to datetime
            input_date = datetime.strptime(loan_date, "%d/%m/%Y %H:%M:%S")
            self.publication_date = input_date.strftime("%d/%m/%Y %H:%M:%S")
        except ValueError:
            print("Invalid input. Date should be in 'dd/mm/yyyy hh:mm:ss' format.")
            return

    def set_return_date(self, return_date):
        # this method is for manually setting the end date of the loan
        try:
            # converts the input to datetime
            input_date = datetime.strptime(return_date, "%d/%m/%Y %H:%M:%S")
            self.publication_date = input_date.strftime("%d/%m/%Y %H:%M:%S")
        except ValueError:
            print("Invalid input. Date should be in 'dd/mm/yyyy hh:mm:ss' format.")
            return

class LoanList:
    """
    A class used to manage a collection of loans in the library.

    Attributes:
        collection (dict): A dictionary containing active loans, indexed by loan codes.

    Methods:
        add_loan(book_id, username): Creates a new loan for a book after validating availability and uniqueness.
        remove_loan(book_id, loan_code): Ends an active loan and updates book availability.
        late_loans(): Returns a list of loan codes for loans that are overdue.
        total_loans(): Returns the total number of active loans in the collection.

    Notes:
        - The 'collection' attribute stores active loans with their loan codes as keys.
        - The 'add_loan' method ensures that a book is available for loan and that loans are unique.
        - The 'remove_loan' method updates book availability when a loan is ended.
        - The 'late_loans' method identifies loans that are overdue based on return dates.
        - The 'total_loans' method provides a count of active loans.
    """

    def __init__(self):
        self.collection = {}

    # create a new loan
    def add_loan(self, book_id, username):
        try:
            # check if the user and book exist in the collection
            if username in user_list.collection and book_id in book_list.collection:
                book = book_list.collection[book_id]
                if book.get_num_available_copies() > 0:
                    new_loan = Loans(book_id, username)
                    self.collection[new_loan.loan_code] = new_loan
                    # Reduce the num_available_copies of the book
                    book.set_num_available_copies(book.get_num_available_copies() - 1)
                else:
                    raise ValueError(f"The book with ID {book_id} is currently not available.")
            else:
                raise ValueError(f"User or book not found in the collection.")
        except ValueError as e:
            print(f"Input error: {e}")

    # find loan
    def find_loan(self, data, search_type):
        # list with all matches for search
        loan_matches = []
        # make sure there is no case-insensitive problem by converting the input into lowercase
        data = data.lower()
        search_type = search_type.lower()

        try:
            for loan_code, loan_item in self.collection.items():
                # find book from title
                # make sure the search does not have any errors from alternating case
                if search_type == "username" and data in loan_item.username.lower():
                    loan_matches.append(loan_code)
                # find books from author
                # make sure the search does not have any errors from alternating case
                if search_type == "book_id" and data in loan_item.book_id.lower():
                    loan_matches.append(loan_code)
            if not loan_matches:
                print("There are no matches for this search, please try again.")
            else:
                return loan_matches
        except KeyError:
            print(
                "Invalid search type. Please provide a valid search type of either 'username or book_id'."
            )

    # end a loan
    def remove_loan(self, book_id, loan_code):
        try:
            del self.collection[loan_code]
            # increase the num_available_copies of the book
            book = book_list.collection[book_id]
            book.num_available_copies += 1
        except KeyError:
            print(f"Input error. The loan number {loan_code} is already no longer active.")
            return

    # get late loans
    def late_loans(self):
        # list with all matches
        late_loans = []
        for k,v in self.collection.items():
            if v.return_date < datetime.now():
                late_loans.append(k)
        if not late_loans:
            return print("There are no currently late loans.")
        else:
            return print(f"Here are the codes for overdue loans:\n{late_loans}")

    # get total of loans
    def total_loans(self):
        return len(self.collection)

def start_select():
    """
    This function presents the user with options related to the library's system
    and allows them to select a category. The options are:
    1. Books
    2. Users
    3. Loans
    The function checks for the validity of user input and ensures it corresponds
    to one of the provided categories.
    """

    while True:
        print("\nWelcome to the library's system, to start select the desired category:")
        categ = input("1. Books     2. Users     3. Loans\n")
        try:
            # check if input is not empty
            if not categ:
                raise ValueError("Input is empty. Please provide a valid number.")
            # check if input is valid whithin the options
            if categ == "1":
                book_options()
                break
            if categ == "2":
                user_options()
                break
            if categ == "3":
                loan_options()
                break
            else:
                raise ValueError("Invalid category choice. Please provide a valid number.")
        except ValueError as e:
            print(f"Input error: {e}\n")

def book_options():
    """
    This function presents the user with book-related operations within the library's system.
    The available operations include:
    1. Add a book
    2. Remove a book
    3. Find a book
    4. Get the information about a book
    5. Update a book
    6. Check the total number of books in the library
    """

    print("""\nWould you like to:\n
          1. Add a book\n
          2. Remove a book\n
          3. Find a book\n
          4. Get the information about a book\n
          5. Update a book\n
          6. Check total of books in library\n""")
    option = get_valid_input("Please choose an option: ",
                             lambda x: x in ["1", "2", "3", "4", "5", "6"],
                             "Invalid input. Please try again.")
    try:
        # 1 add book
        if option == "1":
            print("To add a new book please provide:")
            # input must not be empty
            input_title = get_valid_input("Book title: ",
                                          lambda x: x.strip() != "",
                                          "Input cannot be empty")
            # input must not be empty and contain only letters
            input_author = get_valid_input("Book author: ",
                                           lambda x: x.strip() != "" and x.isalpha(),
                                           "Input invalid. Must not be empty and/or contain only letters.")
            # input must not be empty and be only in numbers and have 4 numbers to ensure is a full year number
            input_year = get_valid_input("Book year: ",
                                         lambda x: x.strip() != "" and x.isnumeric() and len(x) == 4,
                                         "Input invalid. Must not be empty and/or contain only numbers.")
            # input must not be empty
            input_publisher = get_valid_input("Book publisher: ",
                                              lambda x: x.strip() != "",
                                              "Input invalid. Must not be empty.")
            # input must not be empty and be a number
            input_total_copies = get_valid_input("Total number of book copies: ",
                                                 lambda x: x.strip() != "" and x.isnumeric(),
                                                 "Input invalid. Must not be empty and/or contain only numbers.")
            # input must be a valid date
            input_pubdate = get_valid_date("Book publication date (Make sure the date is in the 'dd/mm/yyyy' format): ")
            try:
                book_list.add_book(input_title, input_author, input_year, input_publisher,
                                   input_total_copies, input_total_copies, input_pubdate)
                return print("Book successfully added to library collection.")
            except TypeError as e:
                print(f"Error adding book: try again and make sure your input is in a valid. {e}")
                return

        # 2 remove book
        if option == "2":
            # make sure input is not empty
            remove_title = get_valid_input("Please provide the title of the book you would like to remove from the library:\n",
                                           lambda x: x.strip() != "",
                                           "Input invalid. Must not be empty.")
            return book_list.remove_book(remove_title)
            #return print(f"Book '{remove_title}' successfully removed from library collection.")

        # 3 find book
        if option == "3":
            print("Would you like to find your desired book by title, author, publisher or publication date?")
            # make sure inputs are not empty
            input_search_type = get_valid_input("Please enter here the search type: ",
                                                lambda x: x.strip() != "" and x in ["title", "author", "publisher", "publication_date"],
                                                "Input invalid. Must not be empty and the search type must be one of the above mentioned.")
            input_data = get_valid_input("Please enter here the data be searched: ",
                                         lambda x: x.strip() != "",
                                         "Input invalid. Must not be empty.")
            match_list = book_list.find_book(input_data, input_search_type)
            return print(f"Here are the book IDs that matched your search:\n{match_list}")

        # 4 info on book
        if option == "4":
            print("To get all the information of a specified book please provide the following:")
            # make sure input is not empty and valid
            input_info = get_valid_input("Book ID: ",
                                         lambda x: x.strip() != "" and x.isnumeric() and len(x)<= 4,
                                         "Input invalid. Must not be empty and must contain only numbers (maximum 4).")
            input_info = int(input_info)
            # get book instance from the collection using id
            selected_book = book_list.collection.get(input_info)

            print(f"Book title: {selected_book.get_title()}")
            print(f"Book author: {selected_book.get_author()}")
            print(f"Book year: {selected_book.get_year()}")
            print(f"Book publisher: {selected_book.get_publisher()}")
            print(f"Total number of book copies: {selected_book.get_total_num_copies()}")
            print(f"Available number of book copies: {selected_book.get_num_available_copies()}")
            print(f"Book publication date: {selected_book.get_publication_date()}") #strftime('%d/%B/%Y')}")
            return

        # 5 update book
        if option == "5":
            print("To update a books information please enter:")
            # make sure inputs are not empty and valid
            input_book_id = get_valid_input("ID of the book you wish to update: ",
                                            lambda x: x.strip() != "" and x.isnumeric() and len(x)<= 4,
                                            "Input invalid. Must not be empty and must contain only numbers (maximum 4).")
            input_new_title = get_valid_input("New title: ",
                                              lambda x: x.strip() != "",
                                              "Input invalid. Must not be empty.")
            input_new_author = get_valid_input ("New author: ",
                                                lambda x: x.strip() != "" and x.isalpha(),
                                                "Input invalid. Must not be empty and must contain only letters.")
            input_new_year = get_valid_input("New year: ",
                                             lambda x: x.strip() != "" and x.isnumeric() and len(x)== 4,
                                             "Input invalid. Must not be empty and must contain 4 digits.")
            input_new_publisher = get_valid_input("New publisher: ",
                                                  lambda x: x.strip() != "",
                                                  "Input invalid. Must not be empty.")
            input_new_total_copies = get_valid_input("New number of total copies: ",
                                                     lambda x: x.strip() != "" and x.isnumeric(),
                                                     "Input invalid. Must not be empty and must contain only numbers.")
            input_new_available_copies = get_valid_input("New number of available copies: ",
                                                        lambda x: x.strip() != "" and x.isnumeric(),
                                                        "Input invalid. Must not be empty and must contain only numbers.")
            input_new_publication_date = get_valid_date("New publication date (Make sure the date is in the 'dd/mm/yyyy' format): ")

            for book_item in book_list.collection.values():
                if book_item.book_id == input_book_id:
                    book_item.set_title(input_new_title)
                    book_item.set_author(input_new_author)
                    book_item.set_year(input_new_year)
                    book_item.set_publisher(input_new_publisher)
                    book_item.set_total_num_copies(input_new_total_copies)
                    book_item.set_num_available_copies(input_new_available_copies)
                    book_item.set_publication_date(input_new_publication_date)
            return

        # 6 total books
        if option == "6":
            return print(f"The library has a total of {book_list.total_books_collection()} books.")

        else:
            raise ValueError("Invalid choice. Please provide the number corresponding to your choice.")

    except ValueError as e:
        return print(f"Input error: {e}")

def user_options():
    """
    Display a menu for managing library users and process user choices.

    The function presents the following options to the user:
    1. Add a new user to the library.
    2. Remove an existing user from the library by their first name.
    3. Retrieve and display information about a specific user based on their username.
    4. Update details for an existing user.
    5. Display the total number of users registered in the library.

    Each option performs validations to ensure accurate and consistent data input.
    For instance:
    - Usernames must be unique.
    - Names should only contain alphabetic characters.
    - House numbers and postcodes should be numeric.
    - Email addresses should be in a valid format.
    - Dates of birth should be in the 'dd/mm/yyyy' format.
    """

    print("""\nWould you like to:\n
          1. Add an user\n
          2. Remove an user\n
          3. Get the information about an user\n
          4. Update an user\n
          5. Check total users registered in library\n""")
    option = get_valid_input("Please choose an option: ",
                             lambda x: x in ["1", "2", "3", "4", "5"],
                             "Invalid input. Please try again.")
    try:
        # 1 add user
        if option == "1":
            print("To add a new user please provide:")
            # make sure inputs are valid and not empty
            while True:
                # check if the username already exists
                input_username = get_valid_input("Username: ",
                                             lambda x: x.strip() != "",
                                             "Input cannot be empty")
                if input_username in user_list.collection:
                    print(f"Username '{input_username}' already exists. Please choose a different username.")
                else: break

            input_firstname = get_valid_input("First name: ",
                                              lambda x: x.strip() != "" and x.isalpha(),
                                              "Input invalid. Must not be empty and/or contain only letters.")
            input_surname = get_valid_input("Surname: ",
                                            lambda x: x.strip() != "" and x.isalpha(),
                                            "Input invalid. Must not be empty and/or contain only letters.")
            input_house_number = get_valid_input("House number: ",
                                                 lambda x: x.strip() != "" and x.isnumeric(),
                                                 "Input invalid. Must not be empty and/or contain only numbers.")
            input_street_name = get_valid_input("Street name: ",
                                                lambda x: x.strip() != "",
                                                "Input cannot be empty")
            input_postcode = get_valid_input("Postcode: ",
                                             lambda x: x.strip() != "" and x.isnumeric(),
                                             "Input invalid. Must not be empty and/or contain only numbers.")
            input_email_adress = get_valid_input("Email address: ",
                                                 lambda x: x.strip() != "" and '@' in x and '.' in x,
                                                 "Input invalid. Email address cannot be empty and must contain the '@' and '.' characters.")
            input_date_birth = get_valid_date("Date of birth (Make sure the date is in the 'dd/mm/yyyy' format): ")

            user_list.add_user(input_username,input_firstname,input_surname,input_house_number,
                              input_street_name,input_postcode,input_email_adress,input_date_birth)
            return print("User successfully registered to library.")

        # 2 remove user from first name
        if option == "2":
            # make sure input is valid and not empty
            remove_firstname = get_valid_input("Please provide the first name of the user you would like to remove from the library:\n",
                                               lambda x: x.strip() != "" and x.isalpha(),
                                               "Input invalid. Must not be empty and/or contain only letters.")
            user_list.remove_user(remove_firstname)
            return

        # 3 info on user
        if option == "3":
            # make sure input is not empty
            print("To get all the information of a specified user please provide the following:")
            input_info = get_valid_input("Username: ",
                                         lambda x: x.strip() != "",
                                         "Input invalid. Must not be empty.")
            user = user_list.get_username_values(input_info)
            if user:
                print(f"Username: {user.username}")
                print(f"First Name: {user.firstname}")
                print(f"Surname: {user.surname}")
                print(f"House Number: {user.house_number}")
                print(f"Street Name: {user.street_name}")
                print(f"Postcode: {user.postcode}")
                print(f"Email Address: {user.email_address}")
                print(f"Date of Birth: {user.date_birth}")
            return

        # 4 update user
        if option == "4":
            # make sure inputs are valid and not empty
            print("To update a user's information please enter:")
            while True:
                # make sure input is not empty
                input_username = get_valid_input("Username of the user you wish to update: ",
                                                lambda x: x.strip() != "",
                                            "Input invalid. Must not be empty.")
                # check if the username already exists
                if input_username not in user_list.collection:
                        print(f"Username '{input_username}' does not exist. Please enter a valid username.")
                else: break
            # get user instance
            user_to_update = user_list.collection[input_username]
            # new info input
            while True:
                # new username cannot already exist in collection
                input_new_username = get_valid_input("New username: ",
                                                    lambda x: x.strip() != "",
                                                    "Input invalid. Must not be empty.")
                if input_new_username != user_to_update.username and input_new_username in user_list.collection:
                    print(f"Username '{input_new_username}' already exists. Please choose a different username.")
                else: break
            input_new_firstname = get_valid_input("New first name: ",
                                                  lambda x: x.strip() != "" and x.isalpha(),
                                                  "Input invalid. Must not be empty and/or contain only letters.")
            input_new_surname = get_valid_input ("New surname: ",
                                                 lambda x: x.strip() != "" and x.isalpha(),
                                                 "Input invalid. Must not be empty and/or contain only letters.")
            input_new_house_number = get_valid_input("New house number: ",
                                                 lambda x: x.strip() != "" and x.isnumeric(),
                                                 "Input invalid. Must not be empty and/or contain only numbers.")
            input_new_street_name = get_valid_input("New street name: ",
                                                lambda x: x.strip() != "",
                                                "Input cannot be empty")
            input_new_postcode = get_valid_input("New postcode: ",
                                             lambda x: x.strip() != "" and x.isnumeric(),
                                             "Input invalid. Must not be empty and/or contain only numbers.")
            input_new_email_address = get_valid_input("New email address: ",
                                                 lambda x: x.strip() != "" and '@' in x and '.' in x,
                                                 "Input invalid. Email address cannot be empty and must contain the '@' and '.' characters.")
            input_new_date_birth = get_valid_date("New date of birth (Make sure the date is in the 'dd/mm/yyyy' format): ")

            #for user in user_list.collection.values():
             #   if user.username == input_username:
            user_to_update.edit_username(input_new_username)
            user_to_update.edit_firstname(input_new_firstname)
            user_to_update.edit_surname(input_new_surname)
            user_to_update.edit_house_number(input_new_house_number)
            user_to_update.edit_street_name(input_new_street_name)
            user_to_update.edit_postcode(input_new_postcode)
            user_to_update.edit_email_address(input_new_email_address)
            user_to_update.edit_date_birth(input_new_date_birth)

            print("User sucessfully updated.")
            return

        # 5 total users
        if option == "5":
            print(f"The library has a total of {user_list.total_users_collection()} users.")

        else:
            raise ValueError("Invalid choice. Please provide the number corresponding to your choice.")

    except ValueError as e:
        print(f"Input error: {e}")

def loan_options():
    """
    Provides an interactive menu for loan-related tasks in the library system.

    The function displays a menu to the user with options to:
    1. Start a loan.
    2. End a loan.
    3. Find a loan by either a Username or Book ID.
    4. Check all late loans.
    5. Display the total number of active loans in the library.

    Parameters:
    - None

    Returns:
    - None. The function executes library loan operations based on user input.

    Notes:
    - `get_valid_input` function is used to get and validate user input.
    - `user_list` is a global collection containing user data.
    - `book_list` is a global collection containing book data.
    - `loan_list` is a global collection containing loan data.
    - Exceptions are handled for invalid inputs.
    """
    print("""\nWould you like to:\n
          1. Start a loan\n
          2. End a loan\n
          3. Find a loan\n
          4. Check all late loans\n
          5. Check total of loans in library\n""")
    option = get_valid_input("Please choose an option: ",
                             lambda x: x in ["1", "2", "3", "4", "5"],
                             "Input Error. Please select a valid option (1, 2, 3, 4 or 5).")
    try:
        # 1 add loan
        if option == "1":
            print("To start a new loan please provide:")
            # check for input not empty and if user exists on the collection
            input_book_id = get_valid_input("Username of borrower user: ",
                                            lambda x: x.strip() != "" and x in user_list.collection,
                                             "Input error. Input cannot be empty and/or user must exist on the data base.")
            # check for input not empty and if book exists on the collection
            input_user_id = get_valid_input("Book ID of loaned book: ",
                                            lambda x: x.strip() != "" and x in book_list.collection,
                                            "Input error. Input cannot be empty and/or book must exist on the data base.")
            loan_list.add_loan(input_book_id,input_user_id)
            print("Loan added successfully.")

        # 2 remove loan
        if option == "2":
            end_loan = get_valid_input("Please provide the loan code of the loan you would like to end: ",
                                       lambda x: x.strip() != "" and x in loan_list.collection,
                                       "Input error. Input cannot be empty and/or loan must be valid.")
            loan_list.remove_loan(end_loan)

        # 3 find loan
        if option == "3":
            print("Would you like to find the loan by Username or Book ID?")
            # make sure inputs are not empty
            input_search_type = get_valid_input("Please enter here the search type: ",
                                                lambda x: x.strip() != "" and x in ["username", "book_id"],
                                                "Input invalid. Must not be empty and the search type must be one of the above mentioned.")
            input_data = get_valid_input("Please enter here the data be searched: ",
                                         lambda x: x.strip() != "",
                                         "Input invalid. Must not be empty.")
            matches = loan_list.find_loan(input_data, input_search_type)
            return print(f"Here are the loan codes that matched your search:\n{matches}")

        # 4 late loans
        if option == "4":
            return loan_list.late_loans()

        # 5 total loans
        if option == "5":
            print(f"There are a total of {loan_list.total_loans()} loans currently active.")

        else:
            raise ValueError("Invalid choice. Please provide the number corresponding to your choice.")

    except ValueError as e:
        print(f"Input error: {e}")

def get_valid_input(prompt, validation_function, error_message):
    """
    Prompt the user for input and validate it using a specified function.

    Parameters:
    - prompt (str): The message that prompts the user for input.
    - validation_function (function): A function that takes the user input as an argument and returns True if the input is valid, False otherwise.
    - error_message (str): The message to be displayed when the user provides invalid input.

    Returns:
    - str: The valid user input.

    Raises:
    - ValueError: If there is an issue with the validation function.
    """

    while True:
        user_input = input(prompt)
        try:
            if validation_function(user_input):
                return user_input
            else:
                print(error_message)
        except ValueError as e:
            print(f"Input error: {e}")

def get_valid_date(prompt):
    """
    Prompt the user for a date input and validate its format.

    Parameters:
    - prompt (str): The message that prompts the user for a date input.

    Returns:
    - datetime.datetime: The valid date input as a datetime object.

    Note:
    - The expected date format is 'dd/mm/yyyy'.
    """

    while True:
        date_input = input(prompt)
        try:
            # converts the input to datetime
            date_time = datetime.strptime(date_input, "%d/%m/%Y")
            return date_time
        except ValueError:
            print("Invalid input. Date should be in 'dd/mm/yyyy' format.")



# create instances of classes
book_list = BookList()
user_list = UserList()
loan_list = LoanList()

if __name__ == '__main__':
    """
    Main execution block for the library system.

    This script initializes the library system by creating instances of the BookList, UserList, and LoanList classes.
    It then pre-populates these lists with sample books, users, and loans for testing purposes.

    After setup, the script enters an interactive loop where the user is presented with a start menu (via the start_select() function).
    The user is prompted after each operation to continue with another action or to exit the system.

    Setup Data:
    - Books: "To Kill a Mockingbird", "1984", and "The Great Gatsby".
    - Users: "user123" (John Smith), "booklover22" (Emily Johnson), and "avidreader" (Sarah Williams).
    - Loans: Sample loans are created between the above users and books.

    Notes:
    - The 'start_select()' function is presumed to be the primary interaction method for the user.
    - Execution continues until the user decides to exit.
    """

    # pre-entered book and users for testing
    book_list.add_book("To Kill a Mockingbird", "Harper Lee", 1960, "J. B. Lippincott & Co.", 1, 1, "11/07/1960")
    book_list.add_book("1984", "George Orwell", 1949, "Secker & Warburg", 2, 2, "08/06/1949")
    book_list.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Charles Scribner's Sons", 3, 3, "10/04/1925")

    user_list.add_user("user123", "John", "Smith", 123, "Oak Street", 12345, "john.smith@example.com", "15/01/1985")
    user_list.add_user("booklover22", "Emily", "Johnson", 456, "Maple Avenue", 56789, "emily.johnson@emailprovider.com", "05/11/1990")
    user_list.add_user("avidreader", "Sarah", "Williams", 789, "Elm Lane", 98765, "sarah.williams@example.net", "22/03/2000")

    # obtain book id
    book1id = book_list.find_book("To Kill a Mockingbird", "title")
    book2id = book_list.find_book("1984", "title")
    book3id = book_list.find_book("The Great Gatsby", "title")

    print(book3id)

    # add example loans
    loan_list.add_loan(book1id[0], "user123")
    loan_list.add_loan(book3id[0], "booklover22")
    loan_list.add_loan(book3id[0], "avidreader")

    # start code
    while True:
        start_select()
        while True:
            continue_quit = input("\nWould you like to do another operation? [y/n]")
            if continue_quit == "y":
                break
            if continue_quit == "n":
                print("Exiting the library system.")
                exit()
            else:
                print("Please answer with 'y' for yes and 'n' for no.")
