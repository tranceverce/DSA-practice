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
        return  "Node Inserted Successfully"
    
    def searchNode(self,nodeValue):
        for i in range (len(self.custom_list)):
            if self.custom_list[i] == nodeValue:
                return "Found"
        return "Not Found"

    def preOrderTraverse(self,index):
        if  index > self.lastusedindex:
            return
        print(self.custom_list[index])
        self.preOrderTraverse(2 * index)
        self.preOrderTraverse(2 * index + 1)

    def inOrderTraverse(self,index):
        if index > self.lastusedindex:
            return
        self.inOrderTraverse(2 * index)
        print(self.custom_list[index] )
        self.inOrderTraverse(2 * index + 1)

    def postOrderTraversal(self,index):
        if index > self.lastusedindex:
            return
        self.inOrderTraverse(2 * index)
        self.inOrderTraverse(2 * index + 1)
        print(self.custom_list[index])

    def levelOrder(self,index):


newBT= BinaryTree(6)
newBT.insertNode("N1")
newBT.insertNode("N2")
newBT.insertNode("N3")
newBT.insertNode("N4")
newBT.insertNode("N5")


print(newBT.searchNode("N5"))
# print(newBT.preOrderTraverse(1))
print(newBT.inOrderTraverse(1))
print(newBT.postOrderTraversal(1))