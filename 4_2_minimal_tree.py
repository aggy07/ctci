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

'''


