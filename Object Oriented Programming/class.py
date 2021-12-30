#=========================================================
#=============Dealing with Classes and Objects============
#=========================================================
class Restaurant:#Class initializing
	def __init__(self,name,cuisine_type):
		#A constructor function that automatically call whenever an 
		#object creaated. self is a default aurgument that is use to 
		#define variables in the functions or methods
		self.name = name 					
		self.cuisine_type = cuisine_type

	def description(self):
		"""#This is a method in which 
		the self argument represent
		 the variable values"""
		print("Restaurant Name: ",self.name)
		print("Cuisine Type: ",self.cuisine_type)

	def open(self):
		print("Restaurant is Open NoW!")

"""Object creation of the class. This is how an object has created."""
restaurant = Restaurant('Open Restaurant','Pakistani')
print(restaurant.name.title())#Variable or attribute calling through objects
print(restaurant.cuisine_type.title())
restaurant.description()#Function calling through object
restaurant.open()
print("=========================================================")

class user:
	def __init__(self,fname,lname,location,field):
		self.fname = fname
		self.lname = lname
		self.location = location
		self.field = field

	def describe_user(self):
		full_name = self.fname+' '+self.lname
		print("User Name:",full_name)
		print("Location:",self.location)
		print("Field:",self.field)

	def greetings(self):
		print("Welcome!",self.fname+' '+self.lname)

users = user("Gufran","Abdullah","Lahore","Computer Science")
users.describe_user()
users.greetings()
print("=========================================================")

print("=========================================================")
class Restaurant:
	def __init__(self,name,cuisine_type):
		self.name = name 					
		self.cuisine_type = cuisine_type
		self.no_served = 0

	def description(self):
		print("Restaurant Name: ",self.name)
		print("Cuisine Type: ",self.cuisine_type)

	def increment_customers(self,served):
		self.no_served += served

	def served_people(self):
		print("Number of customers served",self.no_served)	

	def open(self):
		print("Restaurant is Open NoW!")

restaurant = Restaurant('Open Restaurant','Pakistani')
print(restaurant.name.title())
print(restaurant.cuisine_type.title())
restaurant.increment_customers(30)
restaurant.served_people()
restaurant.description()
restaurant.open()

class user:
	def __init__(self,fname,lname,location,field):
		self.fname = fname
		self.lname = lname
		self.location = location
		self.field = field
		self.login_attemps = 0

	def describe_user(self):
		full_name = self.fname+' '+self.lname
		print("User Name:",full_name)
		print("Location:",self.location)
		print("Field:",self.field)

	def increment_login(self,login):
		self.login_attemps += login	

	def show_users(self):
		print("Logged in users are = ",self.login_attemps)	
	
	def reset_login(self):
		self.login_attemps = 0

	def greetings(self):
		print("Welcome!",self.fname+' '+self.lname)

users = user("Gufran","Abdullah","Lahore","Computer Science")
users.describe_user()
users.increment_login(50)
users.show_users()
users.reset_login()
users.show_users()
users.greetings()
print("=========================================================")