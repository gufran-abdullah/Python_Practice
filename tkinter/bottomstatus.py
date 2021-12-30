from tkinter import *

def dropdown():
	print("This is drop down menu.")


root = Tk()

#Top menu Bar
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


#Tool Bar
toolbar = Frame(root, bg="yellow")
insertbtn = Button(toolbar, text="Insert Image", command=dropdown)
insertbtn.pack(side=LEFT, padx=2, pady=2)
delbtn = Button(toolbar, text="Delete", command=dropdown)
delbtn.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)


#Status bar
status = Label(root, text="Noting to show here yet...", bd=1, relief=SUNKEN, anchor=W)
#bd is border, relife is shape of border, anchor is position of text
status.pack(side=BOTTOM, fill=X)


root.mainloop()