try :
    x = int(input('Enter a number: '))
    print(x)
except ValueError:
    print('Invalid input')
finally:
    print('Program executed successfully')
    