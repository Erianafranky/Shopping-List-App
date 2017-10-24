import unittest
from app.classes.user import User

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

	def test_create_shopping_list(self):
		"""
		user create shoppinglist
		"""
		shopping_list = self.user.create_shopping_list('groceries')
		self.assertIn(shopping_list, self.user.shopping_lists)

	def test_delete_shopping_list(self):
		"""
		user can delete their shoppinglist
		the list should exist in their shoppinglist 
		before it's deleted
		"""
		user2 = User('Olive' 'olive@example.com', 'olivejane')
		user_shopping_list = self.user.create_shopping_list('groceries')
		user2_shopping_list = self.user2.create_shopping_list('home accessories')
		self.user.delete_shopping_list(user_shopping_list)
		self.assertNotIn(user_shopping_list, self.user.shopping_lists)

	def test_view_shopping_list(self):
		"""
		User can view shoppinglist created
		"""
		user2 = User('Olive' 'olive@example.com', 'olivejane')
		user_shopping_list = self.user.create_shopping_list('groceries')
		user2_shopping_list = self.user2.create_shopping_list('home accessories')
		self.user.view_shopping_list(user_shopping_list)
		self.assertIn(user_shopping_list, self.user.shopping_lists)


	
	
		

