from tkinter import *

def dropdown():
	print("This is drop down menu.")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)#cascade for dropdown functionallity
submenu.add_command(label="New Project...", command=dropdown)#command for functions of dropdown
submenu.add_command(label="New", command=dropdown)
submenu.add_separator()#deparator for seperating line among dropdown function
submenu.add_command(label="Exit", command=menu.quit)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo", command=dropdown)

root.mainloop()