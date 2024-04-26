class Node:
    def __init__(self, data):
        """
        Initializes a new Node object with the given data.

        Parameters:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

def printLL(head):
    """
    Prints the elements of a linked list starting from the specified head node.

    Parameters:
        head: The head node of the linked list to be printed.
    """
    while head is not None:
        print(head.data, " -> ", end="")
        head = head.next
    print("None")
    return

def insertFIRST(head, data):
    """
    Inserts a new node with the given data at the beginning of the linked list.

    Parameters:
        head: The head node of the linked list.
        data: The data to be inserted into the new node.

    Returns:
        The new head node after insertion.
    """
    nwnode = Node(data)
    nwnode.next = head
    head = nwnode
    return head

def insertLAST(head, data):
    """
    Inserts a new node with the given data at the end of the linked list.

    Parameters:
        head: The head node of the linked list.
        data: The data to be inserted into the new node.

    Returns:
        The head node of the linked list after insertion.
    """
    temp = head
    while temp.next is not None:
        temp = temp.next

    nwnode = Node(data)
    temp.next = nwnode
    return head

def insertANY(head, pos, data):
    """
    Inserts a new node with the given data at the specified position in the linked list.

    Parameters:
        head: The head node of the linked list.
        pos: The position at which the new node should be inserted.
        data: The data to be inserted into the new node.

    Returns:
        The head node of the linked list after insertion.
    """
    temp = head
    while pos > 1:
        temp = temp.next
        pos -= 1
    a = temp.next
    nwnode = Node(data)
    nwnode.next = a
    temp.next = nwnode
    return head

def deleteFIRST(head):
    """
    Deletes the first node from the linked list.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The head node of the linked list after deletion.
    """
    temp = head
    head = head.next
    temp = None
    return head

def deleteLAST(head):
    """
    Deletes the last node from the linked list.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The head node of the linked list after deletion.
    """
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

def deleteANY(head, pos):
    """
    Deletes the node at the specified position from the linked list.

    Parameters:
        head: The head node of the linked list.
        pos: The position of the node to be deleted.

    Returns:
        The head node of the linked list after deletion.
    """
    temp = head
    while pos > 1:
        temp = temp.next
        pos -= 1
    a = temp.next.next
    temp.next = a
    return head

def reverseLL(head):
    """
    Reverses the linked list.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The head node of the reversed linked list.
    """
    prev = None
    curr = head
    while curr is not None:
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead
    return prev

def middleLL(head):
    """
    Finds the middle node of the linked list.

    Parameters:
        head: The head node of the linked list.

    Returns:
        The middle node of the linked list.
    """
    slow = head
    fast = head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

# Creating a linked list with initial nodes
newnode = Node(5)
newnode2 = Node(3)
newnode3 = Node(2)
newnode.next = newnode2
newnode2.next = newnode3

# Inserting nodes at various positions
p = insertFIRST(newnode, 7)
printLL(p)
q = insertLAST(p, 9)
printLL(q)
l = insertANY(q, 2, "#")
printLL(l)

# Deleting nodes from various positions
m = deleteFIRST(l)
printLL(m)
n = deleteLAST(q)
printLL(n)
q = deleteANY(p, 2)
printLL(q)

# Reversing the linked list
r = reverseLL(q)
printLL(r)

# Finding the middle node of the linked list
s = middleLL(m)
print(s.data)
