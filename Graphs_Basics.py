# Array of edges (edge list, undirected)
n = 8 # no. of nodes: 0,1,2,3,4,5,6,7 (given)
edge_arr = [[0,1],[1,2],[0,3],[3,4],[3,7],[3,6],[4,2],[4,5],[5,2]]

# Adj_Matrix = [] # Convert Edge Array --> Adjacency Matrix:
# for i in range(n):
#     Adj_Matrix.append([0]*n)
# for u,v in edge_lst:
#     Adj_Matrix[u][v] = 1
#     Adj_Matrix[v][u] = 1 # comment this for directed

from collections import defaultdict # Convert Edge Array --> Adjacency List:
Adj_lst = defaultdict(list)
for u,v in edge_arr:
    Adj_lst[u].append(v)
    Adj_lst[v].append(u) # comment this for directed


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


def dfs_iterative(node):
    stack = CustomStack()
    stack.push(node)
    result = []
    while not stack.is_empty():
        temp = stack.pop()
        result.append(temp)
        for neigh in Adj_lst[temp]:
            if neigh not in seen:
                stack.push(neigh)
                seen.add(neigh)
    return result


def dfs_recursive(node):
    result = [node]
    for neigh in Adj_lst[node]:
        if neigh not in seen:
            seen.add(neigh)
            result += dfs_recursive(neigh)
    return result


def bfs_iterative(node):
    queue = CustomQueue()
    queue.enqueue(source)
    result = []
    while not queue.is_empty():
        temp = queue.dequeue()
        result.append(temp)
        for neigh in Adj_lst[temp]:
            if neigh not in seen:
                seen.add(neigh)
                queue.enqueue(neigh)
    return result

# Example Usage:
source = 0
seen = {source}
print("\nDFS by Recursion: ",dfs_recursive(source))
seen = {source}
print("\nDFS by Iteration: ",dfs_iterative(source))
seen = {source}
print("\nBFS by Iteration: ",bfs_iterative(source))