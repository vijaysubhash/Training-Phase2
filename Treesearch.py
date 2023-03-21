class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BStree:
    # def __init__(self):
    #     self.root=None
    #     self.data=None 

    def add_element(self, root, value):
        new_node = Node(value)
        if new_node.data < root.data:
            if root.left != None:
                self.add_element(root.left, value)
                return
            else:
                root.left = new_node
                return
        else:
            if root.right != None:
                self.add_element(root.right, value)
                return
            else:
                root.right = new_node

    def search_ele(self, root, value):
        if root.data == value:
            return root
        if value < root.data and root.left != None:
            return self.search_ele(root.left, value)
        if value > root.data and root.right != None:
            return self.search_ele(root.right, value)

    def sum(self, root):
        sum = root.data
        if root.left != None:
            sum += self.sum(root.left)
        if root.right != None:
            sum += self.sum(root.right)
        return sum

    def height(self, root):
        if root == None:
            return -1

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)


obj = BStree()
root = Node(10)
obj.add_element(root, 7)
obj.add_element(root, 40)
obj.add_element(root, 6)
obj.add_element(root, 9)
obj.add_element(root, 15)
obj.add_element(root, 69)
obj.add_element(root, 13)
# print(obj.search_ele(root,5))  location
# if obj.search_ele(root,69):
#     print("found")
# else:
#     print("element not found")  search of element

# print(obj.sum(root.left)) #sum
# print(obj.sum(root.right))

print(obj.height(root))
print(obj.height(root.left))
print(obj.height(root.right))
