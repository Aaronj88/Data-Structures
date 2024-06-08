def fib(num):
    
    if num == 0:
        return 0
    
    if num == 1 or num == 2:
        return 1
    
    if num > 2:
        return fib(num - 1) + fib(num - 2)
    

num = int(input("How many digits of the Fibonacci sequence would you like to see?  "))
print(num,"digit(s) of the fibonacci sequence is:",end = " ")
for i in range(0,num):
    print(fib(i),end = " ")






