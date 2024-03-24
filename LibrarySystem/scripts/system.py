from scripts.functions import get_valid_input, get_valid_date
import re

class LibrarySystem:
    def __init__(self, book_list, user_list, loan_list):
        self.book_options = BookOptions(book_list)
        self.user_options = UserOptions(user_list)
        self.loan_options = LoanOptions(loan_list, book_list, user_list)
        self.options = {
            "1": self.book_options.book_options,
            "2": self.user_options.user_options,
            "3": self.loan_options.loan_options
        }

    def start_select(self):
        max_attempts = 3
        attempts = 0

        while True:
            print("\n------------------------------------------------------------------------")
            print("\nWelcome to the library's system.\n")
            print("1. Books\n2. Users\n3. Loans\n4. Quit")
            categ = input("To start select the desired category:")
            if categ == "4":
                break
            try:
                if not categ:
                    raise ValueError("Input is empty. Please provide a valid number.")
                elif categ in self.options:
                    self.options[categ]()
                    attempts = 0
                else:
                    raise ValueError("Invalid category choice. Please provide a valid number.")
            except ValueError as e:
                print(f"Input error: {e}\n")
                attempts += 1
                if attempts >= max_attempts:
                    print("Maximum attempts reached. Exiting.")
                    break

class BookOptions:
    def __init__(self, book_list):
        self.book_list = book_list

    def book_options(self):
        print("""\nWould you like to:\n
            1. Add a book\n
            2. Remove a book\n
            3. Find a book\n
            4. Get the information about a book\n
            5. Update a book\n
            6. Check total of books in library\n""")

        options = {
            "1": self.book_option_1_add,
            "2": self.book_option_2_remove,
            "3": self.book_option_3_find,
            "4": self.book_option_4_info,
            "5": self.book_option_5_update,
            "6": self.book_option_6_total
        }

        while True:
            option = input("Please choose an option: ")
            if option not in options:
                print("Invalid input. Please try again.")
                continue
            options[option]()
            break

    def get_book_info(self):
        input_title = get_valid_input("Book title: ", lambda x: x.strip() != "", "Input cannot be empty")
        input_author = get_valid_input("Book author: ", lambda x: x.strip() != "" and x.isalpha(), "Input invalid. Must not be empty and/or contain only letters.")
        input_year = int(get_valid_input("Book year: ", lambda x: x.strip() != "" and x.isnumeric() and len(x) == 4, "Input invalid. Must not be empty and/or contain only numbers."))
        input_publisher = get_valid_input("Book publisher: ", lambda x: x.strip() != "", "Input invalid. Must not be empty.")
        input_total_copies = int(get_valid_input("Total number of book copies: ", lambda x: x.strip() != "" and x.isnumeric(), "Input invalid. Must not be empty and/or contain only numbers."))
        input_available_copies = int(get_valid_input("Number of available copies: ", lambda x: x.strip() != "" and x.isnumeric(), "Input invalid. Must not be empty and/or contain only numbers."))
        input_pubdate = get_valid_date("Book publication date (Make sure the date is in the 'dd-mm-yyyy' format): ")
        return input_title, input_author, input_year, input_publisher, input_total_copies, input_available_copies, input_pubdate

    def book_option_1_add(self):
        print("To add a new book please provide:")
        try:
            self.book_list.add_book(*self.get_book_info())
            print("Book successfully added to library collection. You'll be redirected to the main menu.")
        except TypeError as e:
            print(f"Error adding book: try again and make sure your input is in a valid. {e}")

    def book_option_2_remove(self):
        remove_title = get_valid_input("Please provide the title of the book you would like to remove from the library:\n",
                    lambda x: x.strip() != "",
                    "Input invalid. Must not be empty.")
        result = self.book_list.remove_book(remove_title)
        print(result)

    def book_option_3_find(self):
        print("Would you like to find your desired book by title, author, publisher or publication date?")
        input_search_type = get_valid_input("Please enter here the search type: ",
                                            lambda x: x.strip() != "" and x in ["title", "author", "publisher", "publication date"],
                                            "Input invalid. Must not be empty and the search type must be one of the above mentioned.")

        if input_search_type == "publication date":
            input_data = get_valid_date("Please enter here the data be searched (Make sure the date is in the 'dd/mm/yyyy' format): ")
        else:
            input_data = get_valid_input("Please enter here the data be searched: ",
                                    lambda x: x.strip() != "",
                                    "Input invalid. Must not be empty.")
        match_list = self.book_list.find_book(input_data, input_search_type)

        if not match_list:
            print("No books found that correspond your search. You'll be redirected to the main menu.")
        else:
            print(f"Here are the book IDs that matched your search:\n{match_list}\nYou'll be redirected to the main menu.")

    def book_option_4_info(self):
        print("To get all the information of a specified book please provide the following:")
        input_info = get_valid_input("Book ID: ", lambda x: x.strip() != "" and x.isnumeric() and len(x) <= 4,
                    "Input invalid. Must not be empty and must contain only numbers (maximum 4).")
        input_info = int(input_info)
        selected_book = self.book_list.get_books().get(input_info)
        if selected_book is not None:
            book_info = {
            "Book title": selected_book.title,
            "Book author": selected_book.author,
            "Book year": selected_book.year,
            "Book publisher": selected_book.publisher,
            "Total number of book copies": selected_book.total_num_copies,
            "Available number of book copies": selected_book.num_available_copies,
            "Book publication date": selected_book.publication_date
            }

            for key, value in book_info.items():
                print(f"{key}: {value}")
            print("You'll be redirected to the main menu.")
        else: print("Book not found. You'll be redirected to the main menu.")

    def book_option_5_update(self):
        print("To update a book please provide the following:")
        input_id = get_valid_input("Book ID: ", lambda x: x.strip() != "" and x.isnumeric() and len(x) <= 4,
                    "Input invalid. Must not be empty and must contain only numbers (maximum 4).")
        input_id = int(input_id)
        if input_id not in self.book_list.get_books():
            print(f"No book found with id {input_id}. You'll be redirected to the main menu.")
            return

        try:
            self.book_list.update_book(input_id, *self.get_book_info())
            print("Book successfully updated. You'll be redirected to the main menu.")
        except TypeError as e:
            print(f"Error updating book: try again and make sure your input is in a valid format. {e}")

    def book_option_6_total(self):
        total_books = self.book_list.total_books_collection()
        print(f"The library has a total of {total_books} books. You'll now be redirected to the main menu.")

