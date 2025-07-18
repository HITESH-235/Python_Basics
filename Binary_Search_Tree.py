class TreeNode:
    def __init__(self, data):
        self.data = data            # data stored in the node
        self.left = None            # left child node
        self.right = None           # right child node

class BinarySearchTree:
    def __init__(self):
        self.root = None            # Root node of the binary search tree


    def insert_child(self,data):
        if not self.root:
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
        if not self.root:
            return []
        def helper(node):
            if not node:
                return []
            # Traverse left subtree, then append current node, then right subtree
            return (helper(node.left) + [node.data] + helper(node.right))
        return helper(self.root)


    def pre_order_traversal(self):
        if not self.root:
            return []
        def helper(node):
            if not node:
                return []
            return ([node.data] + helper(node.left) + helper(node.right))
        return helper(self.root)


    def post_order_traversal(self):
        if not self.root:
            return []
        def helper(node):
            if not node:
                return []
            return (helper(node.left) + helper(node.right) + [node.data])
        return helper(self.root)


    def dfs_inorder_linear(self): # space intensive
        # Left > node > Right
        if not self.root:
            return []
        stack = CustomStack()
        current = self.root
        result = []
        
        while current or not stack.is_empty():
            if current:
                stack.push(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.data)
                current = current.right
        return result


    def dfs_inorder_quadratic(self): # time intensive
        # Left > node > Right
        if not self.root:
            return None
        stack = CustomStack()
        temp = self.root
        result = []

        while temp or not stack.is_empty():
            while temp:
                stack.push(temp)
                temp = temp.left
            temp = stack.pop()
            result.append(temp.data)
            temp = temp.right
        return result


    def dfs_preorder(self):
        # node > Left > Right
        if not self.root:
            return None
        stack = CustomStack()
        stack.push(self.root)
        result = []

        while not stack.is_empty():
            temp = stack.pop()
            result.append(temp.data)

            if temp.right:
                stack.push(temp.right)
            if temp.left:
                stack.push(temp.left)
        return result


    def dfs_postorder(self):
        # Left > Right > node
        if not self.root:
            return None
        stack = CustomStack()
        stack.push(self.root)
        result = []

        while not stack.is_empty():
            temp = stack.pop()
            result.append(temp.data)

            if temp.left:
                stack.push(temp.left)
            if temp.right:
                stack.push(temp.right)
        return result[::-1]
        

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CustomStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None


# Example Usage:
obj = BinarySearchTree()
obj.insert_child(104857)
obj.insert_child(-948572)
obj.insert_child(583920)
obj.insert_child(34857)
obj.insert_child(-1000000)
obj.insert_child(847293)
obj.insert_child(0)
obj.insert_child(127)
obj.insert_child(94857)
obj.insert_child(-483920)
obj.insert_child(939483)
obj.insert_child(1000000)
obj.insert_child(-123456)
obj.insert_child(384756)
obj.insert_child(294857)
obj.insert_child(192837)
obj.insert_child(-394857)
obj.insert_child(8472)
obj.insert_child(38742)
obj.insert_child(918273)
obj.insert_child(-100)
obj.insert_child(50000)
obj.insert_child(600000)
obj.insert_child(-204857)
obj.insert_child(700000)
obj.insert_child(808080)
obj.insert_child(909090)
obj.insert_child(-111111)
obj.insert_child(222222)
obj.insert_child(-333333)
obj.insert_child(444444)
obj.insert_child(555555)
obj.insert_child(-666666)
obj.insert_child(777777)
obj.insert_child(888888)
obj.insert_child(-999999)
obj.insert_child(123456)
obj.insert_child(234567)
obj.insert_child(345678)
obj.insert_child(456789)
obj.insert_child(-567890)
obj.insert_child(678901)
obj.insert_child(-789012)
obj.insert_child(890123)
obj.insert_child(901234)
obj.insert_child(-1234)
obj.insert_child(4321)
obj.insert_child(876543)
obj.insert_child(135791)
obj.insert_child(246802)
print("In-Order :", obj.in_order_traversal(),"\n")
print("In-Order (DFS,Linear):",obj.dfs_inorder_linear(),"\n")
print("In-Order (DFS,Quadratic):", obj.dfs_inorder_quadratic(),"\n")

print("Pre-Order :", obj.pre_order_traversal(),"\n")
print("Pre-Order (DFS):", obj.dfs_preorder(),"\n")

print("Post-Order :", obj.post_order_traversal(),"\n")
print("Post_Order (DFS):", obj.dfs_postorder())
