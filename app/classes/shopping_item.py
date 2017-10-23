class ShoppingItem(object):
	"""
	class modelling the items in the shopping list
	"""
	def __init__(self,name,quantity,bought=False):
		self.name = name
		self.quantity = quantity
		self.bought = bought