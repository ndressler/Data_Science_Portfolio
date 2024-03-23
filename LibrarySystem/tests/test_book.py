import unittest
from scripts.book import Books, BookList

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.book = Books("Test Title", "Test Author", 2000, "Test Publisher", 10, 5, "2000-01-01")

    def test_init(self):
        self.assertEqual(self.book.title, "test title")
        self.assertEqual(self.book.author, "test author")
        self.assertEqual(self.book.year, 2000)
        self.assertEqual(self.book.publisher, "test publisher")
        self.assertEqual(self.book.total_num_copies, 10)
        self.assertEqual(self.book.num_available_copies, 5)
        self.assertEqual(self.book.publication_date, "2000-01-01")

    def test_title_setter(self):
        with self.assertRaises(ValueError):
            self.book.title = ""

    def test_author_setter(self):
        with self.assertRaises(ValueError):
            self.book.author = ""

    def test_year_setter(self):
        with self.assertRaises(ValueError):
            self.book.year = "not a number"

    def test_publisher_setter(self):
        with self.assertRaises(ValueError):
            self.book.publisher = ""

    def test_total_num_copies_setter(self):
        with self.assertRaises(ValueError):
            self.book.total_num_copies = "not a number"

    def test_num_available_copies_setter(self):
        with self.assertRaises(ValueError):
            self.book.num_available_copies = "not a number"
        with self.assertRaises(ValueError):
            self.book.num_available_copies = 11

    def test_publication_date_setter(self):
        with self.assertRaises(ValueError):
            self.book.publication_date = "not a date"

class TestBookList(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.book_list.add_book("Test Title", "Test Author", 2000, "Test Publisher", 10, 5, "2000-01-01")

    def test_add_book(self):
        self.book_list.add_book("New Title", "New Author", 2001, "New Publisher", 20, 10, "2001-01-01")
        self.assertEqual(self.book_list.total_books_collection(), 2)

    def test_add_book_invalid(self):
        with self.assertRaises(ValueError):
            self.book_list.add_book("", "", "not a number", "", "not a number", "not a number", "not a date")

    def test_find_book(self):
        book_ids = self.book_list.find_book("Test Title", "title")
        self.assertEqual(len(book_ids), 1)

    def test_find_book_invalid_search_type(self):
        with self.assertRaises(KeyError):
            self.book_list.find_book("Test Title", "invalid_search_type")

    def test_remove_book(self):
        self.book_list.remove_book("Test Title")
        self.assertEqual(self.book_list.total_books_collection(), 0)

    def test_remove_book_not_found(self):
        with self.assertRaises(KeyError):
            self.book_list.remove_book("Nonexistent Title")

    def test_total_books_collection(self):
        self.assertEqual(self.book_list.total_books_collection(), 1)

if __name__ == "__main__":
    unittest.main()
