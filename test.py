# ask input from user and print the name and the age of the user
name=input("enter your name:")
age=input("enter your age:")
print("hello"+ " " + name + "!")
# ask two number from users and add them togather
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("the sum of the two number is equal to:"+ str(num1+num2))
# list
name=["bati","bekele","demo","deme","dmekek","debora"]
print(name)
print(name[2])
print(name[0:3])
''' user input'''
n1=float(input("enter the first number:"))
op=input("enter the operator:")
n2=float(input("enter the second number:"))
if op=="+":
    print(n1+n2)
elif(op=="-"):
    print(n1-n2)
elif(op=="*"):
    print(n1*n2)
elif(op=="/"):
    print(n1/n2)
else:
    print("invalid operator")
