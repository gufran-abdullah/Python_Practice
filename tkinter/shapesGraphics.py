from tkinter import *

root = Tk()

canvas= Canvas(root, width=300, height=200)
canvas.pack()

blackline = canvas.create_line(0,0,300,50)
redline = canvas.create_line(0,100,300,50,fill="red")
box= canvas.create_rectangle(25,25,130,70,fill="red")
root.mainloop()