class Stack:
    def __init__(self,maxSize) -> None:
        self.maxSize=maxSize
        self.list = []

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)


    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)==self.maxSize:
            return True 
        else:
            return False

    def push(self,value):
        if self.isFull():
            return "The stack is Full"
        else:
            self.list.append(value)
            return "Element Inserted"

    def pop(self):
        if self.isEmpty():
            return "stack is Empty"
        else:
            return self.list.pop()


    def peek(self):
        if self.isEmpty():
            return "stack is Empty"
        else:
            return self.list[-1]

customStack=Stack(7)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(5)
customStack.push(3)
customStack.push(5)
customStack.push(6)
customStack.push(4)
print(customStack.peek())

