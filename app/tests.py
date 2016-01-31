import os
import unittest

from server import app, basedir, db


TEST_DB = 'test.db'


class BasicTestCase(unittest.TestCase):
    def setUp(self):
    	"""Set up a blank temp database before each test"""
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
    	"""Destroy blank temp database after each test"""
        db.session.remove()
        db.drop_all()

    def login(self, username, password):
        """Login helper function"""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        """Logout helper function"""
        return self.app.get('/logout', follow_redirects=True)


class IndexTestCase(BasicTestCase):

	def test_index(self):
		"""inital test. ensure flask was set up correctly"""
		response = self.app.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	def test_database(self):
		"""inital test. ensure that the database exists"""
        tester = os.path.exists("flaskr.db")
        self.assertTrue(tester)
