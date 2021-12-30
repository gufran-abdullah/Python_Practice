#=========================================================
#=============Dealing with Dictionaries===================
#=========================================================
info = {
	'first_name' : 'Gufran',
	'last_name' : 'Abdullah',
	'age' : 19,
	'city' : 'Lahore',
}

print("First Name: "+info['first_name'],"\nLast Name "+info['last_name'],"\nAge "+str(info['age']),"\nCity "+info['city'])

print("=========================================================")

#=========================================================
#=============Loop Through Dictionaries===================
#=========================================================
rivers = {
	'nile' : 'Egypt',
	'Ravi' : 'Pakistan',
	'Satlug' : 'India',
}
for river,country in rivers.items():
	print("The ",river,"runs through ",country)

for river in rivers.keys():
	print("The ",river)

for country in rivers.values():
	print("The ",country)

print("=========================================================")

#=========================================================
#===================Nested Dictionaries===================
#=========================================================
user1 = {
	'fname': 'gufran',
	'lname': 'abdullah',
	'location': 'lahore',
}

user2 = {
	'fname': 'ali',
	'lname': 'hassan',
	'location': 'karachi'
}

people = [user1,user2]

for peop in people:
	print(peop)
print("=========================================================")

fav_places = {
	'jhon': ['Canada','UK'],
	'kely': ['USA','Paris'],
}	
for name,places in fav_places.items():
	print("Name: ",name.title(),"\nFavriot Places:")
	for place in places:
		print(place.title())
print("=========================================================")

cities = {
	'lahore':{
		'country': 'pakistan',
		'population': '3cr',
		'fact': 'city of gardens',
	},
	'london':{
		'country': 'england',
		'population': '2.5cr',
		'fact': 'city of lights',
	},
	'new york':{
		'country': 'america',
		'population': '4cr',
		'fact': 'city of business',
	},
}

for city,info in cities.items():
	print(city.title(),"\nAbout City: ")
	for data,data_about in info.items():
		print(data.title(),": ",data_about.title())
print("=========================================================")		