from scripts.user import Users, UserList
import unittest

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.user = Users("jdoe", "John", "Doe", "123", "Main St", "12345", "jdoe@example.com", "01-01-1990")

    def test_username(self):
        self.assertEqual(self.user.username, "jdoe")
        self.user.username = "newuser"
        self.assertEqual(self.user.username, "newuser")
        with self.assertRaises(ValueError):
            self.user.username = ""

    def test_firstname(self):
        self.assertEqual(self.user.firstname, "John")
        self.user.firstname = "Jane"
        self.assertEqual(self.user.firstname, "Jane")
        with self.assertRaises(ValueError):
            self.user.firstname = ""

    def test_surname(self):
        self.assertEqual(self.user.surname, "Doe")
        self.user.surname = "Smith"
        self.assertEqual(self.user.surname, "Smith")
        with self.assertRaises(ValueError):
            self.user.surname = ""

    def test_house_number(self):
        self.assertEqual(self.user.house_number, "123")
        self.user.house_number = "456"
        self.assertEqual(self.user.house_number, "456")
        with self.assertRaises(ValueError):
            self.user.house_number = "abc"

    def test_street_name(self):
        self.assertEqual(self.user.street_name, "Main St")
        self.user.street_name = "Second St"
        self.assertEqual(self.user.street_name, "Second St")

    def test_postcode(self):
        self.assertEqual(self.user.postcode, "12345")
        self.user.postcode = "67890"
        self.assertEqual(self.user.postcode, "67890")
        with self.assertRaises(ValueError):
            self.user.postcode = "abc"

    def test_email_address(self):
        self.assertEqual(self.user.email_address, "jdoe@example.com")
        self.user.email_address = "jane@example.com"
        self.assertEqual(self.user.email_address, "jane@example.com")
        # Assuming validate_email raises ValueError for invalid emails
        with self.assertRaises(ValueError):
            self.user.email_address = "invalid"

    def test_date_birth(self):
        self.assertEqual(self.user.date_birth, "01-01-1990")
        self.user.date_birth = "02-02-1992"
        self.assertEqual(self.user.date_birth, "02-02-1992")
        # Assuming parse_date raises ValueError for invalid dates
        with self.assertRaises(ValueError):
            self.user.date_birth = "invalid"

    def test_str(self):
        self.assertEqual(str(self.user), "User(jdoe, John, Doe, 123, Main St, 12345, jdoe@example.com, 01-01-1990)")

class TestUserList(unittest.TestCase):

    def setUp(self):
        self.user_list = UserList()
        self.user_list.add_user("jdoe", "John", "Doe", "123", "Main St", "12345", "jdoe@example.com", "01-01-1990")

    def test_add_user(self):
        self.user_list.add_user("jsmith", "Jane", "Smith", "456", "Second St", "67890", "jsmith@example.com", "02-02-1992")
        self.assertEqual(self.user_list.total_users_collection(), 2)
        self.assertEqual(self.user_list.get_user("jsmith").username, "jsmith")

    def test_remove_user(self):
        self.user_list.remove_user("John")
        self.assertEqual(self.user_list.total_users_collection(), 0)
        with self.assertRaises(ValueError):
            self.user_list.get_user("jdoe")

    def test_total_users_collection(self):
        self.assertEqual(self.user_list.total_users_collection(), 1)

    def test_get_user(self):
        user = self.user_list.get_user("jdoe")
        self.assertEqual(user.username, "jdoe")
        with self.assertRaises(ValueError):
            self.user_list.get_user("nonexistentuser")

if __name__ == '__main__':
    unittest.main()
