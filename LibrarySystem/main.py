
from scripts.user import UserList
from scripts.book import BookList
from scripts.loan import LoanList
from scripts.system import LibrarySystem
from scripts.functions import save_to_csv, load_from_csv

def main():
    # create instances of the classes
    book_list = BookList()
    user_list = UserList()
    loan_list = LoanList()

    # load data from the CSV files
    user_list.user_load_from_csv()
    book_list.book_load_from_csv()
    loan_list.loan_load_from_csv(book_list, user_list)

    # create an instance of the LibrarySystem class
    library_system = LibrarySystem(book_list, user_list, loan_list)

    # start the library system
    exit_program = False
    while not exit_program:
        library_system.start_select()
        while True:
            continue_quit = input("Would you like to do another operation? Press 'n' to exit: [y/n]")
            if continue_quit.lower() == "y":
                break
            elif continue_quit.lower() == "n":
                # save data to the CSV files
                user_list.user_save_to_csv()
                book_list.book_save_to_csv()
                loan_list.loan_save_to_csv()
                print("Exiting the library system.")
                exit_program = True
                break
            else:
                print("Please answer with 'y' for yes and 'n' for no.")



if __name__ == '__main__':
    main()
