import unittest
from scripts.user import User, UserManager

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("TestUser")

    def test_increase_score(self):
        self.user.increase_score()
        self.assertEqual(self.user.score, 1)

    def test_update_num_questions(self):
        self.user.update_num_questions()
        self.assertEqual(self.user.num_questions, 1)

    def test_reset(self):
        self.user.increase_score()
        self.user.update_num_questions()
        self.user.reset()
        self.assertEqual(self.user.score, 0)
        self.assertEqual(self.user.num_questions, 0)

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_create_user(self):
        user = self.user_manager.create_user("TestUser")
        self.assertEqual(user.name, "TestUser")
        self.assertEqual(user.score, 0)
        self.assertEqual(user.num_questions, 0)

    def test_get_user(self):
        self.user_manager.create_user("TestUser")
        user = self.user_manager.get_user("TestUser")
        self.assertEqual(user.name, "TestUser")

    def test_create_existing_user(self):
        self.user_manager.create_user("TestUser")
        with self.assertRaises(ValueError):
            self.user_manager.create_user("TestUser")

    def test_get_nonexistent_user(self):
        with self.assertRaises(ValueError):
            self.user_manager.get_user("NonexistentUser")

if __name__ == "__main__":
    unittest.main()
