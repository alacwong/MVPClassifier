# Node class for binary tree

class Node:
    """
    Represent tournament as Binary tree
           8
         2   8
      2  3   5  8
    1 2 3 4 5 6 7 8

        5
       2 5
      2 4 5
    1 2 3 4 5

    val: index reference of node -> refers to player stat and player name
    left: left child of node
    right: right child of node
    weight: prediction value between left and right (how hard left beats right/vice versa
    base: pointer to node index in base of the tree
    """

    def __init__(self, val, left=None, right=None, weight=0, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.weight = weight
        self.parent = parent

        if left:
            left.parent = self

        if right:
            right.parent = self

        # base node in tournament
        if left and self.val == left.val:
            self.base = left.base
        elif right and self.val == right.val:
            self.base = right.base
        else:
            self.base = self

    def display_tree(self):
        """
        Display tree
        :return:
        """
        pass

    def get_height(self):
        """
        Get height of tree in O(logN)
        :return:
        """

        if not self.left:
            return 1
        else:
            return 1 + self.left.get_height()

    def copy(self):
        """
        Get copy of tournament
        :return:
        """
