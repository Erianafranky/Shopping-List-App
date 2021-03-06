class ShoppingList(object):
	"""
	class modelling a shopping list
	"""
	def __init__(self, name, items=None):
		self.name = name
		self.items = items or []

	def add_item_to_shopping_list(self,item):
		"""
		adds an item to a shopping list
		"""
		self.items.append(item)

	def delete_item_from_shopping_list(self, item):
		"""
		deletes an item from shopping list
		"""
		if len(self.items) > 0 and item in self.items:
			self.items.remove(item)
		else:
			raise ValueError

	def view_shopping_list(self):
		"""
		view shopping list
		"""
		return self.items

	


