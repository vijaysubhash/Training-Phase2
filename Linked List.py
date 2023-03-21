class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def start_add(self, head, value):
        new_node = Node(value)
        new_node.next = head
        head = new_node
        return head

    def add_at_position(self, head, value, pos):
        # index = 2
        current = head
        prev = None
        new_node = Node(value)
        while pos != 0:
            prev = current
            current = current.next
            pos = pos - 1
        prev.next = new_node
        new_node.next = current
        return new_node

    def add_element(self, head, value):
        new_node = Node(value)  # s1
        temp = head
        while temp.next is not None:  # s2
            temp = temp.next
        temp.next = new_node  # s3

    def remove_element(self):
        temp = head
        while temp.next.next is not None:  # s2
            temp = temp.next
        temp.next = None

    def search_element(self, value):
        temp = head
        count = 0
        pos = 0
        while temp.next is not None:
            temp = temp.next
            pos += 1
            if temp.data == value:
                count += 1
                break
            else:
                count
        if count != 0:
            return f"Element Found at {pos}"
        else:
            return "Not Found"

    def reverse(self, head):
        current = head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        return head

    def print_list(self):
        temp = head
        while temp is not None:
            print(temp.data, end="-->")
            temp = temp.next
        print()


obj = LinkedList()
head = Node(10)
obj.add_element(head, 20)
obj.add_element(head, 30)
obj.remove_element()
head = obj.start_add(head, 7)
head = obj.start_add(head, 50)
obj.add_at_position(head, 70, 2)
obj.add_at_position(head, 100, 4)
obj.print_list()
head = obj.reverse(head)
obj.print_list()
val = int(input())
print(obj.search_element(val))
