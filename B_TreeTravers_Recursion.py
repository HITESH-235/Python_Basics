class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:               # binary tree don't repeat any value
            return

        if data < self.data:                # adds data to left subtree (less than root)
            if self.left is None:
                self.left = BinaryTree(data)
            else:
                self.left.add_child(data)

        else:                               # for right (greater than root)
            if self.right == None:
                self.right = BinaryTree(data)
            else:
                self.right.add_child(data)

    def in_order_traversal(self):           # left-> root-> right
        if self.data is None:
            return []

        data_lst = []                       # Empty list to store nodes

        # left subtree:
        if self.left != None:
            data_lst += self.left.in_order_traversal()
  
        # base/middle node currently (if no left child found):
        data_lst.append(self.data)

        # right subtree:
        if self.right != None:
            data_lst += self.right.in_order_traversal()

        return data_lst

    def pre_order_traversal(self):
        if self.data is None:
            return []

        data_lst  = [self.data]

        if self.left != None:
            data_lst += self.left.pre_order_traversal()

        if self.right != None:
            data_lst += self.right.pre_order_traversal()

        return data_lst

    def post_order_traversal(self):
        if self.data is None:
            return []

        data_lst = []

        if self.left != None:
            data_lst += self.left.pre_order_traversal()

        if self.right != None:
            data_lst += self.right.pre_order_traversal()

        data_lst.append(self.data)

        return data_lst
    
tree_root = BinaryTree(23)
tree_root.add_child(21)
tree_root.add_child(45)
tree_root.add_child(256)
tree_root.add_child(2)
tree_root.add_child(26)
tree_root.add_child(29)
tree_root.add_child(19)
tree_root.add_child(13)
tree_root.add_child(10)

print(tree_root.in_order_traversal())
print(tree_root.pre_order_traversal())
print(tree_root.post_order_traversal())
