class Queue:
    arr = []
    size = 5

    def enqueue(self, element):
        if len(self.arr) == self.size:
            print("Overflow: Queue full")
        else:
            self.arr.append(element)

    def dequeue(self):
        if len(self.arr) == 0:
            print("Underflow: Queue empty")
        else:
            self.arr.pop(0)

    def queue_peek(self):
        if len(self.arr) == 0:
            print("Underflow: Queue empty")
        else:
            return self.arr[-1]

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

    def printQueue(self):
        print(self.arr)


obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
print(obj.arr)
obj.dequeue()
obj.dequeue()
print(obj.arr)
print(obj.queue_peek())
