class Queue:
    def __init__(self,maxSize) -> None:
        self.maxSize=maxSize
        self.items = maxSize*[None]
        self.start= -1
        self.top= -1

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)

    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start==0 and self.top + 1==self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "Queue Full"
        else:
            if self.top +1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start == -1:
                    self.start = 0

            self.items[self.top]=value

    
    def dequeue(self):
        if self.isEmpty():
            return "Queue Empty"

        else:
            first=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            
            elif self.start +1 ==self.maxSize:
                self.start=0
            
            else:
                self.start+=1

            self.items[start]=None

            return first


        
    def peek(self):
        if self.isEmpty():
            return "Queue Empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items=self.maxSize*[]
        self.start=-1
        self.top=-1

customQueue=Queue(4)
print(customQueue.isEmpty())
customQueue.enqueue(5)
customQueue.enqueue(8)
customQueue.enqueue(9)
customQueue.enqueue(45)
print(customQueue.dequeue())
print(customQueue)