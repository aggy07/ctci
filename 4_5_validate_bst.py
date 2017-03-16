# 4_5 Validate BST - check if bt is bst
# Hints #35, #57, #86, #113, #128

# binary search tree: all left descendents <= n < all right descendents
# starting at root traverse tree:
# check if left node is <= root
# check if right node is < root
# must visit every node.
# solution from text


class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

last_printed = None
def validate_bst(root):
    global last_printed
    if root == None:    
        print('called on root None')
        return True
    # print('called on {}, lp {}, left {}, right {}'.format(root.value, last_printed, root.left.value if root.left else 'None', root.right.value if root.right else 'None'))
    if not validate_bst(root.left):
        return False
    if last_printed != None and root.value <= last_printed:
        return False
    last_printed = root.value
    # print('root {} lp assigned {}'.format(root.value, last_printed))

    if not validate_bst(root.right):
        return False

    return True




if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(2)
    root.right = Node(7)
    root.right.right = Node(8)
    root.right.left = Node(6)

    print(validate_bst(root))

