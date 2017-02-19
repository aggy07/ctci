# 2.5 
# You have two number represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# Example
# Input: (7 -> 1 -> 6 ) + (5 -> 9 -> 2). That is 617 + 295.
# Output: 2 -> 1 -> 9 that is 912.
# Hints 7 30 71 95 109
from LinkedList import LinkedList

def sum_lists(n1,n2):
	''' Descripting of solution:
	iterate through each linked list 
	take the value from each node and multiply it by 10 multiplied by a counter for the current element. 
	Then add this to the running total
	take the running total and modulo by a factor of ten tracked by the counter. Add the modulo result to the linked list.
	return the result '''
	lists = [n1, n2]
	total = 0
	for l in lists:
		place = 0
		for n in l:
			total += n.value * (10**place)
			place += 1
			print(total)
	sum_as_ll = LinkedList()
	place = 1
	while total > 0:
		remainder = total % (10**place)
		sum_as_ll.add(remainder//(10**(place-1)))
		print(total, place, remainder, remainder//(10**(place-1)))
		total -= remainder
		place += 1
	return sum_as_ll

def sum_lists2(ll_a, ll_b):
	n1, n2 = ll_a.head, ll_b.head
	ll = LinkedList()
	carry = 0
	while n1 or n2:
		result = carry
		if n1:
			result += n1.value
			n1 = n1.next
		if n2:
			result += n2.value
			n2 = n2.next
		ll.add(result % 10)
		carry = result // 10
			
	if carry:
		ll.add(carry)
	
	return ll

def sum_lists_followup(ll_a, ll_b):
	# Pad the shorter list with zeros
	if len(ll_a) < len(ll_b):
		for i in range(len(ll_b) - len(ll_a)):
			ll_a.add_to_beginning(0)
	else:
		for i in range(len(ll_a) - len(ll_b)):
			ll_b.add_to_beginning(0)

	# Find sum
	n1, n2 = ll_a.head, ll_b.head
	result = 0
	while n1 and n2:
		result = (result * 10) + n1.value + n2.value
		n1 = n1.next
		n2 = n2.next

	# Create new linked list
	ll = LinkedList()
	ll.add_multiple([int(i) for i in str(result)])

	return ll

if __name__ == '__main__':
	n1 = LinkedList([7,1,6])
	n2 = LinkedList([5,9,2])
	print('({}) + ({})'.format(n1,n2))
	print(sum_lists(n1,n2))
	print(sum_lists2(n1,n2))
	print(sum_lists_followup(n1,n2))

# LEARNING Try recursion. Suppose you have two lists, A = 1->5->9 (representing 951) and B 	2-> 3->6-> 7 (representing 7632), and a function that operates on the remainder of the 	lists (5->9 and 3->6->7). Could you use this to create the sum method? What is the 	relationship between sum(l->5->9, 2->3->6->7) and sum(5->9, 3->6->7)?
