
# Find kth to last element of LL
# Hints:#8, #25, #41, #67, #126

from LinkedList import LinkedList

# trivial solution when length known
def kth_to_last(ll, k):
    length = len(ll)
    
    if k > length or k == 0:
        return 'incorrect k'
    
    current = ll.head
    
    if k == 1 and length == 1:
        return current
    
    i = 0

    while current.next:
        # print('i: {} | current idx: {} | current node: {}'.format(i,length-k, current))
        # print('i: {} | current idx: {} | next node: {}'.format(i+1,length-k, current.next))
        if i == length - k:
            return current
        elif i+1 == length - k:
            return current.next
        else:
            i += 1
            current = current.next

# iterative
def kth_to_last2(ll, k):
    p1 = p2 = ll.head
    
    for i in range(k):
        if p1 == None:
            return None
        p1 = p1.next


    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2


#TOD): recursive solutions A and C

if __name__ == '__main__':

    k = 5    
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4, 5])
    print(ll)
    print(kth_to_last2(ll, k))

    print()
    ll = LinkedList()
    ll.add_multiple([1, 2])
    print(ll)
    print(kth_to_last2(ll, k))

    print()
    ll = LinkedList()
    ll.add_multiple([1])
    print(ll)
    print(kth_to_last2(ll, k))

    print()
    ll = LinkedList()
    print('Empty ll:', ll)
    print(kth_to_last2(ll, k))


