from collections import deque

class TreeNode:
    def __init__(self, data):
        """
        Initialize a new TreeNode object with the given data.
        
        Parameters:
        - data: the data to store in the node.
        """
        self.data = data
        self.leftChild = None
        self.rightChild = None


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


def searchingTree(root, searchValue):
    """
    Search for a value in a tree using a breadth-first search approach.
    
    Parameters:
    - root: the root TreeNode of the tree.
    - searchValue: the value to search for in the tree.

    Returns:
    - A string indicating whether the value was found or if the tree does not exist.
    """
    if not root:
        return "Tree does not exist"
    else:
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            current_node = queue.popleft()  # Dequeue the front node from the queue
            if current_node.data == searchValue:  # Check if the current node's data matches the search value
                return "Success"
            if current_node.leftChild is not None:
                queue.append(current_node.leftChild)  # Enqueue left child if it exists
            if current_node.rightChild is not None:
                queue.append(current_node.rightChild)  # Enqueue right child if it exists
        return "Not found"


def insertNode(root, newNode):
    if not root:
        root=newNode
    else:
        queue=deque([root])
        
        while queue:
            current_node = queue.popleft()
            if current_node.leftChild is None:
                current_node.leftChild = newNode
                return "Inserted on the left"
            else:
                queue.append(current_node.leftChild)
            
            if current_node.rightChild is None:
                current_node.rightChild = newNode
                return "Inserted on the right"
            else:
                queue.append(current_node.rightChild)


def heightOfTree(root):
    """Returns the height of a binary tree"""
    if not root:
        return 0
    
    return 1 + max(heightOfTree(root.rightChild), heightOfTree(root.leftChild))


def getDeepestNode(root):
    if  not root:
        return 
    else:
        queue = deque([root])
        deepest = None
        while queue:
            current_node = queue.popleft()
            deepest = current_node.data
            if current_node.leftChild:
                queue.append(current_node.leftChild)
            if current_node.rightChild:
                queue.append(current_node.rightChild)

        return deepest

def deleteDeepestNode(root, dNode ):
    if not root:
        return 
    else:
        queue = deque([root])
        queue.append(root)
        while queue:
            current_node = queue.popleft()
            if current_node.leftChild:
                if  current_node.leftChild is dNode:
                    current_node.leftChild = None
            else:
                queue.append(current_node.leftChild)
            
            if current_node.rightChild is None:
                if  current_node.rightChild is dNode:
                    current_node.rightChild = None
            else:
                queue.append(current_node.rightChild)

    

def deleteTree(root):
    root = None
    root.leftChild=None
    root.rightChild=None

    return "Tree is deleted"


    
g=TreeNode("new")



# Level 1
N1 = TreeNode('N1')

# Level 2
N2 = TreeNode('N2')
N3 = TreeNode('N3')

# Assign children to root
N1.leftChild = N2
N1.rightChild = N3

# Level 3
N4 = TreeNode('N4')
N5 = TreeNode('N5')
N6 = TreeNode('N6')
N7 = TreeNode('N7')


# Assign children to second level nodes
N2.leftChild = N4
N2.rightChild = N5
N3.leftChild = N6
N3.rightChild = N7


print(insertNode(N1,g))
print(print_tree(N1))
print(getDeepestNode(N1))
print(heightOfTree(N1))