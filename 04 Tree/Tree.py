class TreeNode:
    def __init__(self,data,children) -> None:
        self.data=data
        self.children = children

    def __str__(self,level=0):
        ret = "-" * level + str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level + 1)

        return ret
    


    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree=TreeNode('Drinks',[])
cold=TreeNode('Cold',[])
Hot=TreeNode('Hot',[])
Coffee=TreeNode("Coffee",[])
tree.addChild(cold)
tree.addChild(Hot)
Hot.addChild(Coffee)
print(tree)