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



root = BSTNode(None)

nodes = [7,30, 8, 1, 6,34,22,45]
for node in nodes:
    insertNode(root, node)

print(preOrderTraverse(root))
