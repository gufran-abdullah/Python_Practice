#=========================================================
#=============Dealing with Lists using Loops==============
#=========================================================
pizzas = ['chicken','tandoori','tikka']
for pizza in pizzas:
	print("I like",pizza.title(),"pizza")
print("I really love pizzas!")
print("=========================================================")

animals = ['horse','dog','cat']
for animal in animals:
	print("A",animal.title(),"would make a great pet!")
print("A Dog would make a great pet!")
print("=========================================================")

for i in range(1,21):
	print(i)
print("=========================================================")

one_million = []
for i in range(1,1000001):
	one_million.append(i)
#print(one_million)
print(max(one_million))
print(min(one_million))
print(sum(one_million))	
print("=========================================================")

for i in range(1,21,2):
	print(i)
print("Odd numbers")
print("=========================================================")

table_of_three = []
for i in range(3,30):
	table_of_three.append(i*3)
print(table_of_three)
print("=========================================================")

cube = []
for i in range(1,11):
	cube.append(i**3)
print(cube)
print("=========================================================")

comp_list = [i**3 for i in range(1,11)]
print(comp_list)
print("=========================================================")
#=========================================================
#=====================Slicing a List======================
#=========================================================
slicing_list = ['cat','dog','horse']
print("First 3 items:")
print(slicing_list[:3])
print("=========================================================")
slicing_list1 = ['cat','dog','horse','lion','monkey','bull','cow']
print("Middle 3 items:")
print(slicing_list1[2:5])
print("=========================================================")
print("Last 3 items:")
print(slicing_list1[4:])
print("=========================================================")
print("Original pizza:")
pizzas = ['chicken','tandoori','tikka']
pizzas.append("vegitable")
print(pizzas)

print("Friend pizza:")
friend_pizza = pizzas[:]
friend_pizza.append("cheese")
print(friend_pizza)

print("My Favorite Pizzas:")
for i in pizzas:
	print(i)

print("My Friend's Favroit Pizzas:")
for i in friend_pizza:
	print(i)
print("=========================================================")
#=========================================================
#=====================Dealing With Tuples=================
#=========================================================
resturant = ('pizza','fries','chicken','nugets','cold drink')
print("List of things that the resturant provide:")
for i in resturant:
	print(i)

resturant = ('biryani','ice cream','chicken','nugets','cold drink')
print("New list of things that the resturant provide:")
for i in resturant:
	print(i)
print("=========================================================")

