#=========================================================
#=============Dealing with Inheritance====================
#=========================================================
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

"""restaurant = Restaurant('Open Restaurant','Pakistani')
print(restaurant.name.title())
print(restaurant.cuisine_type.title())
restaurant.increment_customers(30)
restaurant.served_people()
restaurant.description()
restaurant.open()"""

class icecream(Restaurant):
	def __init__(self,name,cuisine_type,flavours):
		super().__init__(name,cuisine_type)
		self.flavours = flavours

	def get_flavours(self):
		print("Your Flavour is: ",self.flavours)	

ice_cream = icecream("Open mice cafe","Pakistani","Chocolate")
ice_cream.description()
ice_cream.open()
ice_cream.flavours() 