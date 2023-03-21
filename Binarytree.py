class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BStree:

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

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        print(root.data, end=" ")
        if root.right is not None:
            self.inorder(root.right)

    def preorder(self, root):
        print(root.data, end=" ")
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)

    def postorder(self, root):
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        print(root.data, end=" ")

    def levelorder(self, root):
        q = []
        while len(q) != 0:
            ele = q.pop(0)
            print(ele.data, end=" ")
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)


obj = BStree()
root = Node(10)
obj.add_element(root, 7)
obj.add_element(root, 40)
obj.add_element(root, 5)
obj.add_element(root, 9)
obj.add_element(root, 15)
obj.add_element(root, 69)
obj.inorder(root)
print("\nInOrder Completed")
obj.preorder(root)
print("\nPreOrder Completed")
obj.postorder(root)
print("\nPostOrder Completed")
obj.levelorder(root)
print("\nLevelOrder Completed")
