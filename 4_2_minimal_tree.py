# 4_2_minimal_tree - given a ascending sorted array of unigue ints create a binary seart tree with minimal height
# Hints: #19, #73, #116 

''' 
binary search tree means all left descendants <= n < all right descendents
minimal height means the branches should be as balanced as possible
to make a balanced tree we need to pick a root node that is going to 
have an equal number of children on each branch.
Does this require an AVL tree? Or will picking the correct root from the array
eliminate the need for self balancing?

Doing the problem on paper shows that taking the mid point of the list as root gives same number of nodes on each side of tree
slicing the list at this mid point and taking the mid point of each subsequent slice
recursively will generate a balanced binary search tree.
Doing the problem on paper I'm having trouble generalizing into a formula/function.  
I was having trouble keeping track of my place in the sub array.  The solution used the start and end of each 
slice to track it.

The BST implementation in pythonds is overkill for this problem.  All I needed was a node class.

Solution:
https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter4/42MinimalTree.py

'''
class Node:
    def __init__(self,item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

def initiateArrayToBST(array):
    return arrayToBST(array, 0, len(array)-1)

def arrayToBST(array,start,end):
    if start > end:
        return ''
    mid = ((start + end) // 2) 
    root = Node(array[mid])
    root.left = arrayToBST(array, start, mid -1)
    root.right = arrayToBST(array, mid + 1, end)
    return root


if __name__ == '__main__':
    testArray = [1,2,3,4,5,6,7]
    print(initiateArrayToBST(testArray))