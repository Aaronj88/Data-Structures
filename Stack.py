class Stack:
    def __init__ (self,n):
        self.stack = []
        self.n = n #n = max elements allowed in stack

    def push(self,x):
        if len(self.stack) < self.n:
            self.stack.append(x)
        else:
            print("This stack is full.")

    def pop(self):
        if len(self.stack) <= 0:
            print("This stack is empty.")
        else:
            self.stack.pop(-1)


    def top(self):
        if len(self.stack) < 1:
            print("This stack is empty.")
        else:
            print(self.stack[-1])

    def length(self):
        print(len(self.stack))

    def objects(self):
        print(self.stack)



stack1 = Stack(9)
stack1.push(70000)
stack1.push("anything")
stack1.length()
stack1.pop()
stack1.pop()
stack1.pop()
for i in range(1,20):
    stack1.push(i)

stack1.objects()
stack1.top()


