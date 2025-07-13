class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_child(self,data):
        if self.root == None:
            self.root = Node(data)

        else:
            itr = self.root

            while itr != None:
                if data < itr.data:
                    if itr.left != None:
                        itr = itr.left

                    else:
                        itr.left = Node(data)
                        return

                if data > itr.data:
                    if itr.right != None:
                        itr = itr.right

                    else:
                        itr.right = Node(data)
                        return

    @staticmethod
    def in_order_helper(node):
        if node is None:
            return []

        lst = []
        if node.left != None:
            lst.extend(BinaryTree.in_order_helper(node.left))

        if node:
            lst.append(node.data)

        if node.right != None:
            lst.extend(BinaryTree.in_order_helper(node.right))
        return lst

    def in_order_traversal(self):
        if self.root is None:
            return []

        return BinaryTree.in_order_helper(self.root)

obj = BinaryTree()
obj.add_child(10)
obj.add_child(5)
obj.add_child(3)
obj.add_child(4)
obj.add_child(11)
print(obj.root.data, obj.root.left.data, obj.root.left.left.data, obj.root.left.left.right.data, obj.root.right.data)
print(obj.in_order_traversal())

