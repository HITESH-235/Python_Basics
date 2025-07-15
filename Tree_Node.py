class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        
class Tree:
    def __init__(self):
        self.root = None

    def find_node(self, target_value):
        def dfs(node):
            if node.value == target_value:
                return node
            for child in node.children:
                result = dfs(child)
                if result:
                    return result
            return None

        return dfs(self.root)

    def add_node(self, value, parent_value=None):
        new_node = TreeNode(value)

        if self.root and not parent_value:
            print("Root already exists! Provide a parent for the new node")
            return

        if not self.root:
            self.root = new_node
            return

        parent_node = self.find_node(parent_value)
        if not parent_node:
            print(f"Parent node:'{parent_value}' not found.")
            return

        parent_node.children.append(new_node)
        new_node.parent = parent_node

    def get_node_level(self, value):
        node = self.find_node(value)
        if not node:
            return -1

        level = 0
        while node.parent:
            node = node.parent
            level += 1
        return level

    def display_tree_recursive(self):
        if not self.root:
            print("The tree is empty.")
            return

        def traverse(node):
            indent = " " * self.get_node_level(node.value) * 4
            prefix = ">" if node.parent else ""
            print(f"{indent}{prefix}{node.value}")
            for child in node.children:
                traverse(child)

        traverse(self.root)

    def display_tree_stack_array(self):
        if not self.root:
            print("The tree is empty.")
            return

        stack = [[self.root, 0]]

        while stack:
            node, level = stack.pop()
            indent = " " * level * 4
            prefix = ">" if node.parent else ""
            print(f"{indent}{prefix}{node.value}")

            for child in reversed(node.children):
                stack.append([child, level + 1])

    def display_tree_stack_linkedlist(self):
        if not self.root:
            print("The tree is empty.")
            return

        stack = CustomStack()
        stack.push([self.root, 0])

        while not stack.is_empty():
            node, level = stack.pop()
            indent = " " * level * 4
            prefix = ">" if node.parent else ""
            print(f"{indent}{prefix}{node.value}")

            for child in reversed(node.children):
                stack.push([child, level + 1])


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


# Example usage:
tree = Tree()
tree.add_node("Electronics")
tree.add_node("Laptop", "Electronics")
tree.add_node("Lenovo", "Laptop")
tree.add_node("Ideapad", "Lenovo")
tree.add_node("Slim", "Lenovo")
tree.add_node("Asus", "Laptop")
tree.add_node("Phone", "Electronics")
tree.add_node("Samsung", "Phone")
tree.add_node("Iphone", "Phone")

print("Level of 'Electronics'(Root):", tree.get_node_level("Electronics"))

print("\nTree (Recursive Display):")
tree.display_tree_recursive()

print("\nTree (Stack using Array):")
tree.display_tree_stack_array()

print("\nTree (Stack using LinkedList):")
tree.display_tree_stack_linkedlist()