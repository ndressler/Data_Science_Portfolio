import unittest
from datetime import datetime, timedelta
from scripts.loan import Loans, LoanList
from scripts.book import BookList
from scripts.user import UserList

class TestLoans(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.book_list.add_book('book1', 'author1', 2022, 'publisher1', 5, 5, datetime.strptime('01-01-2022', '%d-%m-%Y'))
        self.user_list.add_user('user1', 'name1', 'surname1', '1', 'street1', 'postcode1', 'email@1.com', datetime.strptime('01-01-1990', '%d-%m-%Y'))
        self.loan = Loans('book1', 'user1', self.book_list, self.user_list)

    def test_book_id(self):
        self.assertEqual(self.loan.book_id, 'book1')
        with self.assertRaises(ValueError):
            self.loan.book_id = 'book2'

    def test_username(self):
        self.assertEqual(self.loan.username, 'user1')
        with self.assertRaises(ValueError):
            self.loan.username = 'user2'

    def test_loan_date(self):
        self.assertEqual(self.loan.loan_date.date(), datetime.today().date())
        with self.assertRaises(ValueError):
            self.loan.loan_date = 'invalid date'

    def test_return_date(self):
        self.assertEqual(self.loan.return_date.date(), (datetime.today() + timedelta(days=10)).date())
        with self.assertRaises(ValueError):
            self.loan.return_date = 'invalid date'

class TestLoanList(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loan_list = LoanList()
        self.book_list.add_book('book1', 'author1', 2022, 'publisher1', 5, 5, datetime.strptime('01-01-2022', '%d-%m-%Y'))
        self.user_list.add_user('user1', 'name1', 'surname1', '1', 'street1', 'postcode1', 'email@1.com', datetime.strptime('01-01-1990', '%d-%m-%Y'))

    def test_add_loan(self):
        self.loan_list.add_loan('book1', 'user1', self.book_list, self.user_list)
        self.assertEqual(len(self.loan_list.collection), 1)
        with self.assertRaises(ValueError):
            self.loan_list.add_loan('book2', 'user2', self.book_list, self.user_list)

    def test_find_loan(self):
        self.loan_list.add_loan('book1', 'user1', self.book_list, self.user_list)
        self.assertEqual(len(self.loan_list.find_loan('user1', 'username')), 1)
        with self.assertRaises(KeyError):
            self.loan_list.find_loan('user1', 'invalid')

    def test_remove_loan(self):
        self.loan_list.add_loan('book1', 'user1', self.book_list, self.user_list)
        loan_code = list(self.loan_list.collection.keys())[0]
        self.loan_list.remove_loan('book1', loan_code, self.book_list)
        self.assertEqual(len(self.loan_list.collection), 0)
        with self.assertRaises(ValueError):
            self.loan_list.remove_loan('book2', loan_code, self.book_list)

    def test_total_loans(self):
        self.loan_list.add_loan('book1', 'user1', self.book_list, self.user_list)
        self.assertEqual(self.loan_list.total_loans(), 1)

    def test_late_loans(self):
        self.loan_list.add_loan('book1', 'user1', self.book_list, self.user_list)
        for loan in self.loan_list.collection.values():
            loan.return_date = datetime.now() - timedelta(days=1)
        self.assertEqual(len(self.loan_list.late_loans()), 1)

if __name__ == '__main__':
    unittest.main()
