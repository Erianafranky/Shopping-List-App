import unittest
from app.classes.shopping_list import ShoppingList
class TestShoppingList(unittest.TestCase):
	"""
	This includes the tests for the shoppinglist model
	"""

	def setUp(self):
		self.shoppinglist = ShoppingList('User')

	def test_view_item_in_shopping_list(self):
		"""
		view shopping list with items
		"""
		self.shoppinglist.items.append('tomato')
		self.assertEqual(self.shoppinglist.view_shopping_list(), ['tomato'])

	def test_delete_item_from_shopping_list(self):
		"""
		adds item then delete one of the items
		"""
		self.shoppinglist.items.append('sugar')
		self.shoppinglist.items.append('tea')
		self.shoppinglist.delete_item_from_shopping_list('tea')		
		self.assertEqual(self.shoppinglist.items, ['sugar'])

	def test_delete_item_not_in_shopping_list(self):
		"""
		deletes item that is not in the shopping list
		"""
		self.assertRaises(ValueError, self.shoppinglist.delete_item_from_shopping_list, 'biscuits')

	def test_add_item_to_shopping_list(self):
	    """
	    adds item to shoppinglist with items
	    """
	    self.shoppinglist.items.append('milk')
	    self.shoppinglist.add_item_to_shopping_list('tea')
	    self.assertEqual(self.shoppinglist.items, ['milk', 'tea'])

	
