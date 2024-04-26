
class Queue:
    def __init__(self):
        self.items=[]

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)


    
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False

    
    def enqueue(self,value):
        self.items.append(value)
        return "Value Inserted"

    
    def dequeue(self):
        if self.isEmpty():
            return "Queue Empty"
        else:
            return self.items.pop(0)
    
    
    def peek(self):
        if self.isEmpty():
            return "Queue Empty"
        else:
            return self.items[0]
    
    
    def delete(self):
        self.items=None

customQueue=Queue()
print(customQueue.isEmpty())
customQueue.enqueue(5)
customQueue.enqueue(8)
customQueue.enqueue(9)
customQueue.enqueue(45)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)