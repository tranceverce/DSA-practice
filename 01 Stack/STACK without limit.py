class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)

    

    def isEmpty(self): #Time and space Complexity is O(1)
        if self.list==[]: 
            return True
        else:
            return False

    def pushInStack(self,value):
        self.list.append(value)
        return "element Inserted"

    def popFromStack(self): #Time and space Complexity is O(1)
        if self.isEmpty():
            return "No elemts to pop"
        else:
            return self.list.pop()
    
    def peek(self): #Return the top of the stack
        if self.isEmpty():
            return "Empty"
        else:
            return self.list[-1]

    def deleteStack(self):
        self.list=None

stack1=Stack()
print(stack1.isEmpty())
stack1.pushInStack(2)
stack1.pushInStack(1)
stack1.pushInStack(3)
stack1.popFromStack()
print(stack1)