num1 = int(input("choose one number "))
num2 = int(input("choose another number "))
var = input ("choose a math symbol ")

if var == '+':
    print(num1 + num2)
    
elif var == '-':
    print(num1 - num2)
    
elif var == '/':
    print(num1 / num2)
    
elif var == '*':
    print(num1 * num2)

else:
    print("I cant do that!")
