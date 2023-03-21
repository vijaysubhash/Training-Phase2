class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.previous = None
class LinkedList:

    def add_element(self,head,value):
        new_node=Node(value)  #1
        temp=head
        while temp.next is not None:  #2
            temp=temp.next
        temp.next=new_node  #3
        new_node.previous = temp
        new_node.next = None

    def remove_element(self,head):
        temp=head
        while temp.next.next is not None:
            temp=temp.next
        temp.next.previous = None
        temp.next=None

    def reverse(self,head):
        curr=head
        while curr.next is not None:
            curr = curr.next
        while curr:
            print("<-",curr.data,end="")
            curr = curr.previous
        print()
    
    def print_list(self,head):
        temp=head
        while temp is not None:
            print(temp.data,end="<->")
            temp=temp.next
        print()

    def is_prime_or_not(self, head):
        temp = head
        pos = 0
        while temp is not None:
            pos+=1 
            if temp.data >1:
                for i in range(2,int(temp.data/2)+1):
                    if(temp.data%i) == 0:
                        print(f"{temp.data} is not prime")
                        break
                else:
                    print(f"{temp.data} is a prime at position {pos}")
            else:
                print(f"{temp.data} is not prime")
            temp = temp.next
    
obj=LinkedList()
head=Node(7) 
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,77)
obj.add_element(head,19)
obj.print_list(head)
obj.is_prime_or_not(head)