# This program makes a tree in python useful in making root and their children

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None  # will assign parent while making child

    def add_child(self,child): # just takes the name of the child, then make it a node
        child.parent = self # form current self. as parent then child_class as child in next line
        self.children.append(child)

    def add_children(self,child_lst):
        for x in child_lst:
            x.parent = self
            self.children.append(x)

    def get_level(self): # start from level 0 (root)
        level = 0
        count = self.parent # if 1 parent generation exist, level = 0

        while count != None: # if no parent, then self = root, level = 0
            level += 1
            count = count.parent
        return level

    def is_leaf(self): # check if the node has no child or not so
        if self.children == []:
            return True
        else:
            return False

    def print_tree(self):
        spaces = " " * self.get_level() * 3  # 3 is just to visualise indentation more
        if self.parent != None:
            x = ">"
        else:
            x = ""
        prefix = spaces + x
        print(prefix + self.data) # in first loop, root gets printed, then:
        # Recursion:
        if self.children:
            for child in self.children:
                child.print_tree()

root = TreeNode("ELECTRONICS")

laptop = TreeNode("Laptop")
phone = TreeNode("Phone")

asus = TreeNode("Asus")
lenovo = TreeNode("Lenovo")
iphone = TreeNode("Iphone")
samsung = TreeNode("Samsung")
google = TreeNode("Google")
ideapad = TreeNode("ideapad")
slim = TreeNode("slim")
note = TreeNode('Note')
galaxy = TreeNode('Galaxy')

root.add_child(laptop)
root.add_child(phone)
laptop.add_child(asus)
laptop.add_child(lenovo)
phone.add_child(google)
phone.add_child(samsung)
samsung.add_child(galaxy)
samsung.add_child(note)

lenovo.add_children([ideapad,slim])
phone.add_child(iphone)

print(samsung.get_level())

print("__________________")
root.print_tree()
print("__________________")
laptop.print_tree()
print("__________________")
phone.print_tree()
