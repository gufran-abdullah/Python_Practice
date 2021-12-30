#=========================================================
#=============Dealing with if else elif statements========
#=========================================================
alien_colour = "red"
if alien_colour == "green":
	print("You just earned 5 points.")
print("=========================================================")
if alien_colour == "green":
	print("You just earned 5 points.")
else:
	print("You just earned 10 points.")
print("=========================================================")
if alien_colour == "green":
	print("You just earned 5 points.")
elif alien_colour == "yellow":
	print("You just earned 10 points.")
elif alien_colour == "red":
	print("You just earned 15 points.")
print("=========================================================")
person_age = 19
if person_age < 2:
	print("The person is baby.")
elif person_age==2 or person_age<4:
	print("The person is toddler.")
elif person_age==4 or person_age<13:
	print("The person is a kid.")
elif person_age==13 or person_age<20:
	print("The person is teenager.")
elif person_age==20 or person_age<65:
	print("The person is adult.")
elif person_age==65 or person_age>65:
	print("The person is an elder.")
else:
	print("Error!!!")
print("=========================================================")

favorit_fruit = ['bnanna','apple','grapes']
if "mango" in favorit_fruit:
	print("I really like bnannas.")
elif "apple" in favorit_fruit:
	print("I really like apples.")
elif "coconut" in favorit_fruit:
	print("I really like grapes.")
else:
	print("I do not like this one.")
print("=========================================================")

users = ['admin','user1','user2','user3','user4','user5']
for i in users:
	print("Welcome!!! "+i)

for j in users:
	if "admin" in j:
		print("Hello "+j[0]+" ,would you like to see a status report?")
	else:
		print("Hello "+j+" thank you for logging in again!")

if users:
	print("List has members.")
else:
	print("List is empty.")

users.pop()
print(users)
users.pop()
print(users)
users.pop()
print(users)
users.pop()
print(users)
users.pop()
print(users)
users.pop()
print(users)

if users:
	print("List has members.")
else:
	print("We have to find some users.")
print("=========================================================")

current_users = ['adam','jhon','sushi','rick']
new_users = ['adam','lara','jhon','ben']

for new_user in new_users:
	if new_user in current_users:
		if new_user.upper() or new_user.lower():
			print("You need to enter a new username.")
	else:
		print("The "+new_user+" name is available.")
print("=========================================================")

numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
	print(num)

for num in numbers:
	if num == 1:
		print("1st")
	if num == 2:
		print("2nd")
	if num == 3:
		print("3rd")
	if num == 4:
		print("4th")
	if num == 5:
		print("5th")
	if num == 6:
		print("6th")
	if num == 7:
		print("7th")
	if num == 8:
		print("8th")
	if num == 9:
		print("9th")
print("=========================================================")