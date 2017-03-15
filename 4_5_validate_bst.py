# 4_5 Validate BST - check if bt is bst
# Hints #35, #57, #86, #113, #128

# binary search tree: all left descendents <= n < all right descendents
# starting at root traverse tree:
# check if left node is <= root
# check if right node is < root
# must visit every node.


class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def validate_bst(root):
    if root != None:
    
    return True


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(2)
    # root.left.left.left = Node(1)
    root.right = Node(7)
    root.right.right = Node(8)
    root.right.left = Node(70)

    print(validate_bst(root))

