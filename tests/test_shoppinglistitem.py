import unittest
from app.classes.shopping_item import ShoppingItem

class TestShoppingItem(unittest.TestCase):
	"""
	this includes the test for the shopping items model
	"""

	def setUp(self):
		self.shopping_item = ShoppingItem('milk', 2, 'units')

	
