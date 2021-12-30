from tkinter import *


class nameprint:

	def __init__(self,master):
		frame = Frame(master)
		frame.pack()

		self.pbtn = Button(frame, text="Print My Name", command=self.printname)
		self.pbtn.pack(side=LEFT)
		self.ebtn = Button(frame, text="Exit", command=frame.quit)
		self.ebtn.pack(side=LEFT)

	def printname(self):
		print("My name is M Gufran Abdullah")

root = Tk()
obj = nameprint(root)
root.mainloop()