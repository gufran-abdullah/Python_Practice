from tkinter import *

root = Tk()

def printname(event):
	print("My name is M Gufran Abdullah.")

btn = Button(root, text="Print My Name", command=printname)
#command is used for binding the function into window
btn.pack()

root.mainloop()