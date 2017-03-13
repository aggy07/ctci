# 4_3 List of Depths: Create LL of all nodes at each depth of BT.
# Hints #107 #123 #135

# traversing the list recursively can we keep track of the depth of each level of recursion?
# then based on the depth add to a linked list corresponding to that depth

# I came up with the pre order traversal solution
# next time implement BFS solution

from LinkedList import LinkedList, LinkedListNode
# from BinaryTree import BinaryTree

class Node:
    def __init__(self,item):
        self.right = None
        self.left = None
        self.val = item

def list_depths(node, depth, a):
    array_of_lists = a
    if node:
        if len(array_of_lists) < depth+1:
            array_of_lists.append(LinkedList())
        array_of_lists[depth].add(node)
        depth += 1
        list_depths(node.left, depth, array_of_lists)
        list_depths(node.right, depth, array_of_lists)
    return array_of_lists

if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.right.right = Node('e')
    root.right.left = Node('f')
    root.left.right = Node('g')   
    root.left.left = Node('h')
    a = list_depths(root, 0 , [])
    for item in a:
        print(item)
        print(len(item))