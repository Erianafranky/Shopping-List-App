import unittest
from app.classes.user import User

class TestUser(unittest.TestCase):
	"""
	This  includes the tests for the user model
	"""
	def setUp(self):
		self.user = User('dottie', 'dottie@example.com', 'abcdefg')

	def test_correct_login(self):
		"""
		user can login with the correct credentials
		"""
		self.assertFalse(self.user.login('Dottie', 'abcdef'))
		

	def test_incorrect_login(self):
		"""
		test to reject user login if the user login
		with incorrect credentials
		"""
		self.assertFalse(self.user.login('Drottie', 'fedcba'))

	def test_create_shopping_list(self):
		"""
		user create shoppinglist
		"""
		self.user.create_shopping_list('groceries')
		self.assertEqual(self.user.shopping_lists, ['groceries'])

	def test_delete_shopping_list(self):
		"""
		user can delete their shoppinglist
		the list should exist in their shoppinglist 
		before it's deleted
		"""
		self.user.shopping_lists.append('list1')
		self.user.shopping_lists.append('list2')
		self.user.delete_shopping_list('list1')
		self.assertEqual(self.user.shopping_lists, ['list2'])

	def test_view_shopping_list(self):
		"""
		User can view shoppinglist created
		"""
		self.user.shopping_lists.append('list1')
		self.assertEqual(self.user.view_shopping_list(),['list1'])


	
	
		

