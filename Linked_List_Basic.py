class Node:
    def __init__(self, data=None, ):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_lst(self):
        if self.head is None:
            print("Linked List Empty!")
            return

        itr = self.head
        ll_str = ""

        while itr is not None:
            ll_str += str(itr.data) + "-->"
            itr = itr.next

        print("Linked List: ",ll_str)
        return

    def get_length(self):
        count = 0
        itr = self.head
        while itr is not None:
            count+=1
            itr = itr.next

        return count

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None

        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(data)

    def insert_values_at_end(self,data_lst):
        for data in data_lst:
            self.insert_at_end(data)
        return

    def remove_at(self,index):
        if (index<0) or (index >= self.get_length()):
            print("Index out of range!")
            return

        if index == 0:
            if self.get_length() == 1:
                self.head = None
                return
            else:
                self.head = self.head.next
                return

        count = 0
        itr = self.head
        while itr.next is not None:
            if count == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1
        return

    def insert_at(self,index,data):
        if (index<0) or (index > self.get_length()):
            print("Index out of range!")

        if index == 0:
            self.insert_at_beginning()
            return
        
        if index == self.get_length():
            self.insert_at_end(data)
        count = 0
        itr = self.head
        while itr.next is not None:
            if count == index-1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                return
            itr = itr.next
            count += 1

obj = Linked_list()
obj.insert_at_beginning(36)
obj.insert_at_beginning(38)
obj.insert_at_beginning(39)
obj.insert_at_beginning(34)
obj.insert_at_end(12)
obj.insert_values_at_end([2,3,5,7,6])
obj.print_lst()
obj.remove_at(5)
obj.insert_at(5,21212)
obj.print_lst()