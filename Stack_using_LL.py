class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stck_LL:
    
    def __init__(self,size):
        self.top = None                             # pointer moves opposite (top to bottom)
        self.size = size
        self.count = 0
    
    def is_empty(self):
        return self.top is None                     # returns True or False

    def push(self,data):
        if self.top == None:                        # if no top, no stck exists, so make a new top
            self.top  = Node(data)
            return
        
        if self.count == self.size:
            print("Stack Overflow!")
            return
        new_node = Node(data)                       # new node with pointer towards top
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        return

    def pop(self):
        if self.is_empty() is True:
            print("Stack is empty!")
            return
        
        itr = self.top.data                         # since pop removes only top element, new top is node under it
        self.top = self.top.next
        print("Popped Node:",itr)
        self.count -= 1
        return

    def print_stck(self):
        if self.is_empty() is True:
            print("Stack is empty!")
            return

        itr = self.top
        print("--------------")
        while itr is not None:
            print(itr.data)
            itr = itr.next
        print("--------------")
        return
    
    def top_(self):
        if self.is_empty() is True:
            print("Stack is empty!")
            return

        print(self.top.data)
        return
    
    def get_length(self):
        print(self.count)
        return

obj = Stck_LL(10)
obj.push(23)
obj.pop()
obj.push(25)
obj.push(27)
obj.push(28)
obj.push(29)
obj.push(30)
obj.push(31)
obj.pop()
obj.push(35)
obj.push(35)
obj.push(38)
obj.push(39)
obj.push(42)
obj.push(43)
obj.push(44)
obj.pop()
obj.push(45)
obj.push(46)
obj.print_stck()