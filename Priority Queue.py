class Queue:

    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.available = size
        self.queue = [None] * size

    def enqueue(self, item):
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
            self.queue = self.queue[1:]
            self.front = (self.front + 1) % self.size
            self.available += 1

    def print_queue(self):
        if self.available == self.size:
            print('Your queue is over!')
        else:
            print("Your queue consists of", self.queue)


start = "\033[1m"
end = "\033[0;0m"
print('How many people would you like in your ' + start + 'Priority' + end +
      ' queue?')
amount_ppl = int(input())
priority_queue = Queue(amount_ppl)
for i in range(0, amount_ppl):
    print('Enter the name of person number', i + 1)
    person = input(' ')
    priority_queue.enqueue(person)
priority_queue.print_queue()
while amount_ppl != 0:
    person_gone = input(
        'Press enter whenever somebody exits your priority queue:')
    priority_queue.dequeue()
    priority_queue.print_queue()
    amount_ppl -= 1
