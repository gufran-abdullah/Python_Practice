#===============================================================#
#==============Dealing With Strings and Variables===============#
#===============================================================#
message = "Hello! This is first python message variable."
print(message)#Simple valiable stored messages
#===============================================================
message1 = "This is message"#Simple valiable stored messages
print(message1)
message1 = "This is changed message"
print(message1)
#===============================================================
message_new = "Erik"
print("Hello",message_new,",whould you like to learn some Python today?")
#================================================================
person_name = "eric"
print(person_name.upper())# Function for captilize any string
print(person_name.lower())# Function for making small leeters string
print(person_name.title())# Function for captilize first word of any string
#================================================================
golden_message = "Gufran Said: \"Presence is more than just being there\""
print(golden_message)#Escaping string
#================================================================
name = " Gufran "
print(name.lstrip())#functions for avoiding white spaces like " "
print(name.rstrip())
print(name.strip())
#================================================================
name = "Gufran"
age = 19 # integer type variable can be adjust in string using str() function
msg = "Hello My name is "+name+" and i am "+str(age)+" years old"
print(msg)
#===============================================================#
#==============Dealing With Numbers and Variables===============#
#===============================================================#
print(5+3)
print(10-2)
print(2*4)
print(16/2)
print(2**3)# 2 raise to power 3
#================================================================
fav_num = 4
msg1 = "my faviourt number is: "+str(fav_num)
print(msg1)# integer type variable can be adjust in string using str() function
#=================================================================