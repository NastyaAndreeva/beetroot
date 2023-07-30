def tree_by_levels(node):
    p, q = [], [node]
    while q:
        v = q.pop(0)
        if v is not None:
            p.append(v.value)
            q += [v.left,v.right]
            print(q)
    return p if not node is None else []

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
print([1, 2] + [3, 4])
