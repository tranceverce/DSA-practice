class Node:
    def __init__(self,value=None):
        """
        Initialize a new Node object with the given value.
        """
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty LinkedList object.
        """
        self.head=None

    def __iter__(self):
        """
        Return an iterator object for the LinkedList.
        """
        node = self.head 
        while node:
            yield node  
            node= node.next

    def insert(self,value):
        """
        Insert a new node with the given value at the beginning of the LinkedList.
        """
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode

    def printLL(self):
        """
        Print the contents of the LinkedList.
        """
        temp= self.head
        while temp is not None:
            print (temp.value,"->",end="")
            temp = temp.next
        print("None")
        print()

class Stack:
    def __init__(self):
        """
        Initialize an empty Stack object.
        """
        self.LinkedList=LinkedList()

    def __str__(self):
        """
        Return a string representation of the Stack.
        """
        values=[str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        """
        Return True if the Stack is empty, False otherwise.
        """
        if self.LinkedList.head==None:
            return True
        else:
            return False

    def push(self,value):
        """
        Insert a new node with the given value at the beginning of the LinkedList.
        """
        self.LinkedList.insert(value)

    def pop(self):
        """
        Remove and return the first node in the LinkedList.
        """
        if self.isEmpty():
            return "Stack Empty"
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue

    def peek(self):
        """
        Return the value of the first node in the LinkedList.
        """
        if self.isEmpty():
            return "Stack Empty"
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue

    def delete(self):
        """
        Remove all nodes from the LinkedList.
        """
        self.LinkedList.head=None



customStack=Stack()
print(customStack.isEmpty())
customStack.push(5)
customStack.push(8)
customStack.push(25)
customStack.push(66)
print(customStack.peek())
print()
print(customStack)

#print(customStack)