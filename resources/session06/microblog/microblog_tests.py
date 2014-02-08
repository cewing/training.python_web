import os
import tempfile
import unittest
from flask import session


import microblog


class MicroblogTestCase(unittest.TestCase):

    def setUp(self):
        db_fd = tempfile.mkstemp()
        self.db_fd, microblog.app.config['DATABASE'] = db_fd
        microblog.app.config['TESTING'] = True
        self.client = microblog.app.test_client()
        self.app = microblog.app
        microblog.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(microblog.app.config['DATABASE'])

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout',
                               follow_redirects=True)

    def test_database_setup(self):
        con = microblog.connect_db()
        cur = con.execute('PRAGMA table_info(entries);')
        rows = cur.fetchall()
        self.assertEquals(len(rows), 3)

    def test_write_entry(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            microblog.write_entry(*expected)
            con = microblog.connect_db()
            cur = con.execute("select * from entries;")
            rows = cur.fetchall()
        self.assertEquals(len(rows), 1)
        for val in expected:
            self.assertTrue(val in rows[0])

    def test_get_all_entries_empty(self):
        with self.app.test_request_context('/'):
            entries = microblog.get_all_entries()
            self.assertEquals(len(entries), 0)

    def test_get_all_entries(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            microblog.write_entry(*expected)
            entries = microblog.get_all_entries()
            self.assertEquals(len(entries), 1)
            for entry in entries:
                self.assertEquals(expected[0], entry['title'])
                self.assertEquals(expected[1], entry['text'])

    def test_empty_listing(self):
        response = self.client.get('/')
        assert 'No entries here so far' in response.data

    def test_listing(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            microblog.write_entry(*expected)
        response = self.client.get('/')
        for value in expected:
            assert value in response.data

    def test_login_passes(self):
        with self.app.test_request_context('/'):
            microblog.do_login(microblog.app.config['USERNAME'],
                               microblog.app.config['PASSWORD'])
            self.assertTrue(session.get('logged_in', False))

    def test_login_fails(self):
        with self.app.test_request_context('/'):
            self.assertRaises(ValueError,
                              microblog.do_login,
                              microblog.app.config['USERNAME'],
                              'incorrectpassword')

    def test_login_logout(self):
        # verify we can log in
        response = self.login('admin', 'secret')
        assert 'You were logged in' in response.data
        # verify we can log back out
        response = self.logout()
        assert 'You were logged out' in response.data
        # verify that incorrect credentials get a proper message
        response = self.login('notadmin', 'secret')
        assert 'Invalid Login' in response.data
        response = self.login('admin', 'notsosecret')
        assert 'Invalid Login' in response.data

    def test_add_entries(self):
        self.login('admin', 'secret')
        response = self.client.post('/add', data=dict(
            title='Hello',
            text='This is a post'
        ), follow_redirects=True)
        assert 'No entries here so far' not in response.data
        assert 'Hello' in response.data
        assert 'This is a post' in response.data


if __name__ == '__main__':
    unittest.main()
