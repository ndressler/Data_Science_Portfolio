import random
import csv
from tabulate import tabulate
from scripts.user import User

class Quiz:
    """Represents a quiz system."""

    HEADERS = ['Name', 'Correct Answers', 'Number of Questions', 'Score']

    def __init__(self, user_manager):
        self.users = {}
        self.user_manager = user_manager
        self.users = user_manager.users

    def add_user(self, user: User):
        self.users[user.name] = user

    def update_scores_file(self, users_table):
        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.HEADERS)
            writer.writerows(users_table)

    def show_scores(self,users_table):
        users_table = [
            [user.name, user.score, user.num_questions, self.calculate_percentage(user.score, user.num_questions)]
            for user in self.users.values()]
        users_table = sorted(users_table, key=lambda x: x[3], reverse=True)

        self.update_scores_file(users_table)

        if users_table:
            avg_score = sum(row[3] for row in users_table) / len(users_table)
        else:
            avg_score = 0

        print(tabulate(users_table, headers=self.HEADERS, tablefmt="grid"))
        print(f"Average Score: {round(avg_score, 2)}%\n")


class Math(Quiz):
    """Represents a math quiz system."""

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
                operator1 = random.choice(operators)
                operator2 = random.choice(operators)
                question = f"{num1} {operator1} {num2} {operator2} {num1}"
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

    def show_final_score(self, user: User):
        print(f"Well done {user.name}, you have finished the quiz! Here are your results:")
        print(f"Number of questions: {user.num_questions}")
        print(f"Correctly answered: {user.score}")
        print(f"Your final score: {self.user_manager.calculate_percentage(user.score, user.num_questions)}\n")

    def start_quiz(self, user: User):
        while True:
            for _ in range(user.num_questions):
                question, correct_answer = self.generate_question()
                user_answer = self.get_user_answer(question)
                if user_answer == correct_answer:
                    print("\nYou have answered correctly!\n")
                    user.increase_score()
                else:
                    print(f"\nYour answer was incorrect. The correct answer is {correct_answer}.")
                print(f"Your score so far is: {user.score} out of {user.num_questions}.\n")

            self.show_final_score(user)
            self.user_manager.update_user(user)

            again_quit = input("Would anyone else like to take the quiz? [y/n]")
            print("\n")
            if again_quit.lower() == 'y':
                user.num_questions = 0
                break
            elif again_quit.lower() == 'n':
                self.show_scores()
                return
            else:
                print("Invalid answer. Please enter 'y' for yes or 'n' for no.\n")
