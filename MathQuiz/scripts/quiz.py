import random
import csv
from tabulate import tabulate
from scripts.user import User

class Quiz:
    """Represents a quiz system.

    Attributes:
        HEADERS (list): A list of column headers for the scores table.
        users (dict): A dictionary of users participating in the quiz.
        user_manager (UserManager): An instance of the UserManager class.

    Methods:
        __init__(self, user_manager): Initializes a Quiz object.
        add_user(self, user): Adds a user to the quiz.
        update_scores_file(self, users_table): Updates the scores file with the latest scores.
        show_scores(self, users_table): Displays the scores table and average score.

    """

    HEADERS = ['Name', 'Correct Answers', 'Number of Questions', 'Score', 'Percentage']

    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.users = user_manager.users

    def add_user(self, user: User):
        self.users[user.name] = user

    def update_scores_file(self, users_table):
        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.HEADERS)
            writer.writerows(users_table)

    def reset_scores(self):
        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.HEADERS)
        self.users.clear()

class Math(Quiz):
    """Represents a math quiz system.

    This class provides methods to interact with the user and conduct a math quiz.
    It inherits from the `Quiz` class.

    Attributes:
        None

    Methods:
        get_user_info: Prompts the user for their name and the number of questions they want to solve.
        generate_question: Generates a math question with random numbers and operators.
        get_user_answer: Prompts the user to enter their answer for a given question.
        show_final_score: Displays the final score and results of the quiz.
        start_quiz: Starts the math quiz for a given user.

    """

    def get_user_info(self) -> User:
        print("To start the quiz please enter your name.")
        while True:
            name = input("Name: ")
            if name.strip():
                break
            else:
                print("Name cannot be empty.\n")

        user = User(name)

        print(f"\nHi {name}, ready to start your math quiz?\nRemember, if your answer is a decimal number, it must be rounded to two decimal points.")

        while True:
            nq = input("Select the number of questions you would like to solve: ")
            if nq.isnumeric():
                user.num_questions = int(nq)
                break
            else:
                print("\nYou must provide a number of questions.\n")

        return user

    def generate_question(self) -> tuple[str, float]:
        operators = ['+', '-', '*', '/']
        while True:
            try:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                num3 = random.randint(1, 100)
                operator1 = random.choice(operators)
                operator2 = random.choice(operators)
                question = f"{num1} {operator1} {num2} {operator2} {num3}"
                correct_answer = round(eval(question), 2)
                return question, correct_answer
            except ZeroDivisionError:
                pass

    def get_user_answer(self, question: str) -> float:
        while True:
            answer = input(f"\nWhat is {question}?\nYour answer: ")
            if answer.strip():
                try:
                    return float(answer)
                except ValueError:
                    print("Invalid answer, try again.")
            else:
                print("Answer cannot be empty.\n")

    def show_scores(self):
        users_table = [
            [user.name, user.correct_answers, user.num_questions, user.score, user.percentage]
            for user in self.users.values()]
        users_table = sorted(users_table, key=lambda x: x[3], reverse=True)

        self.update_scores_file(users_table)

        print(tabulate(users_table, headers=self.HEADERS, tablefmt="grid"))
        print(f"Average Score: {self.user_manager.calculate_avg_percentage()}%\n")

    def show_final_score(self, user: User):
        print(f"Well done {user.name}, you have finished the quiz! Here are your results:")
        print(f"Number of questions: {user.num_questions}")
        print(f"Correctly answered: {user.correct_answers}")
        print(f"Your final score: {user.score}")
        print(f"Percentage score: {user.percentage}%\n")

    def exit_quiz(self):
        users_table = []
        self.update_scores_file(users_table)

    def start_quiz(self, user: User):
        for _ in range(user.num_questions):
            question, correct_answer = self.generate_question()
            user_answer = self.get_user_answer(question)
            if user_answer == correct_answer:
                print("\nYou have answered correctly!\n")
                user.increase_score()
                user.increase_correct_answers()
            else:
                print(f"\nYour answer was incorrect. The correct answer is {correct_answer}.")

        user.update_percentage()
        print(f"Your score so far is: {user.score} out of {user.num_questions}.\n")

        self.show_final_score(user)
        self.user_manager.update_user(user)
        self.user_manager.save_users()

        while True:
            again_quit = input("Would anyone else like to take the quiz? [y/n]")
            print("\n")
            if again_quit.lower() == 'y':
                break
            elif again_quit.lower() == 'n':
                self.show_scores()
                return
            else:
                print("Invalid answer. Please enter 'y' for yes or 'n' for no.\n")
