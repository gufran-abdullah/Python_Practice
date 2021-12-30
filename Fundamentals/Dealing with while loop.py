#=========================================================
#=================Dealing with While Loop=================
#=========================================================
prompt = "Enter a pizza topping."
prompt += "\nEnter 'quit' to exit."

flag = True
while flag:
	message = input(prompt)
	if message == 'quit':
		flag = False
	else:
		print("You like",message.title(),"pizza")
print("=========================================================")

ticket = "Enter your age for ticket price."
ticket += "\nPress 0 to exit: "

active = True
while active:
	age = int(input(ticket))
	if age == 0:
		print("Thank You!")
		active = False
	else:	
		if age <= 3:
			print("Your ticket is free.")
		elif age > 3 and age < 12:
			print("Your ticket cost is $10.")
		else:
			print("Your ticket price is $15.")	
print("=========================================================")

pizza_orders = ['chicken','tandoori','tikka','chicken']
finishid_pizzas = []
for pizza_order in pizza_orders:
	print("Ordered",pizza_order,"pizza.")

while 'chicken' in pizza_orders:
	pizza_orders.remove('chicken')
print("We are run out of chicken pizza.")
	

while pizza_orders:
	current_making = pizza_orders.pop()

	print("Making of",current_making.title())
	finishid_pizzas.append(current_making)
for finishid_pizza in finishid_pizzas:
	print("Your",finishid_pizza.title(),"is ready!")				
print("=========================================================")	

dream_place = {}
active = True
while active:
	place = input("\nEnter your dream place: ")
	visited = input("Enter any place name which you have visited yet:  ")

	dream_place[place] = visited

	repeat = input("\nGive permission to poll any other person (yes/no)? ")
	if repeat == 'no':
		active = False

for places,visit in dream_place.items():
	print("\nYou have visit",visit.upper(),"and your dream place is",place.upper())		
print("=========================================================")		