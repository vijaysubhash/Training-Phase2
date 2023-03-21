from stack import Stack

obj = Stack()
obj2 = Stack()
for i in range(obj.size):
    obj.stack_push(i)
print(obj.arr)
num = int(input())
for j in obj.arr:
    pop_ele = obj.stack_pop()
    if j == pop_ele:
        print("Element Found")
        obj2.stack_push(obj.stack_pop())
    else:
        print("Element not found")
print(obj2.arr)

