class ShoppingList(object):
	"""
	class modelling a shopping list
	"""
	def __init__(self, name, items=None, shopping_lists=None):
		self.name = name
		self.items = items
		self.shopping_lists=shopping_lists or []

	def add_item_to_shopping_list(self,item):
		"""
		adds an item to a shopping list
		"""
		self.items.append(item)

	def delete_item_from_shopping_list(self, item):
		"""
		deletes an item from shopping list
		"""
		if item in self.items:
			self.items.remove(item)
		else:
			raise ValueError

	def view_item_from_shopping_list(self):
		"""
		view shopping list
		"""
		return self.items

	
		
