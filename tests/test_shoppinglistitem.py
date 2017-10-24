import unittest
from app.classes import ShoppingItem

class TestShoppingItem(unittest.TestCase):
	"""
	this includes the test for the shopping items model
	"""

	def setUp(self):
		self.shopping_list = ShoppingList('groceries')
		self.shopping_item = ShoppingItem('milk', 2, 'units')

	
