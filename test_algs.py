from tree import Tree
from node import Node

def test_is_bst():
    head = Node(10, Node(6, Node(4, Node(3), Node(5)), Node(7)), Node(15, Node(13, Node(12), Node(14)), Node(16)))
    t = Tree(head)
    #print(t.inorder(head))
    print(t.is_bst(head))

test_is_bst()

