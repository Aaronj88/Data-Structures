def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    else:
        return num * factorial(num-1)
    

num = int(input("What would you like to know the factorial of?  "))
if num >= 1000:
    print('Please keep your number to a maximum of 999.')
    quit()
print('The factorial of ',num,"is ", factorial(num))