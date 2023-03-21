class Queue:
    temp = []
    original = []

    def enqueue(self, element):
        self.temp.append(element)  # step 1
        while len(self.original) != 0:  # step 2
            pop_ele = self.original.pop(0)
            self.temp.append(pop_ele)
        while len(self.temp) != 0:  # step 3
            pop_ele = self.temp.pop(0)
            self.original.append(pop_ele)
        # if len(self.arr) >= self.size:
        #     print("Overflow: queue full")
        # else:
        #     return self.arr.append(element)

    def dequeue(self):
        # if len(self.arr) == 0:
        #     print("Underflow: queue empty")
        # else:
        #     return self.arr.pop(0)
        return self.original.pop(0)

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False


obj = Queue()
for i in range(5):
    obj.enqueue(i)
print(obj.original)
# temp1 = Queue()
# orig = Queue()
# for i in range(5):
#     temp1.enqueue(i)
#     print(temp1.temp)
#     for ele in orig.original:
#         temp1.enqueue(orig.dequeue())
#     orig.enqueue(temp1.dequeue())
# print(orig.original)
