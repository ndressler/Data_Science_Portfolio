from scripts.quiz import  Quiz, Math
from scripts.user import UserManager

def main():
    user_manager = UserManager()
    user_manager.load_users()
    math_quiz = Math(user_manager)

    while True:
        print("-------------------------------------------------------------")
        print("Welcome to the Math Quiz!")
        print("\nWould you like to:\n")
        print("1. Start Quiz")
        print("2. Show Scores")
        print("3. Reset Scores")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n\n")
            user = math_quiz.get_user_info()
            math_quiz.start_quiz(user)
        elif choice == '2':
            print("\n\n")
            math_quiz.show_scores()
        elif choice == '3':
            math_quiz.reset_scores()
            math_quiz = Math(user_manager)
        elif choice == '4':
            users_table = []
            math_quiz.update_scores_file(users_table)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            choice = input("Enter your choice: ")

if __name__ == "__main__":
    main()
