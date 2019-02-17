
class Tree:
    def __init__(head):
        self.head = head

    def insert(val):
        node = head
        while(node != None):
            if(head.val < val):
                node = head.right
            else:
                node = head.left


class Node:
    def __init__(val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
