from collections import deque

class BSTNode:
    def __init__(self,data):
        self.leftChild = None
        self.rightChild=None
        self.data=data

def print_tree(node, level=0):
    """
    Print the tree starting from the given node in a visually indented format,
    showing the structure of the tree and the node values.
    
    Parameters:
    - node: the current TreeNode to print.
    - level: the current level in the tree, used to determine indentation.
    """
    if node is not None:
        print_tree(node.rightChild, level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.leftChild, level + 1)

def insertNode(root, data):
    if root.data is None:
        root.data = data
    elif data<=root.data:
        if root.leftChild is None:
            root.leftChild=BSTNode(data)
        else:
            insertNode(root.leftChild, data)
    else:
        if root.rightChild is None:
            root.rightChild=BSTNode(data)
        else:
            insertNode(root.rightChild, data)

    return "Node Inserted"


def preOrderTraverse(root):
    """
    Perform a pre-order traversal of the tree and print each node's data.
    
    Pre-order traversal visits nodes in the following order: root, left, right.
    
    Parameters:
    - root: the root TreeNode of the tree.
    """
    if root is None:
        return
    print(root.data)
    preOrderTraverse(root.leftChild)
    preOrderTraverse(root.rightChild)


def inOrderTraverse(root):
    """
    Perform an in-order traversal of the tree and print each node's data.
    
    In-order traversal visits nodes in the following order: left, root, right.
    
    Parameters:
    - root: the root TreeNode of the tree.
    """
    if root is None:
        return
    inOrderTraverse(root.leftChild)
    print(root.data)
    inOrderTraverse(root.rightChild)


def postOrderTraversal(root):
    """
    Perform a post-order traversal of the tree and print each node's data.
    
    Post-order traversal visits nodes in the following order: left, right, root.
    
    Parameters:
    - root: the root TreeNode of the tree.
    """
    if root is None:
        return
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data)

def levelOrderTraversal(root):
    """
    Perform a level-order traversal of the tree and print each node's data.
    
    Level-order traversal visits nodes level by level from top to bottom.
    
    Parameters:
    - root: the root TreeNode of the tree.
    """
    if root is None:
        return
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        print(current_node.data)
        if current_node.leftChild:
            queue.append(current_node.leftChild)
        if current_node.rightChild:
            queue.append(current_node.rightChild)


def searchNode(root,value):
    if root.data == value:
        print("Found")
    elif  root.data > value:
        if root.leftChild.data == value :
            print("Found")
        else:
            searchNode(root.leftChild ,value)
    else:
        if root.rightChild.data == value :
            print("Found")
        else:
            searchNode(root.rightChild ,value)


def minValueNode(root):
    current = root
    while current.leftChild is not None:
        current=current.leftChild
    return current


def deleteNode(root,value):
    if root is None:
        return root
    if value<root.data:
        root.leftChild=deleteNode(root.leftChild,value)
    elif(value>root.data):
        root.rightChild=deleteNode(root.rightChild,value)
    else:
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        
        if root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
        
        temp=minValueNode(root.rightChild)
        root.data =temp.data
        root.rightChild=deleteNode(root.rightChild,temp.data)
    return root


root = BSTNode(None)

nodes = [7,30, 8, 1, 6,34,22,45]
for node in nodes:
    insertNode(root, node)

# print(preOrderTraverse(root))
# print(levelOrderTraversal(root))
print(print_tree(root,22))
deleteNode(root,22)
print(print_tree(root))