from tkinter import *

root = Tk()

def leftclick(event):
	print("Left")

def middleclick(event):
	print("Middle")

def rightclick(event):
	print("Right")

frame = Frame(root, width=100, height=100)
#bind is also use for binding functions which have parameters
frame.bind("<Button-1>", leftclick)#button-1 for left click
frame.bind("<Button-2>", middleclick)#button-2 for middle click
frame.bind("<Button-3>", rightclick)#button-3 for right click
frame.pack()

root.mainloop()