# Creation of node and linked link initiation
class Node:
    def __init__(self,data):
        """
        Initialize a new Node object with the given data.
        """
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        """
        Initialize an empty DoubleLinkedList object.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Return an iterator object for the DoubleLinkedList.
        """
        node = self.head 
        while node:
            yield node  
            node= node.next

    def create_DLL(self, nodeval):
        """
        Create a new DoubleLinkedList with the given nodeval as the head and tail.
        """
        node = Node(nodeval)
        node.prev = None
        node.next = None
        self.head=self.tail=node
        return "List is Created"

    def printLL(self):
        """
        Print the contents of the DoubleLinkedList.
        """
        temp= self.head
        while temp is not None:
            print (temp.data,"->",end="")
            temp = temp.next
        print("None")
        print()

#Insertion of nodes in the DLL
    def insertFirst(self, data):
        """
        Insert a new node with the given data at the beginning of the DoubleLinkedList.
        """
        newNode=Node(data)
        newNode.prev = None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        return "Added at beginning"

    def insertLast(self,data):
        """
        Insert a new node with the given data at the end of the DoubleLinkedList.
        """
        newNode = Node(data)
        newNode.next = None
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def insertAny(self, data,location):
        """
        Insert a new node with the given data at the specified location in the DoubleLinkedList.
        """
        newNode = Node(data)
        temp = self.head
        if  location ==1:
            return self.insertFirst(data)
        else:
            temp = self.head
            count = 1
            while temp is not None and count < location - 1:
                temp = temp.next
                count += 1
            if temp is None:
                print("Position out of range")
                return
            newNode.next = temp.next
            if temp.next is not None:
                temp.next.prev = newNode
            temp.next = newNode
            newNode.prev = temp

#Deletion of Nodes from Linked List
    def deleteFirst(self):
        """
        Delete the first node in the DoubleLinkedList.
        """
        self.head = self.head.next
        self.head.prev = None
        return "Delete at beginning"

    def deleteLast(self):
        """
        Delete the last node in the DoubleLinkedList.
        """
        self.tail.prev.next = None

    def deleteAny(self, location):
        """
        Delete the node at the specified location in the DoubleLinkedList.
        """
        temp = self.head
        if  location ==1:
            return self.deleteFirst()
        else:
            count = 1
            while temp is not None and count < location - 1:
                temp = temp.next
                count += 1
            if temp is None:
                print("Position out of range")
                return
            temp.next = temp.next.next
            temp.next.prev=temp

# Reverse traverse in linked list
    def  reverseLinkedList(self):
        """
        Reverse traverse the DoubleLinkedList and print the contents.
        """
        if self.head is None:
            print("No elements")
        else:
            temp=self.tail
            while temp is not None:
                print(temp.data)
                temp = temp.prev
        


        

            
        
a=DoubleLinkedList()
a.create_DLL(5)
a.insertFirst(56)
a.printLL()

a.insertFirst(25)
a.printLL()

a.insertLast(10)
a.printLL()

a.insertLast(178)
a.insertAny(55,2)
a.printLL()
 
a.insertAny(5555,2)

a.deleteAny(4)
a.printLL()

a.reverseLinkedList()