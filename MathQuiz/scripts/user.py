import csv

class User:
    """Represents a user in the quiz system."""

    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.num_questions = 0

    def increase_score(self):
        self.score += 1

    def update_num_questions(self):
        self.num_questions += 1

    def reset(self):
        self.score = 0
        self.num_questions = 0

    def __str__(self):
        return f'User(name={self.name}, score={self.score}, num_questions={self.num_questions})'


class UserManager:
    """Manages the users in the quiz system."""

    def __init__(self):
        self.users = {}

    def create_user(self, name: str) -> User:
        if name in self.users:
            raise ValueError(f"User {name} already exists.")
        self.users[name] = User(name)
        return self.users[name]

    def get_user(self, name: str) -> User:
        if name not in self.users:
            raise ValueError(f"User {name} does not exist.")
        return self.users[name]

    def calculate_percentage(self, correct_answers: int, num_questions: int) -> float:
        if num_questions == 0:
            return 0.0
        return round((correct_answers / num_questions * 100), 2)

    def load_users(self):
        try:
            with open('scores.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    name, correct_answers, num_questions, _ = row
                    self.users[name] = User(name)
                    self.users[name].score = int(correct_answers)
                    self.users[name].num_questions = int(num_questions)
        except FileNotFoundError:
            pass

    def save_users(self):
        headers = ['Name', 'Correct Answers', 'Number of Questions', 'Score']
        users_table = [
            [user.name, user.score, user.num_questions, self.calculate_percentage(user.score, user.num_questions)]
            for user in self.users.values()]
        users_table = sorted(users_table, key=lambda x: x[3], reverse=True)

        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(users_table)

        return users_table

    def update_user(self, user: User):
        self.users[user.name] = user
        self.save_users()
