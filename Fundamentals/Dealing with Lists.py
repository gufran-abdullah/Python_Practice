#=========================================================
#===================Dealing with Lists====================
#=========================================================
name = ['Ali','Hassan',"Kashif"]#A list like array in C++ 
print(name)
print("=========================================================")
msg = "Hello "
print(msg,name[0])#print list items by their index number
print(msg,name[1])#index of the list starts from 0(zero)
print(msg,name[2])
print("=========================================================")
vehicles = ['Honda Motorcycle','Honda Car','Toyota']
msg1 = "I would like to own a "
print(msg1,vehicles[1])
print("=========================================================")
#=========Changing, adding, and removing elements=========
#=========================================================
dinner = ['Ali','Hassan',"Kashif"]
msg2 = "Hello "
print(msg2,dinner[0]," you are invited today's dinner.")
print(msg2,dinner[1]," you are invited today's dinner.")
print(msg2,dinner[2]," you are invited today's dinner.")
print("=========================================================")
print("Mr. Kashif can not attend the dinner today.")
dinner[2] = "Farhan"
print(msg2,dinner[0]," you are invited today's dinner.")
print(msg2,dinner[1]," you are invited today's dinner.")
print(msg2,dinner[2]," you are invited today's dinner.")
print(dinner)
print("=========================================================")
print("I have found a bigger dinner table today.")
dinner.insert(0,"Gohar")
dinner.insert(3, "Khan")
dinner.append("Bilal")
print(dinner)
print("=========================================================")
print("I will invite only two members for now.")
first = dinner.pop()
print("Sorry ",first," I can not invite you today.")
second = dinner.pop()
print("Sorry ",second," I can not invite you today.")
third = dinner.pop()
print("Sorry ",third," I can not invite you today.")
fourth = dinner.pop()
print("Sorry ",fourth," I can not invite you today.")
print(dinner)
print("Hello ",dinner[0]," your are still invited today's dinner.")
print("Hello ",dinner[1]," your are still invited today's dinner.")
del dinner[0]
print(dinner)
del dinner[0]
print("The list is empty now.")
print(dinner)
print("=========================================================")
#====================Organizig a List=====================
#=========================================================
places = ['Gilgit','Skardu','Swat','Balochistan']
print(places)
print("List in Sorted Form:")
print(sorted(places))
print("List in Original Form:")
print(places)
print("List is in reverse order:")
places.reverse()
print(places)
print("List is in original oreder:")
places.reverse()
print(places)
print("List is in permanent sorted form:")
places.sort()
print(places)
print("List is in changed oredered:")
places.sort()
print(places)
print("=========================================================")
print("No people on the dinner table:")
print(len(dinner))
print("=========================================================")
#======Avoiding Index errors when working with lists======
#=========================================================