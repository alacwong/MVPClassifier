"""
Node class for binary tree structure
"""


class Node:

    def __init__(self, val, left=None, right=None, weight=0, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.weight = weight
        self.parent = parent
