import math

def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
def exp(a,b):
    return (a**b) 
                 

n1 = float(input("Enter 1st number: "))
op = str(input("Enter operator: "))
n2 = float(input("Enter 2nd number: "))

if op == '+':
    print("The Answer is: ",add(n1,n2))                 
elif op == '-':
    print("The Answer is: ",sub(n1,n2))
elif op == '*':
    print("The Answer is: ",mul(n1,n2))
elif op == '/':
    print("The Answer is: ",div(n1,n2))
elif op == '**':
    print("The Answer is: ",exp(n1,n2))            


