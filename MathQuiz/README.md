# Math Quiz

## Table of Contents
- [About the Project](#about-the-project)
- [Tasks](#tasks-for-analysis)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Functionality](#functionality)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## About the Project

This is a console-based quiz application written in Python. It allows users to take a math quiz consisting of 10 questions, with the option to extend the quiz to any number of questions. The program keeps track of users' scores, displays their results, and provides additional features such as randomizing question order and showing correct/incorrect answers.

## Tasks

- Produce a program from the console (command line)
- You can produce a quiz which can ask any number of questions (i.e. user can specify the number of questions they wan to answer, e.g., 15 questions)
- The system displays random questions
- Asks the user their name
- Runs through all questions of the quiz and keep a running score of the number of correctly questions answered
- Once the users has answered all the questions, the system should print out their score as well as a percentage score on the screen
- The program should then prompt to ask if anybody else wants to take the quiz. It should then perform the same steps for the next user
- Once all the users have finished the quiz, the program displays:
  - The name of the user with the highest score (as well as other users’ score).
  - The average score percentage of all users
- You should make use of conditional statements, iterative statements, functions, data structures etc. in your program
- Your program should suitably handle user errors (e.g., incorrect input type, such as empty answer or name etc.)


## Project Structure

MathQuiz/
├── main.py            # Entry point of the program
└── scripts/
│   ├── __init__.py    # Initialization file
│   ├── quiz.py        # Module containing quiz-related functions
│   └── user.py        # Module containing user-related functions
├── LICENSE<br>
└── README.md                              # You are here<br>


## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ndressler/Data_Science_Portfolio/tree/main/MathQuiz
   ```

2. Navigate to the project directory:

   ```bash
   cd MathQuiz
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

6. Follow the on-screen instructions to interact with the math quiz system.

## Functionality

The math quiz system provides the following functionality:

- Start Quiz: Start a math quiz session.
- Show Scores: Display the scores of all users who have taken the quiz.
- Reset Scores: Reset all scores and start fresh.
- Exit: Exit the program.

## Future Improvements

- Automated Testing Suite: Develop an automated testing suite using frameworks like pytest or unittest to thoroughly test the quiz system's functionality, ensuring reliability and stability across updates.

- Graphical User Interface (GUI): Create a user-friendly GUI using libraries like Tkinter or PyQt, allowing for intuitive interaction with the quiz system and enhancing the overall user experience.

- Advanced Customization Options: Enhance customization capabilities by implementing features to create custom question sets, set specific difficulty levels, and adjust parameters such as time limits and scoring criteria, empowering users to tailor quizzes to their unique preferences and learning goals.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
