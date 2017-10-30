from flask import Flask, render_template, flash, request, redirect,url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from classes.user import User
from classes.shopping_list import ShoppingList
from classes.shopping_item import ShoppingItem
from functools import wraps


app =  Flask(__name__)

@app.route('/')
def index():
	"""
	This is the homepage of the app
	"""
	return render_template('index.html')

@app.route('/about')
def about():
	"""
	Describes what the app is all about
	"""
	return render_template('about.html')

class RegisterForm(Form):
	"""
	A form to enable users registration
	"""
	name = StringField('Name', [validators.Length(min=2, max=30)])
	username = StringField('Username', [validators.Length(min=2, max=30)])
	email = StringField('Email', [validators.Length(min=5, max=20)])
	password = PasswordField('Password', [validators.DataRequired(), 
		validators.EqualTo('confirm', message='Passwords do not match')])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def create_account():
	"""
	function to enable users to register
	"""
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data 
		username = form.username.data
		email = form.email.data
		password = form.password.data
		
		flash('You are registered and can login', 'success')

		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
	"""
	function to enable users to login
	"""
	if request.method == 'POST':
		#get form fields
		username = request.form['username']
		password = request.form['password']
		#passed
		session['logged_in'] = True
		session['username'] = username

		flash('You are now logged in', 'success')
		return redirect(url_for('dashboard'))
		error = 'Invalid login'
		return render_template('login.html', error=error)

	return render_template('login.html')

def is_logged_in(f):
	"""check if a user is logged in"""
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please login', 'danger')
			return redirect(url_for('login'))
	return wrap


@app.route('/dashboard')
@is_logged_in 
def dashboard():
	user = User('username', 'email', 'password')
	shopping_lists = user.view_shopping_list()
	

	return render_template('dashboard.html', shopping_lists=shopping_lists)

class ShoppingListForm(Form):
	listname = StringField('Listname', [validators.Length(min=1, max=50)])

@app.route('/add_shoppinglist', methods=['GET', 'POST'])
@is_logged_in
def user_create_shopping_list():
	"""
	function to create shopping list
	"""
	form = ShoppingListForm(request.form)
	user = User('username', 'email', 'password')
	if request.method == 'POST' and form.validate():
		name = form.listname.data 
		shopping_list = ShoppingList(name)
		user.create_shopping_list(shopping_list)

		flash('ShoppingList Created', 'success')
		return redirect(url_for('add_items_to_shoppinglist'))

	return render_template('add_shoppinglist.html', form=form)

@app.route('/delete_shopping_list', methods=['POST'])
@is_logged_in
def delete_shopping_list():
	"""
	function to delete shopping_list
	"""
	form=ShoppingListForm(request.form)
	name = request.form['name']
	shopping_list = ShoppingList(name)
	shopping_list.delete_shopping_list(name)
	flash('Shopping list deleted', 'success')
	return redirect(url_for('dashboard'))



class AddItemsForm(Form):
	items = StringField('Items', [validators.Length(min=1, max=50)])
	quantity = StringField('Quantity', [validators.Length(min=1, max=50)]) 

@app.route('/add_items', methods=['GET', 'POST'])
@is_logged_in
def add_items_to_shoppinglist():
	"""
	function to add items to the shopping list
	"""
	form = AddItemsForm(request.form)
	if request.method == 'POST' and form.validate():
		items = form.items.data
		quantity = form.quantity.data
		shopping_list = ShoppingList(items)
		shopping_list.add_item_to_shopping_list(items)

		flash('Item added', 'success')

		return redirect(url_for('dashboard'))

	return render_template('add_items.html', form=form)


@app.route('/logout')
def logout():
	session.clear()
	flash('You are logged out', 'success')
	return redirect(url_for('login'))


if __name__ == '__main__':
	app.secret_key='abcd1234'
	app.run(debug=True)