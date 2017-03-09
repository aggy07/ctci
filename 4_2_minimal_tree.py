# 4_2_minimal_tree - given a ascending sorted array of unigue ints create a binary seart tree with minimal height
# Hints: #79, #73, #7 76 

''' 
binary search tree means all left descendants <= n < all right descendents
minimal height means the branches should be as balanced as possible
implement a binary search tree class with add method
then try testing starting with small lists of integers.
to make a balanced tree we need to pick a root node that is going to 
have an equal number of children on each branch.
Does this require an AVL tree? Or will picking the correct root from the array
eliminate the need for self balancing?

Doing the problem on paper shows that taking the mid point of the list as root.
slicing the list at this mid point and taking the mid point of each subsequen slice
recursively will generate a balanced binary search tree.
Even and odd list lengths require a decision on which side of the tree should be deeper.

The BST implementation in pythonds is maybe a little overkill for this problem.  After I finish it I need to think about how to trim it down to work just for these problem.
In otherwords in an interview would I assume the BST was implemented and refer to the methods of the assumed implementation or would I implement one with the minimal features needed to finish the problem.
'''