class UserOptions:
    def __init__(self, user_list):
        self.user_list = user_list

    def user_options(self):
        print("""\nWould you like to:\n
            1. Add a user\n
            2. Remove a user\n
            3. Find a user\n
            4. Get the information about a user\n
            5. Update a user\n
            6. Check total of users in library\n""")

        options = {
            "1": self.user_option_1_add,
            "2": self.user_option_2_remove,
            "3": self.user_option_3_find,
            "4": self.user_option_4_info,
            "5": self.user_option_5_update,
            "6": self.user_option_6_total
        }

        while True:
            option = input("Please choose an option: ")
            if option not in options:
                print("Invalid input. Please try again.")
                continue
            options[option]()
            break

    def get_user_info(self):
        username = get_valid_input("Enter username: ", lambda x: x.strip() != "" and x not in self.user_list.get_users(), "Input invalid. Must not be empty or cannot already exist.")
        firstname = get_valid_input("Enter first name: ", lambda x: x.strip() != "", "Input invalid. Must not be empty.")
        surname = get_valid_input("Enter surname: ", lambda x: x.strip() != "", "Input invalid. Must not be empty.")
        house_number = int(get_valid_input("Enter house number: ", lambda x: x.strip() != "" and x.isnumeric(), "Input invalid. Must not be empty and/or contain only numbers."))
        street_name = get_valid_input("Enter street name: ", lambda x: x.strip() != "", "Input invalid. Must not be empty and/or contain only numbers.")
        postcode = int(get_valid_input("Enter postcode: ", lambda x: x.strip() != "" and x.isnumeric(), "Input invalid. Must not be empty and/or contain only numbers."))
        email_address = get_valid_input("Enter email address: ", lambda x: re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", x) is not None, "Input invalid. Must be a valid email address.")
        date_birth = get_valid_date("Enter date of birth (Make sure the date is in the 'dd-mm-yyyy' format): ")
        return username, firstname, surname, house_number, street_name, postcode, email_address, date_birth

    def user_option_1_add(self):
        print("To add a new user please provide:")
        try:
            self.user_list.add_user(*self.get_user_info())
            print("User successfully added to library collection. You'll be redirected to the main menu.")
        except TypeError as e:
            print(f"Error adding user: try again and make sure your input is valid. {e}")

    def user_option_2_remove(self):
        remove_name = get_valid_input("Please provide the name of the user you would like to remove from the library:\n",
                            lambda x: x.strip() != "",
                            "Input invalid. Must not be empty.")
        result = self.user_list.remove_user(remove_name)
        print(result)

    def user_option_3_find(self):
        print("Would you like to find your desired user by username, firstname or surname?")
        input_search_type = get_valid_input("Please enter here the search type: ",
                                            lambda x: x.strip() != "" and x in ["username", "firstname", "surname"],
                                            "Input invalid. Must not be empty and the search type must be one of the above mentioned.")
        input_data = get_valid_input("Please enter here the data be searched: ",
                                    lambda x: x.strip() != "",
                                    "Input invalid. Must not be empty.")
        match_list = self.user_list.find_user(input_data, input_search_type)

        if not match_list:
            print("No users found that correspond your search. You'll be redirected to the main menu.")
        else:
            print(f"Here are the usernames that matched your search:\n{match_list}\nYou'll be redirected to the main menu.")

    def user_option_4_info(self):
        print("To get all the information of a specified user please provide the following:")
        input_info = get_valid_input("Username: ", lambda x: x.strip() != "", "Input invalid. Must not be empty.")
        selected_user = self.user_list.get_users().get(input_info)

        if selected_user is not None:
            user_info = {
            "User username": selected_user.username,
            "User first name": selected_user.firstname,
            "User surname": selected_user.surname,
            "User house number": selected_user.house_number,
            "User street name": selected_user.street_name,
            "User postcode": selected_user.postcode,
            "User date of birth": selected_user.date_birth,
            "User email": selected_user.email_address,
        }
            for key, value in user_info.items():
                print(f"{key}: {value}")
            print("You'll be redirected to the main menu.")
        else: print("User not found. You'll be redirected to the main menu.")

    def user_option_5_update(self):
        print("To update a user please provide the following:")
        input_id = get_valid_input("Username: ", lambda x: x.strip() != "", "Input invalid. Must not be empty.")
        selected_user = self.user_list.get_users().get(input_id)

        if selected_user is None:
            print(f"No user with username {input_id} exists.")
            return

        try:
            self.user_list.update_user(selected_user, *self.get_user_info())
            print("User successfully updated. You'll be redirected to the main menu.")
        except TypeError as e:
            print(f"Error updating user: try again and make sure your input is in a valid. {e}")

    def user_option_6_total(self):
        total_users = self.user_list.total_users_collection()
        print(f"The library has a total of {total_users} users.")

class LoanOptions:
    def __init__(self, loan_list, book_list, user_list):
        self.loan_list = loan_list
        self.book_list = book_list
        self.user_list = user_list

    def loan_options(self):
        print("""\nWould you like to:\n
            1. Add a loan\n
            2. Remove a loan\n
            3. Find a loan\n
            4. Get the information about a loan\n
            5. Find all late loans\n
            6. Check total of loans in library\n""")

        options = {
            "1": self.loan_option_1_add,
            "2": self.loan_option_2_remove,
            "3": self.loan_option_3_find,
            "4": self.loan_option_4_info,
            "5": self.loan_option_5_late,
            "6": self.loan_option_6_total
        }

        while True:
            option = input("Please choose an option: ")
            if option in options:
                options[option]()
                break
            else:
                print("Invalid input. Please try again.")

    def get_loan_info(self):
        input_user_id = get_valid_input("Username: ",
                                        lambda x: x.strip() != "" and x in self.user_list.get_users().keys(),
                                        "Input invalid. Must not be empty and must exist in the user list.")
        input_book_id = int(get_valid_input("Book ID: ",
                                            lambda x: x.strip() != "" and x.isnumeric() and len(x) <= 4 and int(x) in self.book_list.get_books().keys(),
                                            "Input invalid. Must not be empty, must contain only numbers (maximum 4), and must exist in the book list."))
        input_loan_date = get_valid_date("Loan date (Make sure the date is in the 'dd-mm-yyyy' format): ")
        return input_user_id, input_book_id, input_loan_date

    def loan_option_1_add(self):
        print("To add a new loan please provide:")
        try:
            self.loan_list.add_loan(*self.get_loan_info())
            print("Loan successfully added to library collection. You'll be redirected to the main menu.")
        except TypeError as e:
            print(f"Error adding loan: try again and make sure your input is valid. {e}")

    def loan_option_2_remove(self):
        remove_loan_id = get_valid_input("Please provide the ID of the loan you would like to remove from the library:\n",
                            lambda x: x.strip() != "",
                            "Input invalid. Must not be empty.")
        self.loan_list.move_loan(remove_loan_id)
        print(f"Loan '{remove_loan_id}' successfully removed from library collection. You'll be redirected to the main menu.")

    def loan_option_3_find(self):
        print("Would you like to find your desired loan by username or book ID?")
        input_search_type = get_valid_input("Please enter here the search type: ",
                                            lambda x: x.strip() != "" and x in ["username", "book id"],
                                            "Input invalid. Must not be empty and the search type must be one of the above mentioned.")
        input_data = get_valid_input("Please enter here the data be searched: ",
                                    lambda x: x.strip() != "",
                                    "Input invalid. Must not be empty.")
        match_list = self.loan_list.find_loan(input_data, input_search_type)
        print(f"Here are the loan IDs that matched your search:\n{match_list}\nYou'll be redirected to the main menu.")

    def loan_option_4_info(self):
        print("To get all the information of a specified loan please provide the following:")
        input_info = get_valid_input("Loan ID: ", lambda x: x.strip() != "" and x.isnumeric() and len(x) <= 4,
                    "Input invalid. Must not be empty and must contain only numbers (maximum 4).")
        input_info = int(input_info)
        selected_loan = self.loan_list.get_loans().get(input_info)

        loan_info = {
            "User ID": selected_loan.get_user_id(),
            "Book ID": selected_loan.get_book_id(),
            "Loan date": selected_loan.get_loan_date(),
            "Return date": selected_loan.get_return_date()
        }

        for key, value in loan_info.items():
            print(f"{key}: {value}")
            print("You'll be redirected to the main menu.")

    def loan_option_5_late(self):
        print("To update a loan please provide the following:")
        input_id = get_valid_input("Loan ID: ", lambda x: x.strip() != "" and x.isnumeric() and len(x) <= 4,
                    "Input invalid. Must not be empty and must contain only numbers (maximum 4).")
        input_id = int(input_id)
        selected_loan = self.loan_list.get_loans().get(input_id)

        try:
            self.loan_list.update_loan(selected_loan, *self.get_loan_info())
            print("Loan successfully updated. You'll be redirected to the main menu.")
        except TypeError as e:
            print(f"Error updating loan: try again and make sure your input is in a valid. {e}")

    def loan_option_6_total(self):
        total_loans = self.loan_list.total_loans_collection()
        print(f"The library has a total of {total_loans} loans.")
