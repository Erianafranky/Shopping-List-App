import unittest
from app.classes import ShoppingList
class TestShoppingList(unittest.TestCase):
	"""
	This includes the tests for the shoppinglist model
	"""

	def setUp(self):
		self.shopping_list = ShoppingList('groceries')

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

	def test_view_item_in_shopping_list(self):
		"""
		view shopping list with items
		"""
		self.shopping_list.items.append('tomato')
		self.assertEqual(self.shopping_list.view_shopping_list(), ['tomato'])

	def test_delete_item_in_shopping_list(self):
		"""
		adds item then delete one of the items
		"""
		self.shopping_list.items.append('sugar')
		self.shopping_list.items.append('tea')
		self.shopping_list.delete_item_in_shopping_list('tea')		
		self.assertEqual(self.shopping_list.items, ['sugar'])

	def test_delete_item_not_in_shopping_list(self):
		"""
		deletes item that is not in the shopping list
		"""
		self.assertRaises(ValueError, self.shopping_list.delete_item_in_shopping_list, 'biscuits')

	def test_add_item_to_shopping_list(self):
	    """
	    adds item to shoppinglist with items
	    """
	    self.shopping_list.items.append('milk')
	    self.shopping_list.add_item_to_shopping_list('tea')
	    self.assertEqual(self.shopping_list.items, ['milk', 'tea'])

	def test_add_item_to_empty_shopping_list(self):
	    """
	    adds item to an empty shopping list
	    """
	    self.shopping_list.add_item_to_shopping_list('sweets')
	    self.assertEqual(self.shopping_list.items, ['sweets'])

