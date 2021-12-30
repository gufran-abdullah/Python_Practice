from tkinter import *

root = Tk()

#frames Making
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

#buttons in the frames
btn1 = Button(topframe, text="Button 1", fg="red")
btn2 = Button(topframe, text="Button 2", fg="blue")
btn3 = Button(topframe, text="Button 3", fg="green")
btn4 = Button(bottomframe, text="Button 4", fg="black")
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=BOTTOM)

root.mainloop()
