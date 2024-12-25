print("- Function")
#def - define 

def greetings_function(name, age):
    print("Hello", name ,"Your age is", age)
    
# name = input('Enter Your Name :')
# age =  input('Enter Your Age :')  

greetings_function("John", 24)
# greetings_function(name, age)

print("- Function with return value")
# Return Statement

def addNumbers(num1, num2):
    return num1 + num2

num1 = int(input('Enter First Number :'))
num2 = int(input('Enter Second Number :'))

print(addNumbers(num1, num2))