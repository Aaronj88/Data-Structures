def printFun(test):

    if(test < 1):
        return
    else:
        print(test, end = " ")
        printFun(test-1)
        print(test, end = " ")
        return
    
test = 77



printFun(test)




#Recursion = A function that calls itself, a loop that repeats until a condition is met, written with a definition, like the example above. This reduces input size (space complexity), which in turn reduces the runtime (time complexity) of the program and increases performance (effieciency)