from tkinter import *

root = Tk()

#Data Entry Fields
name_lbl = Label(root, text="Name")
pass_lbl = Label(root, text="Password")
name_entry = Entry(root)
pass_entry = Entry(root)
chkbox = Checkbutton(root, text="Keep me logged in")
btn = Button(root, text="Login", fg="black")
name_lbl.grid(row="0", sticky=E)#sticky is use for making text direction(N,E,W,S) These are used as parameter of sticky
pass_lbl.grid(row="1", sticky=E)
name_entry.grid(row="0",column="1")
pass_entry.grid(row="1", column="1")
chkbox.grid(columnspan=2)
btn.grid(row="4", column="0")
root.mainloop()