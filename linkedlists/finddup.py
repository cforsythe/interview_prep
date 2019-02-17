def find_dup(Node):
    set_ = set()
    prev_node = None
    find_dup_(Node, set_, prev_node)

def find_dup_(Node, set_, prev_node):
    if Node is None:
        return
    if Node.val in set_:
        prev_node.next = Node.next
    else:
        prev_node = Node
        set_.add(Node.val)
    find_dup_(Node.next, set_, prev_node)

def find_dup_ns(Node):
    if Node is None:
        return
    if 

class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_ 
    def __str__(self):
        str_ = ""
        while self.next is not None:
           str_ += self.val + ", "
           self = self.next
        return str_ + self.val

def main():
    n = Node('a', Node('b', Node('a', Node('z', Node('c', Node('z'))))))
    print(n)
    find_dup(n)
    print(n)
main()
