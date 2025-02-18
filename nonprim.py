# dictionary: values are not unique; keys are unique
# dictionary:key-value pair example of dictionary in python is as follows 
nameAndDept={"bati":"cse","bekam":"cse","bereket":"cse","abel":"sw","besu":"sw","milki":"ece","belete":"epce"}
print(nameAndDept);
print(nameAndDept["bati"])
print(nameAndDept["abel"])
print(nameAndDept["milki"])
print(nameAndDept.get("bati"))
print(nameAndDept.get("fdghg","not a valid key"))
# while loop in python 
i=0
while i<=10:
    print(i)
    i+=1
print("done with the loop")

# for loop in python
for i in range(0,20):
    print(i)
    i+=4
print("done successfuly!!")

#exponent function in python
print(2**3)
# function raise to the power: base to power
def raiseTopower(base,power):# base=2, power=4
    result=1#any number raised to the power of zero is equal to one
    for i in range(power):# 0,1,2,3 not including 4
        result=result*base# 1*2=2, 2*2=4, 4*2=8, 8*2=16 therefore 16 is the result of the unction 
    return result
print(raiseTopower(2,4))
print("done with the power function")

# 2d list in python
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])
#print(number_grid[2][2])
print("all the elements in the number_grid are as follows:")
for row in number_grid:
    for col in row:
        print(col)
print("done with the 2d function")

# build a translator in python
def translate(phrase):# hello
    translation=" " # empty string to store the translation
    for letter in phrase: # h
        if letter in"AEIOUaeiou": # h
            translation=translation+"g" # gello # it append the letter
        else:
            translation=translation+letter # h
    return translation

try:
    print(translate(input("enter a phrase:")))
except:
    print("invalid input")

# comments in python
# this is a comment
''' this is a comment'''
# this program is cool
print("comments are fun")
# try except in python
number=int(input("enter a number:"))
print(number)

try:
    number=int(input("enter a number:"))
    print(number)
except:
    print("invalid number")
# reading files in python
# open a file
# read a file
# close a file

    
    
    
    