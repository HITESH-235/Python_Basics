class Stack_impl:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, x):
        if self.top == 10:
            print("Stack Overflow!")
            return

        self.top += 1
        self.stack.append(x)
        return        
        
    def pop(self):
        if self.top == -1:
            print("Empty Stack")
            return
        
        print("Element Popped: ", self.stack[self.top])
        self.stack.pop(self.top)
        self.top -= 1
        return 

    def top_(self):
        if self.top == -1:
            print("Empty Stack")
            return

        print("Top Element: ",self.stack[self.top])
        return

    def get_length(self):
        if self.top == -1:
            print("Empty Stack")
            return

        print("Stack Length:",self.top+1)
        return
    

Obj = Stack_impl()
Obj.push(4)
Obj.push(5)
Obj.push(8)
Obj.pop()
Obj.push(10)
Obj.push(6)
Obj.pop()
Obj.push(13)
Obj.push(12)
Obj.pop()
Obj.push(167)
Obj.push(17)
Obj.get_length()
Obj.top_()
