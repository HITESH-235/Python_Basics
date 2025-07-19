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


    def bfs(self):
        if not self.root:
            return None
        queue = CustomQueue()
        queue.enqueue(self.root)
        result = []

        while not queue.is_empty():
            temp = queue.dequeue()
            result.append(temp.data)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)
        return result

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


class QueueNode:
    def __init__(self,data):
        self.data = data
        self.next = None 

class CustomQueue:
    def __init__(self):
        self.start = None
        self.end = None

    def enqueue(self,value):
        new_node = QueueNode(value)
        if self.is_empty():
            self.start = new_node
            self.end = new_node
            return
        self.end.next = new_node
        self.end = self.end.next
        return

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.start == self.end:
            popped_node = self.start.data
            self.start = None
            self.end = None
            return popped_node
        else:
            popped_node = self.start.data
            self.start = self.start.next
            return popped_node

    def is_empty(self):
        return self.start is None


# Example Usage:
obj = BinarySearchTree()
obj.insert_child(10)
obj.insert_child(5)
obj.insert_child(3)
obj.insert_child(2)
obj.insert_child(4)
obj.insert_child(12)
obj.insert_child(9)
obj.insert_child(14)
print("In-Order :", obj.in_order_traversal(),"\n")
print("In-Order (DFS,Linear):",obj.dfs_inorder_linear(),"\n")
print("In-Order (DFS,Quadratic):", obj.dfs_inorder_quadratic(),"\n")

print("Pre-Order :", obj.pre_order_traversal(),"\n")
print("Pre-Order (DFS):", obj.dfs_preorder(),"\n")

print("Post-Order :", obj.post_order_traversal(),"\n")
print("Post_Order (DFS):", obj.dfs_postorder(),"\n")
print("Using Queue (BFS):", obj.bfs())