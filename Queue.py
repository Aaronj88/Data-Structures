class Queue:
    def __init__(self,size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.available = size
        self.queue = [None] * size

    def enqueue(self,item):
        if self.available == 0:
            print("There's no space left in this queue!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -= 1

    def dequeue(self):
        if self.available == self.size:
            print("Your queue has nothing to remove!")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1

    def print_rear(self):
        print("The last item in your queue is",self.queue[self.rear])

    def print_front(self):
        print("The foremost item in your queue is",self.queue[self.front])
        
    def print_queue(self):
        print("Your queue consists of",self.queue)

queue1 = Queue(10)

queue1.enqueue("something")
queue1.enqueue("anything")
queue1.print_queue()
queue1.dequeue()
queue1.print_front()
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.enqueue(65)
queue1.print_rear()



#research trees (gfg)