# Getting User Input 

name =input("Enter Your Name: ")
age = input("Enter Your age: ")

print('Hi,',name,'we get to know that your age is',age)

# Word Replacement Exercise

sentence = input('Enter your sentence: ')
print("Your Sentence is :",sentence)
word1 = input('Enter the word to replace :')
word2 = input('Enter the word to replace it with:')
print(sentence.replace(word1,word2))

# Function
def greetings_function():
    name = input('Enter your name :')
    print("Hello", name)
    
greetings_function()