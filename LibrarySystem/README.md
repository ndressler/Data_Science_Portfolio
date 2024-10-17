# In Progress . . .

Missing: Loans section in system.py,<br>
Rewrite unittests and check functionalities manually,<br>
create requirements file.

# Library System

## Table of Contents
- [About the Project](#about-the-project)
- [Task](#tasks-for-analysis)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Functionality](#functionality)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## About the Project

This is a console-based library management system application written in Python. It allows you to manage books, users, and loans in a library.

## Task

The module requires implementing a library record system in Python utilizing object-oriented programming concepts. The system comprises several classes: Books, BookList, Users, UserList, and Loans. For instance, the Books class creates book records with attributes like ID, title, author, etc., along with methods for editing and retrieving these attributes. BookList manages a collection of book instances, allowing search, removal, and counting functionalities. Similarly, Users and UserList classes handle user details and their management. Loans class facilitates book borrowing and returning for users, along with tracking overdue books. Additionally, extra features include command-line interfaces for modifying book and user details.

## Project Structure

LibrarySystem<br>
├── main.py<br>
├── scripts<br>
│   ├── book.py<br>
│   ├── functions.py<br>
│   ├── loan.py<br>
│   ├── system.py<br>
│   └── user.py<br>
├── tests<br>
|   ├── test_book.py<br>
|   ├── test_functions.py<br>
|   ├── test_loan.py<br>
|   ├── test_system.py<br>
|   └── test_user.py<br>
├── scripts/ <br>
├── LICENSE<br>
└── README.md<br>

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ndressler/Data_Science_Portfolio/tree/main/LibrarySystem
   ```

2. Navigate to the project directory:

   ```bash
   cd LibrarySystem
   ```

3. Make sure you have Python installed on your system and install the following dependency:

   ```bash
   pip install tabulate==0.9.0
   ```

4. Set the PYTHONPATH environment variable to the root directory of the project:
   ```bash
   export PYTHONPATH=$(pwd)
   ```

5. Run the application:

   ```bash
   python main.py
   ```

6. Follow the on-screen instructions to interact with the library system.

## Functionality

The math quiz system provides the following functionality:

- Manage Books: You can add, remove, find, update, and get information about books in the library. You can also check the total number of books in the library.

- Manage Users: The system allows you to add, remove, find, update, and get information about users. You can also check the total number of users in the library.

- Manage Loans: You can add, remove, find, and get information about loans. You can also find all late loans and check the total number of loans in the library.

- Exit: exit the system and save the data.

## Future Improvements

- Graphical User Interface (GUI): Create a user-friendly GUI using libraries like Tkinter or PyQt, allowing for intuitive interaction with the system and enhancing the overall user experience.

- Advanced Customization Options: Enhance customization capabilities by implementing features to make the system more robust.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.
