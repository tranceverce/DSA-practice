class BinaryTree:
    def __init__(self,size) -> None:
        self.custom_list = size*[None]
        self.lastusedindex = 0
        self.maxsize = 0

    def insertNode(self,value):
        if self.lastusedindex+1==self.maxsize:
            return " Tree FULL "
        self.custom_list[self.lastusedindex + 1] = value
        self.lastusedindex += 1
        return  " Node Inserted Successfully"
    
    