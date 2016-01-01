import unittest


class BookAppTestCase(unittest.TestCase):
    """shared functionality"""

    def setUp(self):
        from bookdb import database
        self.db = database


class BookDBTestCase(BookAppTestCase):
    """tests for the bookdb code"""

    def makeOne(self):
        from bookdb import BookDB
        return BookDB()

    def test_all_titles_returned(self):
        actual_titles = self.makeOne().titles()
        self.assertEqual(len(actual_titles), len(self.db))

    def test_all_titles_correct(self):
        actual_titles = self.makeOne().titles()
        for actual_title in actual_titles:
            self.assertTrue(actual_title['id'] in self.db)
            actual = actual_title['title']
            expected = self.db[actual_title['id']]['title']
            self.assertEqual(actual, expected)

    def test_title_info_complete(self):
        use_id, expected = self.db.items()[0]
        actual = self.makeOne().title_info(use_id)
        # demonstrate all actual keys are expected
        for key in actual:
            self.assertTrue(key in expected)
        # demonstrate all expected keys are present in actual
        for key in expected:
            self.assertTrue(key in actual)

    def test_title_info_correct(self):
        for book_id, expected in self.db.items():
            actual = self.makeOne().title_info(book_id)
            self.assertEqual(actual, expected)


class ResolvePathTestCase(BookAppTestCase):
    """tests for the resolve_path function"""

    def call_function_under_test(self, path):
        from bookapp import resolve_path
        return resolve_path(path)

    def test_root_returns_books_function(self):
        """verify that the correct function is returned by the root path"""
        from bookapp import books as expected
        path = '/'
        actual, args = self.call_function_under_test(path)
        self.assertTrue(actual is expected)

    def test_root_returns_no_args(self):
        """verify that no args are returned for the root path"""
        path = '/'
        func, actual = self.call_function_under_test(path)
        self.assertTrue(not actual)

    def test_book_path_returns_book_function(self):
        from bookapp import book as expected
        book_id = self.db.keys()[0]
        path = '/book/{0}'.format(book_id)
        actual, args = self.call_function_under_test(path)
        self.assertTrue(actual is expected)

    def test_book_path_returns_bookid_in_args(self):
        expected = self.db.keys()[0]
        path = '/book/{0}'.format(expected)
        func, actual = self.call_function_under_test(path)
        self.assertTrue(expected in actual)

    def test_bad_path_raises_name_error(self):
        path = '/not/valid/path'
        self.assertRaises(NameError, self.call_function_under_test, path)


class BooksTestCase(BookAppTestCase):
    """tests for the books function"""

    def call_function_under_test(self):
        from bookapp import books
        return books()

    def test_all_book_titles_in_result(self):
        actual = self.call_function_under_test()
        for book_id, info in self.db.items():
            expected = info['title']
            self.assertTrue(expected in actual)

    def test_all_book_ids_in_result(self):
        actual = self.call_function_under_test()
        for expected in self.db:
            self.assertTrue(expected in actual)


class BookTestCase(BookAppTestCase):
    """tests for the book function"""

    def call_function_under_test(self, id):
        from bookapp import book
        return book(id)

    def test_all_ids_have_results(self):
        for book_id in self.db:
            actual = self.call_function_under_test(book_id)
            self.assertTrue(actual)

    def test_id_returns_correct_results(self):
        for book_id, book_info in self.db.items():
            actual = self.call_function_under_test(book_id)
            for expected in book_info.values():
                self.assertTrue(expected in actual)

    def test_bad_id_raises_name_error(self):
        bad_id = "sponge"
        self.assertRaises(NameError, self.call_function_under_test, bad_id)


if __name__ == '__main__':
    unittest.main()
