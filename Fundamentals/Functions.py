#=========================================================
#=============Dealing with Functions======================
#=========================================================
def display_message():
	print("We are going to learn about functions in this chapter.")

display_message()
print("=========================================================")	

#=========================================================
#=============Dealing with Functions with parameters======
#=========================================================
def favorite_book(title):
	print("One of my favorite book is",title.upper())

favorite_book('History of Time')
print("=========================================================")	

def make_shirts(size,msg):
	print(msg,size)

make_shirts(msg="The beautiful shirt has size of",size=20)	
print("=========================================================")

def make_shirt(msg,size='Large'):
	print(msg,size)

make_shirt(msg="I love Python!")
print("=========================================================")

#=========================================================
#=============Dealing with Functions with return type=====
#=========================================================
def describe_city(city,country='Pakistan'):
	print(city,"is in",country)	

describe_city("Lahore")
describe_city(city="Karachi")
describe_city(city="London",country="UK")	
print("=========================================================")

def city_country(city,country):
	pack = city+' '+country
	return pack
print(city_country("Lahore","Pakistan"))
print("=========================================================")

def make_album(name,album,number_of_tracks=''):
	singer = {'Artist Name':name, 'Artist Album':album}
	if number_of_tracks:
		singer = {'Artist Name':name, 'Artist Album':album, 'Number of Tracks':number_of_tracks}
	return singer
print(make_album("Rahat Fateh Ali Khan","Tumhy Dil Lagi"))
print(make_album("Rahat Fateh Ali Khan","Tumhy Dil Lagi",20))
print("=========================================================")

#=========================================================
#Dealing with Functions with dictionaries and while loop==
#=========================================================
def make_album(name,album,number_of_tracks=''):
	singer = {'Artist Name':name, 'Artist Album':album}
	if number_of_tracks:
		singer = {'Artist Name':name, 'Artist Album':album, 'Number of Tracks':number_of_tracks}
	return singer
while True:		
	name = input("Enter Name: ")
	if name == 'q':
		break
	album = input("Enter album name: ")
	if album == 'q':
		break
	num_of_tracks = input("Enter number of tracks: ")
	if num_of_tracks == 'q':
		break	
	print(make_album(name,album,num_of_tracks))
print("=========================================================")

#=========================================================
#=============Dealing with Functions with lists===========
#=========================================================
def show_megician(names):
	for name in names:
		print(name)	

meg = ['ali','kashif']
show_megician(meg)	
print("=========================================================")


#=========================================================
#Dealing with Functions with Arbitrary Arguments==========
#=========================================================
def pizza(*toppings):
	for topping in toppings:
		print(topping)

pizza("Cheeze","Tikka","Chicken")											
print("=========================================================")

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('Gufran', 'Abdullah',location='Lahore',field='Computer Science')
print(user_profile)