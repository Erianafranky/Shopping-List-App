import unittest
import sys
from classes.shopping_item import ShoppingItem

class TestShoppingItem(unittest.TestCase):
	"""
	this includes the test for the shopping items model
	"""

	def setUp(self):
		self.shopping_list = ShoppingList('groceries')
		self.shopping_item = ShoppingItem('milk', 2, 'units')

	
