class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def get_level(self):
        level = 0
        itr = self
        while itr.parent != None:
            level += 1
            itr = itr.parent
        return level

    def print_tree(self):
        indentation = " " * (self.get_level()) * 4
        itr = self
        if itr.parent != None:
            indentation +=  ">"

        print(indentation+self.data)

        if itr.children != []:
            for x in itr.children:
                x.print_tree()
        return

class Tree:
    def __init__(self):
        self.root = None

    def node_find(self,data):

        def helper(node):
            if data == node.data:
                return node

            if node.children != []:
                for x in node.children:
                    recurs_var = helper(x)
                    if recurs_var != None:
                        return recurs_var
            return None

        return helper(self.root)
    
    def add_child(self, data, parent=None):
        new_node = Node(data)

        if self.root != None and parent is None:
            print("Root already exists!")
            return

        if self.root is None:
            self.root = Node(data)
            return

        if parent == None:
            print("Provide parent data as parameter first!")
            return
        
        parent_node = self.node_find(parent)
        if parent_node is None:
            return "Parent doesn't exists!"
        parent_node.children.append(new_node)
        new_node.parent = parent_node

    def get_level(self,data):
        node = self.node_find(data)
        return node.get_level()

    def print_tree(self):
        self.root.print_tree()

root = Tree()
root.add_child("Electronics") # root
root.add_child("Electrons") # Root already exists
root.add_child("Laptop","Electronics") # (child,parent)
root.add_child("Lenovo","Laptop")
root.add_child('Ideapad','Lenovo')
root.add_child('Slim','Lenovo')
root.add_child('Asus','Laptop')
root.add_child('Phone','Electronics')
root.add_child('Samsung','Phone')
root.add_child('Iphone','Phone')
print(root.get_level("Electronics"))
root.print_tree()