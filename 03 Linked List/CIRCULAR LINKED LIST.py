class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node.next == self.head:
                break
        
    def printList(self):
        if self.head==None:
            print("singly linked lst does not exist!")
        else:    
            temp = self.head
            while (temp):
                print (temp.value)
                temp = temp.next  
                if temp==self.head:
                    break

    def createCLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "List created"


    def insertion(self,value,pos):
        if self.head is None:
            return "the head is none"
        else:
            newNode=Node(value)
            
            if pos==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            
            elif pos==1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode     
            
            else:
                tempNode=self.head
                index=0
                while(index<pos-1):
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode

                



     

circularSLL = CircularLL()
# circularSLL.createCLL(5)
# circularSLL.insertion(1,1)
# circularSLL.insertion(2,0)
# circularSLL.insertion(3,3)


print(circularSLL.createCLL(5))
circularSLL.insertion(0,0)
circularSLL.insertion(7,1)
circularSLL.insertion(6,2)

print([node.value for node in circularSLL]) 

#print([node.value for node in cll])
