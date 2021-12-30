import os #Use for system 
"""
open(): It is main function to handle files.
r: It is use to read data from files.
w: It is use to write data in files.
a: It is use to append(update) data in files.
x: It is use to create files in system.
remove(): It is use to delete files from system.
import os
os.remove(): These two lines can remove the file from the system.
close(): It is use to close the files after performing some operations.

"""
# Create a file in the system.
f = open('file1.txt','x')
f.close()

# Write somthing in the file
f = open('file1.txt','w')# w will overwrite all the data in the file.
f.write("Hello! This is first thing that i write in file.\n")
f.write("I Love Python")
print("Success in writing something n file.")
f.close()


# Update File
f = open('file1.txt','a')# a will update something in the file except overwrite anything.
f.write("\nThis is Updating function in file handeling.")
f.write("\nFile is now update.")
print("Update Successfully.")
f.close()

# Read From File
f = open('file1.txt','r')
call = f.read()
print(call)
f.close()

# Delete file
p = open('file2.txt','x')
p.close()

os.remove('file2.txt')#remove file

if os.path.exists('file2.txt'):#Checking condition if file exists then delete it.
	os.remove('file2.txt')
else:
	print("File does not exists.")# Otherwise print a message that the file does not exists.	