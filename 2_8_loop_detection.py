# With a curcular linked list return the node that starts loop
# Hints: #50, #69, #83, #90
from LinkedList import LinkedList
def isloop(ll):
    # check if the next node is in a list of nodes
    current = ll.head
    nodes = []
    while current:
        nodes.append(current)
        if current.next in nodes:
            return current.next
        current = current.next

    return False

def isloop2(ll): 
    # take advantage of the LinkedList class and the way our code generates the test ll
    if ll.tail.next:
        return ll.tail.next

    return False

def isloop3(ll):
    # use a runner
    
    runner = ll.head.next
    runner_count = 0
    while runner:
        runner_count += 1
        current_count = 0
        current = ll.head
        while current_count < runner_count:
            if current == runner:
                return current
            current_count += 1
            current = current.next
        runner = runner.next

    return False

def isloop4(ll):
    # use a fast runner, less loop iterations
    slow = fast = ll.head

    while fast and fast.next and fast is not slow:
        slow = slow.next
        fast = fast.next.next

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast

if __name__ == '__main__':
    ll = LinkedList([1,2,3,4,5,6,7])
    print(ll)
    for n in ll:
        if n.value == 7:
            loop = n
        if n.value == 4:
            entry = n
    loop.next = entry
    # 1 2 3 4 5 6 7 4 5 6 7 4 5 6 7 4
    #       c     
    #               r 
    # track the distance.  
    # If c == r before distance then there is a loop
    print('#1', isloop(ll))
    print('#2', isloop2(ll))
    print('#3', isloop3(ll))
    print('#4', isloop4(ll))

#OPPORTUNITIES loop mechanics and incrementing details, using runners before trying lists, using a fast runner, describing/exploring the relationship in mathematical terms