#=========================================================
#===================Dealing with input====================
#=========================================================
car = input("What kind of rental car they would like? ")
print("Let me see if I can find you a",car.title())
print("=========================================================")

dinner = int(input("How many people are in their dinner group? "))
#int(dinner) could be used insted of int(input()))
if dinner > 8:
	print("You have to wait for a table.")
else:
	print("Your table is ready.")
print("=========================================================")

num = input("Enter a number: ")
if int(num)%10 == 0:
	print(str(num), "is multiple of 10." )
else: 
	print(str(num), "is not multiple of 10." )			