class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Q_LL:
    def __init__(self,size):
        self.start = None
        self.end = None
        self.size = size
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self,data):
        new_node = Node(data)
        if self.end is None:
            self.start = new_node
            self.end = new_node
            self.count += 1
            return

        if self.count == self.size:
            print("Queue Overflow!")
            return

        self.end.next = new_node
        self.end = new_node
        self.count += 1
        return

    def pop(self): 
        if self.is_empty() is True:
            print("Queue is empty")
            return
        
        itr = self.start.data
        self.start = self.start.next
        print(itr,"Popped!")
        self.count -= 1
        return
    
    def top_(self):
        if self.is_empty() is True:
            print("Queue is empty")
            return
        
        print(self.start.data)
        return

    def print_q(self):
        if self.is_empty() is True:
            print("Queue is empty")
            return
        
        itr = self.start
        while itr is not None:
            print(itr.data, end="-")
            itr = itr.next
        return

obj = Q_LL(5)
obj.push(2)
obj.push(2)
obj.pop()
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
obj.push(5)
obj.push(6)
obj.print_q()