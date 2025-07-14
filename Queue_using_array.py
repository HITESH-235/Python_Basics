class Queue_impl:
    element = None

    def __init__(self,size):
        self.size = size
        self.q = []
        self.cur_size = 0
        self.start = -1
        self.end = -1

    def push(self,x):
        if self.cur_size == self.size:
            print("Queue Full")
            return

        if self.cur_size == 0:
            self.start = 0
            self.end = 0

        self.end = (self.end + 1)%self.size   #0 when full, or updates by +1
        self.q.append(x)

        self.cur_size += 1
        return

    def pop(self):   #first out
        Queue_impl.element = self.q[self.start]

        if self.cur_size == 0:
            print("Empty Queue")
            return

        if self.cur_size == 1:   #initialize everything
            self.start = -1
            self.end = -1

        else:
            self.start = (self.start + 1)%self.size

        self.cur_size -= 1
        print("Element Popped:",Queue_impl.element)
        return

    def top_(self):

        if self.cur_size == 0:
            print("Empty Queue")
            return
        print("Top Element:",self.q[self.start])
        return

    def get_length(self):
        print("Queue Length:",self.cur_size)
        return

obj = Queue_impl(5)
obj.push(2)
obj.push(4)
obj.pop()
obj.push(6)
obj.push(4)
obj.pop()
obj.push(9)
obj.push(3)
obj.pop()
obj.push(2)
obj.push(7)
obj.top_()
obj.get_length()
