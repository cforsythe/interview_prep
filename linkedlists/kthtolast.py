def kth_to_last(Node, k):
    if Node is None:
        return 0
    n = kth_to_last(Node.next, k) 
    if n == k:
        print(Node.val)
    return 1 + n 

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
    kth_to_last(n, 4) 

main()
