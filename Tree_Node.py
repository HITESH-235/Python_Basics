class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
class Tree:
    def __init__(self):
        self.root = None

    def node_find(self,data):

        def helper(node):
            if data == node.data:
                return node

            if node.children:
                for x in node.children:
                    recurs_var = helper(x)
                    if recurs_var:
                        return recurs_var
            return None

        return helper(self.root)
    
    def add_child(self, data, parent=None): # (child,parent)
        new_node = Node(data)

        if self.root and not parent:
            print("Root already exists!")
            return

        if not self.root:
            self.root = Node(data)
            return

        if not parent:
            print("Provide parent data as parameter first!")
            return

        parent_node = self.node_find(parent)
        if not parent_node:
            print(f"Parent:'{parent}' doesn't exists!")
            return

        parent_node.children.append(new_node)
        new_node.parent = parent_node

    def get_level(self,data):
        node = self.node_find(data)
        level = 0

        if node is None:
            return -1

        while node.parent != None:
            node = node.parent
            level += 1
        return level

    def print_tree(self):
        if not self.root:
            print("Empty Tree")
            return

        def helper(node):
            spaces = " " * self.get_level(node.data) * 4 + (">" if node.parent else "")

            print(spaces + node.data)

            if node.children:
                for x in node.children:
                    helper(x)
            return
        helper(self.root)

    def print_tree_stack(self):
        if not self.root:
            print("Empty Tree")
            return

        stack = [[self.root,0]] # [node,level]

        while stack:
            cur_node = stack.pop() # [0: data, 1:level]
            node = cur_node[0]
            level = cur_node[1]
            spaces = " " * level * 4 + ('>' if node.parent else "")

            print(spaces + node.data)

            if node.children:
                for x in node.children[::-1]: # reversed to maintain order
                    stack.append([x,level+1])

    def print_tree_queue(self):
        if not self.root:
            print("Empty Tree")
            return

        queue = Queue()
        queue.enqueue([self.root,0]) # [node,level]
        while not queue.is_empty():
    
            cur_node = queue.dequeue_right()
            node = cur_node[0]
            level = cur_node[1]
            spaces = " " * level * 4 + ('>' if node.parent else "")

            print(spaces + node.data)

            if node.children:
                for x in node.children[::-1]:
                    queue.enqueue([x,level+1])

class Q_Node: # Custom Queue class
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.end = None
        self.start = None

    def enqueue(self,data):
        new_node = Q_Node(data)
        if not self.end:
            self.start = new_node
            self.end = new_node
            return

        self.end.next = new_node
        self.end = new_node
        return

    def dequeue_right(self):
        if not self.start:
            return None

        # when only one element:
        if self.start == self.end:
            popped_node = self.end.value
            self.start = None
            self.end = None
            return popped_node

        itr = self.start
        while itr.next != self.end:
            itr = itr.next

        popped_node = self.end.value
        self.end = itr
        self.end.next = None

        return popped_node

    def is_empty(self):
        return self.start is None

root = Tree()
root.add_child("Electronics") # root

# root.add_child("Electrons") # Root already exists
root.add_child("Laptop","Electronics") # (child,parent)
root.add_child("Lenovo","Laptop")
root.add_child('Ideapad','Lenovo')
root.add_child('Slim','Lenovo')
root.add_child('Asus','Laptop')
# root.add_child('Dummy_child','Dummy_parent') # Wrong parent case
root.add_child('Phone','Electronics')
root.add_child('Samsung','Phone')
root.add_child('Iphone','Phone')

print(root.get_level("Electronics"))

print("\nTree:")
root.print_tree()

print("\nTree by Stack method:")
root.print_tree_stack()

print("\nTree by Queue method:")
root.print_tree_queue()