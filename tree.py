class Tree:
    def __init__(self, Node):
        self.head = Node

    def is_bst(self, node, min_=float('-inf'), max_=float('inf')):
        if node is None:
            return True 
        elif node.val < min_ or node.val > max_:
            return False;
        return self.is_bst(node.left, min_, node.val) and self.is_bst(node.right, node.val, max_)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)
