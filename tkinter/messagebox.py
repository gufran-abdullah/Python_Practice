from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Hi! This is messagebox of tkinter")

answer = tkinter.messagebox.askquestion("Question 1.", "Do you like tkinter?")
if answer == "yes":
	print("You are Welcome to tkinter.")
else:
	print("Sorry! you can not use tkinter.")

root.mainloop()