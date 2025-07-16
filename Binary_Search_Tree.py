class TreeNode:
    def __init__(self, data):
        self.data = data            # data stored in the node
        self.left = None            # left child node
        self.right = None           # right child node

class BinarySearchTree:
    def __init__(self):
        self.root = None            # Root node of the binary search tree


    def insert_child(self,data):
        if self.root == None:
            self.root = TreeNode(data)
            return
        current = self.root
        while current:
            if data < current.data:     # then add as left child node
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    return
            elif data > current.data:   # then add as right child node
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    return
            else: return
                # If the value already exists, do not insert duplicates


    def search_loop(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True # you can also return current(node) here
            elif data < current.data:
                current = current.left
            else: current = current.right
        return False


    def search_recursive(self, data):
        def recursion(node):
            if not node:
                return False
            if data ==  node.data:
                return True
            elif data < node.data:
                return recursion(node.left)
            else: 
                return recursion(node.right)
        return recursion(self.root)

   
    def in_order_traversal(self):
        if self.root is None:
            return []
        def helper(node):
            if node is None:
                return []
            # Traverse left subtree, then append current node, then right subtree
            return (helper(node.left) + [node.data] + helper(node.right))
        return helper(self.root)


    def pre_order_traversal(self):
        if self.root is None:
            return []
        def helper(node):
            if node is None:
                return []
            return ([node.data] + helper(node.left) + helper(node.right))
        return helper(self.root)


    def post_order_traversal(self):
        if self.root is None:
            return []
        def helper(node):
            if node is None:
                return []
            return (helper(node.left) + helper(node.right) + [node.data])
        return helper(self.root)


# Example Usage:
obj = BinarySearchTree()
obj.insert_child(10)
obj.insert_child(5)
obj.insert_child(3)
obj.insert_child(4)
obj.insert_child(11)
print(obj.search_loop(2))
print(obj.search_recursive(11))
print("In-Order Traversal: ",obj.in_order_traversal())
print("Pre-Order Traversal: ",obj.pre_order_traversal())
print("Post-Order Traversal: ",obj.post_order_traversal())
