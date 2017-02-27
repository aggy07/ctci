#Palindrome: Implement a function to check if a linked list is a palindrome.
#Hints:#5, #13, #29, #61, #101
from LinkedList import LinkedList

def palindrome(ll): # reverse and compare
	gg = LinkedList()
	current = ll.head
	
	while current:
		gg.add_to_beginning(current.value)
		current = current.next
	current = ll.head
	pal = gg.head
	
	while current and pal: 
		if current.value == pal.value:
			current = current.next
			pal = pal.next
		else:
			return False
	
	return True

def palindrome2(ll, length): # iterative  https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

	fast = slow = ll.head
	stack = []

	while fast and fast.next: 	# fast moves 2x slow so when fast is at end slow is at middle
		stack.append(slow.value)
		slow = slow.next
		fast = fast.next.next

	if fast: # odd list length so skip middle node
		slow = slow.next

	while slow:
		top = stack.pop()

		if top != slow.value:
			return False

		slow = slow.next

	return True

def palindrome3(ll):
	length = len(ll)
	head = ll.head
	node, result = isPalindromeRecurse(head, length)
	return result

def isPalindromeRecurse(head, length):
	if head == None or length <= 0: # even
		return head, True
	elif length == 1: # odd
		return head.next, True

	node, result = isPalindromeRecurse(head.next, length - 2)

	if not result or not node:
		return node, result

	result = head.value == node.value

	node = node.next

	return node, result



if __name__ == '__main__':
	print('Reverse List')
	ll = LinkedList([1,2,3,2,1])
	print(palindrome(ll))

	ll = LinkedList([1,2,3,3,2,1])
	print(palindrome(ll))

	ll = LinkedList([1,2,3,4,2,1])
	print(palindrome(ll))

	ll = LinkedList([1])
	print(palindrome(ll))

	ll = LinkedList([1,1])
	print(palindrome(ll))

	ll = LinkedList()
	print(palindrome(ll))

	print('Iterative')
	ll = LinkedList([1,2,3,2,1])
	print(palindrome2(ll, len(ll)))

	ll = LinkedList([1,2,3,3,2,1])
	print(palindrome2(ll, len(ll)))

	ll = LinkedList([1,2,3,4,2,1])
	print(palindrome2(ll, len(ll)))

	ll = LinkedList([1])
	print(palindrome2(ll, len(ll)))

	ll = LinkedList([1,1])
	print(palindrome2(ll, len(ll)))

	ll = LinkedList()
	print(palindrome2(ll, len(ll)))

	print('Recursive')
	ll = LinkedList([1,2,3,2,1])
	print(palindrome3(ll))

	ll = LinkedList([1,2,3,3,2,1])
	print(palindrome3(ll))

	ll = LinkedList([1,2,3,4,2,1])
	print(palindrome3(ll))

	ll = LinkedList([1])
	print(palindrome3(ll))

	ll = LinkedList([1,1])
	print(palindrome3(ll))

	ll = LinkedList()
	print(palindrome3(ll))