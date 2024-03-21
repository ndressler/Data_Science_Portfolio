from scripts.quiz import  Quiz, Math
from scripts.user import UserManager

def main():
    user_manager = UserManager()
    user_manager.load_users()
    math_quiz = Quiz(user_manager)

    print("-------------------------------------------------------------")
    print("Welcome to the Math Quiz!")
    print("\nWould you like to:\n")
    print("1. Take the quiz")
    print("2. Check the scores")
    print("3. Exit")
    choice = input("Enter your choice: ")

    while True:
        if choice == '1':
            print("\n\n")
            math_quiz = Math(user_manager)
            user = math_quiz.get_user_info()
            math_quiz.start_quiz(user)
        elif choice == '2':
            print("\n\n")
            math_quiz = Math(user_manager)
            math_quiz.show_scores()
        elif choice == '3':
            users_table = []
            math_quiz.update_scores_file(users_table)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            choice = input("Enter your choice: ")

if __name__ == "__main__":
    main()
