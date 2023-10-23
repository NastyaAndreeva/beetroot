class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def insert_subtree(root, subtree):
        root.add_child(subtree)

    def remove_subtree(root, subtree):
        if subtree in root.children:
            root.remove_child(subtree)
        else:
            for child in root.children:
                remove_subtree(child, subtree)

