a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
opr = input("Enter the operator: ") # +, -, *, /
if opr == '+':
    print(a+b)
elif opr == '-':
    print(a-b)
elif opr == '*':
    print(a*b)
elif opr == '/':
    print(a/b)
elif opr == '%':
    print(a % b)
else:
    print("Invalid operator")