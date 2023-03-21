class Stack:
    arr = []
    size = 70

    def stack_push(self, element):
        if len(self.arr) == self.size:
            print("Overflow: stack full")
        else:
            self.arr.append(element)

    def stack_pop(self):
        if len(self.arr) == 0:
            print("Underflow: stack empty")
        else:
            self.arr.pop()

    def stack_peek(self):
        if len(self.arr) == 0:
            print("Underflow: stack empty")
        else:
            return self.arr[-1]

    def printStack(self):
        print(self.arr)

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False


#obj = Stack()
# obj.stack_push(10)
# obj.stack_push(20)
# obj.stack_push(30)
# obj.stack_push(40)
# print(obj.arr)
# obj.stack_pop()
# obj.stack_pop()
# print(obj.arr)
# print(obj.stack_peek())
