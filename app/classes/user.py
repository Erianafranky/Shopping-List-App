class User(object):
	"""
	class modelling a user
	"""
	def __init__(self, username,email,password,shopping_lists=None):
		self.username = username
		self.email = email
		self.password = password
		self.shopping_lists = [] or shopping_lists


	def login(self, username, password):
		"""
		function to handle ability of user to login
		"""
		if username == self.username and password == self.password:
			return True
		else:
			return False

	def create_shopping_list(self, shopping_list):
		"""
		function to create shopping list
		"""
		self.shopping_lists.append(shopping_list)

	def delete_shopping_list(self, shopping_list):
		"""
		function to delete shopping list
		"""
		self.shopping_lists.remove(shopping_list)

	def view_shopping_list(self):
		"""
		function to view shopping list
		"""
		return self.shopping_lists

	

		
