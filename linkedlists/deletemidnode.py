# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

# Code

def delete_middle(node):
    if node is None or node.next is None:
        return False

    node.val = node.next.val
    node.next = node.next.next
    return True
