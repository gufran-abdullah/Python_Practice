from tkinter import *	#TKINTER package import

root = Tk() #Main loop Strat from here

#Label for some text
one = Label(root, text="This is too easy to learn.", bg="red", fg="white")
one.pack()
two = Label(root, text="This is too easy to learn.", bg="green", fg="white")
two.pack(fill=X)
three = Label(root, text="This is too easy to learn.", bg="blue", fg="white")
three.pack(side=LEFT,fill=Y)

root.mainloop() #Main loop ends here