from tkinter import *
from tkinter import ttk

root = Tk()
root.title('A Simple Calculator')
root.geometry('500x500')

# Add Function
def calc_func():
    n1 = float(n1_entry.get())
    n2 = float(n2_entry.get())
    op = str(op_entry.get())

    if op == '+':
        return (n1+n2)
    elif op == '-':
        return (n1-n2)
    elif op == '*':
        return (n1*n2)        
    elif op == '/':
        return (n1/n2)

## Labels
n1_label = ttk.Label(root,text='Enter 1st Number: ')
n1_label.grid(row=0,column=0,pady=5)
n2_label = ttk.Label(root,text='Enter 2nd number: ')
n2_label.grid(row=1,column=0,pady=5)
op_label = ttk.Label(root,text='Enter operator: ')
op_label.grid(row=2,column=0,pady=5)
ans_label = ttk.Label(root,text='The Answer is: ')
ans_label.grid(row=3,column=0,pady=10)

## Entry
n1_entry = ttk.Entry(root,width=20)
n1_entry.grid(row=0,column=1,pady=5)
n2_entry = ttk.Entry(root,width=20)
n2_entry.grid(row=1,column=1,pady=5)
op_entry = ttk.Entry(root,width=20)
op_entry.grid(row=2,column=1,pady=5)
# ans_entry = ttk.Entry(root,width=20)
# ans_entry.grid(row=3,column=1,pady=5)
ans_btn = ttk.Button(root,text='Calculate',command=calc_func)
ans_btn.grid(row=3,column=1)

root.mainloop()