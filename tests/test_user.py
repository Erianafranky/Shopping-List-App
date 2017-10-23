import unittest
from classes.user import User

class TestUser(unittest.TestCase):
	"""
	This  includes the tests for the user model
	"""
	def setUp(self):
		self.user = User('Dottie', 'dottie@example.com', 'abc123')

	def test_login(self):
		"""
		user can login with the correct credentials
		"""
		self.assertTrue(self.user.login('Dottie', 'abcdef'))

	def test_incorrect_login(self):
		"""
		test to reject user login if the user login
		with incorrect credentials
		"""
		self.assertFalse(self.user.login('drottie','abcdef'))

	
	
		

