def multiplication(num1,num2):
    if num1 == 0 or num2 == 0:
        return 0
    
    else:
        return num1 + multiplication(num1, num2 -1)
    

num1 = int(input("What is your first number?  "))
if num1 > 998:
    print("Your number has exceeded this programs limitations. Please try again with a smaller number.")
    exit()
num2 = int(input("What is your second number?  "))
if num2 > 998:
    print("Your number has exceeded this programs limitations. Please try again with a smaller number.")
    exit()
print('Your answer is',multiplication(num1,num2))