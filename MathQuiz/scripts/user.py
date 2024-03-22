import csv

class User:
    """Represents a user in the quiz system."""

    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.correct_answers = 0
        self.num_questions = 0
        self.percentage = 0

    def increase_score(self):
        self.score += 1

    def increase_correct_answers(self):
        self.correct_answers += 1

    def update_num_questions(self):
        self.num_questions += 1

    def update_percentage(self):
        if self.num_questions == 0:
            return 0
        self.percentage = round(((self.correct_answers / self.num_questions) * 100), 2)

    def __str__(self):
        return f'User(name={self.name}, correct_answers={self.correct_answers}, num_questions={self.num_questions}, score={self.score}, percentage={self.percentage})'

class UserManager:
    """
    Manages the users in the quiz system.

    Attributes:
        users (dict): A dictionary containing the users, where the key is the user's name and the value is the User object.
    """

    def __init__(self):
        self.users = {}
        self.users_file =  'scores.csv'

    def create_user(self, name: str) -> User:
        if name in self.users:
            raise ValueError(f"User {name} already exists.")
        self.users[name] = User(name)
        return self.users[name]

    def get_user(self, name: str) -> User:
        if name not in self.users:
            raise ValueError(f"User {name} does not exist.")
        return self.users[name]

    def calculate_avg_percentage(self) -> float:
        total_perc = sum(user.percentage for user in self.users.values())
        num_users = len(self.users)
        if num_users == 0:
            return 0.0
        return round(total_perc / num_users, 2)

    def load_users(self):
        with open(self.users_file, 'r') as file:
            reader = csv.reader(file)
            try:
                next(reader)
            except StopIteration:
                return

            for row in reader:
                name, correct_answers, num_questions, score, percentage = row
                self.users[name] = User(name)
                self.users[name].correct_answers = int(correct_answers)
                self.users[name].num_questions = int(num_questions)
                self.users[name].score = int(score)
                self.users[name].percentage = float(percentage)

    def save_users(self):
        headers = ['Name', 'Correct Answers', 'Number of Questions', 'Score', 'Percentage']
        users_table = [
            [user.name, user.correct_answers, user.num_questions, user.score, user.percentage]
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
