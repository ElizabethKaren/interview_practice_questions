def nodeDepths(root):
    sum = 0
    stack = [{node: 'root', depth: 0}]
    for child in root:
        sum += 1 
        nodeDepths(child)

    return sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
