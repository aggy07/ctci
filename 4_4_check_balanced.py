# 4_4_check_balanced
# check if BT is balanced such that two subtrees of any node never differ by more than one
# Hints #21, #33, #49, #105, #124

class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.value = item
# Slow solution:
def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1

def check_balanced(root):
    if root is None:
        return True

    diff = get_height(root.left) - get_height(root.right)
    if abs(diff) > 1:
        return False
    else:
        return check_balanced(root.left) and check_balanced(root.right)

# Faster solution
def check_height(root):
    if root is None:
        return -1
    left_height = check_height(root.left)
    if left_height == 'error':
        return 'error'
    right_height = check_height(root.right)
    if right_height == 'error':
        return 'error'

    if abs(left_height - right_height) > 1:
        return 'error'
    else:
        return max(left_height, right_height) + 1

def is_balanced(root):
    return check_height(root) != 'error'


if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.left = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    print(check_balanced(root))
    print(is_balanced(root))