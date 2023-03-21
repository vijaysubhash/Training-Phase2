from stack import Stack

obj = Stack()
stack1 = []
st_input = input()
for i in st_input:
    obj.stack_push(i)
obj.printStack()
# if obj.arr[0] == ')':
#     print("Not Balanced Parenthesis")
# elif obj.arr[-1] == '(':
#     print("Not Balanced Parenthesis")
for i in st_input:
    if i == '(':
        stack1.append(i)
    elif i == ')' and len(stack1) != 0:
        stack1.pop()
    else:
        print("Invalid String")
if len(stack1) == 0:
    print("Valid String")
else:
    print("invalid string")
