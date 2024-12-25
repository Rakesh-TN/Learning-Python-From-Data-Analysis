# Variables 
print("- Variables")
name = "Rakesh"
print(name+"is Batman")
print(name,"is Lucky")
print(name,"is in Bangalore")

#Strings 
print("- Strings")
print('Hi, I\'m,'+name+'\nI Living in bangalore')
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.upper().isupper())
print(len(name))
print(name.replace('k','j'))

# Number
print("- Number")
number = 100

print(abs(-55))
print(max(4,8,12,2))
print(min(4,8,12,2))
print(round(3.2))
print(round(3.5))
print(bin(8)) #binary value of number

from math import *

print (sqrt(100))

# List in Python
print("- List in Python")
countries = ['United Status of America', 'Canada', 'Brazil', 'Australia', 'India']
print(countries)
print(countries[2])
print(countries[2][0])
print(countries[2:])
print(countries[1:2])
print(countries[-4])
print(len(countries))

detail = list(('Rakesh', 24, True, 'Bangalore'))
print(detail)


print(type(countries))
print(type(detail))

# List Methods
print("- List Methods")
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, "Rakesh"]
list1.extend(list2)
print(list1)
list2.append(0)
print(list2)
# print(list2.clear())
# print(list2.count(0))
list1.reverse()
print(list1)

# Tuples
print("- Tuples")
three_numbers = (1, 2, 3)
print(three_numbers.index(3)) # We Can't modify, add and remove 
print(three_numbers) 

# IF Statement
print("- IF Statement")

a = 200
b = 100

if a > b:
    print(a,'A is greater than B',b)
elif a == b:
    print(a,'A is equal to B',b)
else:
    print(b ,'B is greater than A', a)
    
# Dictionaries
print("- Dictionaries")

person = {
    "name": "Rakesh",
    "age": 24,
    "nationality": "Indian",
    "city": "Bangalore",
    "Occupation": "Software Developer",
}
print(person)
Name= person["name"]
print(Name)