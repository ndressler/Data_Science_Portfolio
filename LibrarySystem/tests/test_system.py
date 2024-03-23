# FILEPATH: /home/ndressler/code/ndressler/Data_Science_Portfolio/LibrarySystem/tests/test_system.py
import unittest
from unittest.mock import patch, MagicMock
from scripts.system import BookOptions, UserOptions, LoanOptions, LibrarySystem

class TestLibrarySystem(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '4'])
    @patch('scripts.system.BookOptions.book_options')
    def test_start_select_book_options(self, mock_book_options, mock_input):
        book_list = MagicMock()
        user_list = MagicMock()
        loan_list = MagicMock()
        library_system = LibrarySystem(book_list, user_list, loan_list)
        library_system.start_select()
        mock_book_options.assert_called_once()

    @patch('builtins.input', side_effect=['2', '4'])
    @patch('scripts.system.UserOptions.user_options')
    def test_start_select_user_options(self, mock_user_options, mock_input):
        book_list = MagicMock()
        user_list = MagicMock()
        loan_list = MagicMock()
        library_system = LibrarySystem(book_list, user_list, loan_list)
        library_system.start_select()
        mock_user_options.assert_called_once()

    @patch('builtins.input', side_effect=['3', '4'])
    @patch('scripts.system.LoanOptions.loan_options')
    def test_start_select_loan_options(self, mock_loan_options, mock_input):
        book_list = MagicMock()
        user_list = MagicMock()
        loan_list = MagicMock()
        library_system = LibrarySystem(book_list, user_list, loan_list)
        library_system.start_select()
        mock_loan_options.assert_called_once()

    @patch('builtins.input', return_value='')
    def test_start_select_empty_input(self, mock_input):
        book_list = MagicMock()
        user_list = MagicMock()
        loan_list = MagicMock()
        library_system = LibrarySystem(book_list, user_list, loan_list)
        with self.assertRaises(ValueError):
            library_system.start_select()

    @patch('builtins.input', return_value='5')
    def test_start_select_invalid_category(self, mock_input):
        book_list = MagicMock()
        user_list = MagicMock()
        loan_list = MagicMock()
        library_system = LibrarySystem(book_list, user_list, loan_list)
        with self.assertRaises(ValueError):
            library_system.start_select()

class TestBookOptions(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_book_options_add(self, mock_input, mock_print):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        book_options.book_option_1_add = MagicMock()
        book_options.book_options()
        book_options.book_option_1_add.assert_called_once()

    @patch('builtins.input', side_effect=['2'])
    def test_book_options_remove(self, mock_input):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        book_options.book_option_2_remove = MagicMock()
        book_options.book_options()
        book_options.book_option_2_remove.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    def test_book_options_find(self, mock_input):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        book_options.book_option_3_find = MagicMock()
        book_options.book_options()
        book_options.book_option_3_find.assert_called_once()

    @patch('builtins.input', side_effect=['4'])
    def test_book_options_info(self, mock_input):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        book_options.book_option_4_info = MagicMock()
        book_options.book_options()
        book_options.book_option_4_info.assert_called_once()

    @patch('builtins.input', side_effect=['5'])
    def test_book_options_update(self, mock_input):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        book_options.book_option_5_update = MagicMock()
        book_options.book_options()
        book_options.book_option_5_update.assert_called_once()

    @patch('builtins.input', side_effect=['6'])
    def test_book_options_total(self, mock_input):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        book_options.book_option_6_total = MagicMock()
        book_options.book_options()
        book_options.book_option_6_total.assert_called_once()

    @patch('builtins.input', side_effect=['7'])
    def test_book_options_invalid(self, mock_input):
        book_list = MagicMock()
        book_options = BookOptions(book_list)
        with self.assertRaises(ValueError):
            book_options.book_options()

class TestUserOptions(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_user_options_add(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        user_options.user_option_1_add = MagicMock()
        user_options.user_options()
        user_options.user_option_1_add.assert_called_once()

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_user_options_remove(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        user_options.user_option_2_remove = MagicMock()
        user_options.user_options()
        user_options.user_option_2_remove.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_user_options_find(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        user_options.user_option_3_find = MagicMock()
        user_options.user_options()
        user_options.user_option_3_find.assert_called_once()

    @patch('builtins.input', side_effect=['4'])
    @patch('builtins.print')
    def test_user_options_info(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        user_options.user_option_4_info = MagicMock()
        user_options.user_options()
        user_options.user_option_4_info.assert_called_once()

    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_user_options_update(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        user_options.user_option_5_update = MagicMock()
        user_options.user_options()
        user_options.user_option_5_update.assert_called_once()

    @patch('builtins.input', side_effect=['6'])
    @patch('builtins.print')
    def test_user_options_total(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        user_options.user_option_6_total = MagicMock()
        user_options.user_options()
        user_options.user_option_6_total.assert_called_once()

    @patch('builtins.input', side_effect=['7'])
    @patch('builtins.print')
    def test_user_options_invalid(self, mock_input, mock_print):
        user_list = MagicMock()
        user_options = UserOptions(user_list)
        with self.assertRaises(ValueError):
            user_options.user_options()

class TestLoanOptions(unittest.TestCase):
    def setUp(self):
        self.loan_list = MagicMock()
        self.loan_options = LoanOptions(self.loan_list)

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_loan_options_invalid_input(self, mock_input):
        self.loan_options.loan_option_1_add = MagicMock()
        try:
            self.loan_options.loan_options()
        except ValueError:
            pass
        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', return_value='2')
    def test_loan_options_remove(self, mock_input):
        self.loan_options.loan_option_2_remove = MagicMock()
        self.loan_options.loan_options()
        self.loan_options.loan_option_2_remove.assert_called_once()

    @patch('builtins.input', return_value='3')
    def test_loan_options_find(self, mock_input):
        self.loan_options.loan_option_3_find = MagicMock()
        self.loan_options.loan_options()
        self.loan_options.loan_option_3_find.assert_called_once()

    @patch('builtins.input', return_value='4')
    def test_loan_options_info(self, mock_input):
        self.loan_options.loan_option_4_info = MagicMock()
        self.loan_options.loan_options()
        self.loan_options.loan_option_4_info.assert_called_once()

    @patch('builtins.input', return_value='5')
    def test_loan_options_update(self, mock_input):
        self.loan_options.loan_option_5_update = MagicMock()
        self.loan_options.loan_options()
        self.loan_options.loan_option_5_update.assert_called_once()

    @patch('builtins.input', return_value='6')
    def test_loan_options_total(self, mock_input):
        self.loan_options.loan_option_6_total = MagicMock()
        self.loan_options.loan_options()
        self.loan_options.loan_option_6_total.assert_called_once()

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_loan_options_invalid_input(self, mock_input):
        self.loan_options.loan_option_1_add = MagicMock()
        self.loan_options.loan_options()
        self.assertEqual(mock_input.call_count, 2)

if __name__ == '__main__':
    unittest.main()
