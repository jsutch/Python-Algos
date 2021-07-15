import random

class BSTNode(object):
    """
    A node has a value,a left object and a right object.
    Create a tree by creating a new single node:
    usage: foo = BSTNode(512)
    """
    def __init__(self, key):
        self.val = key
        self.left = self.right =  None


# BST Methods
def insert(root, node):
    """
    insert the given key into the BST
    usage: insert(bsttree, BSTNode(val))
    insert(foo, BSTNode(random.randint(1,4096)))
    """
    # case where root is empty
    if root is None:
        root = node
    else:
        # case where tree exists and value goes right
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def search(root, key):
    """
    Does key exist in the BST?
    usage: search(foo, 555)
    returns: value or False
    """
    if root is None:
        return False
    elif root.val == key:
        return root.val
    elif root.val > key:
        return search(root.left, key)
    return search(root.right, key)


def minvalue(node): 
    """
    return the smallest valued node. needed for delete
    """
    cursor = node 
    # loop down to find the leftmost leaf 
    while(cursor.left is not None): 
        cursor = cursor.left  
    return cursor  


def minvalueval(node): 
    """
    return the smallest valued node's value for testing
    """
    cursor = node 
    # loop down to find the leftmost leaf 
    while(cursor.left is not None): 
        cursor = cursor.left  
    return cursor.val


def aslist(node):
    """
    return inorder bst as a list. needed for randomval
    """
    if node is None:
        return []
    return aslist(node.left) + [node.val] + aslist(node.right)

def randomval(root):
    """
    return a random value from from the bst.
    utility to test delete. 
    """
    return random.choice(aslist(root))
    
def delete(root, key):
    """
    returns a BST without the deleted value
    """
    if root is None:
        return root
    # Is key in left or right?
    if key < root.val:
        root.left = delete(root.left, key)
    elif (key > root.val):
        root.right = delete(root.right, key)
    # Is root the key?
    else:
    # Case with no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # with two children get the inOrder successor
        # smallest on right subtree
        temp = minvalue(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    #
    return root



# Traversals
# Depth First traversals
def inorder(root):
    """
    DFT returns nodes in non-decreasing order
    print left -> root -> right
    """
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    """
    DFT used to create a copy of the tree
    print root -> left -> right
    """
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """
    DFT - used to delete a tree
    print left -> right -> root
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


# Breadth first Traversals
def height(node):
    """
    Find height of node. Needed for levelorder traversal
    """
    if node is None:
        return 0
    else:
        lh = height(node.left)
        rh = height(node.right)
        #
        if lh > rh:
            return lh + 1
        else:
            return rh + 1

def givenlevel(root, level):
    """
    find the givenlevel of the level. Needed for levelorder traversal
    """
    if root is None:
        return
    if level == 1:
        print(root.val)
    elif level > 1:
        givenlevel(root.left, level -1)
        givenlevel(root.right, level -1)

def levelorder(root):
    """
    levelorder is a Breadth First Traversal that prints all nodes per-level
    and iterates through the levels
    relies on height() and givenlevel() functions
    print all node values at level 1, then level 2, etc
    usage: levelorder(foo)
    """
    h = height(root)
    for i in range(1, h + 1):
        givenlevel(root, i)


def printlevel(root):
    [(print("=== Level", x, "==="), givenlevel(root, x)) for x in range(1,height(root))]


# Balancing a tree
# is a tree balanced?
def isbalanced(root):
    if root is None:
        return True
    return isbalanced(root.right) and isbalanced(root.left) and abs(height(root.left) - height(root.right)) <= 1

#
# breaking this into 3 parts - balance() is the wrapper, store() builds an inorder array of the values 
# and build() recursively rebuilds the inorder array into a balanced tree
# handing back to balance() to return the BST object
# creating an balanced BST from an unbalanced BST looks like this:
# newobject = balance(<BST object>)
#
def store(root, nodearr):
    """
    recreate the bst as an inorder array.
    needed by balance
    """
    if not root:
        return
    store(root.left, nodearr)
    nodearr.append(root.val)
    store(root.right, nodearr)


def build(nodearr):
    """
    rebuild the bst from the inorder array
    needed by balance
    """
    if not nodearr:
        return None
    mid = len(nodearr) // 2
    node = BSTNode(nodearr[mid])
    node.left = build(nodearr[:mid])
    node.right = build(nodearr[mid + 1:])
    return node


def balance(root):
    """
    - get inorder traversal of existing BST as an array
    - create a new BST object sorted by the midpoint
    - return the object
    """
    nodes = []
    store(root, nodes)
    return build(nodes)



# Helper code
# create and  populate a tree
"""
foo = BSTNode(500)
[insert(foo, BSTNode(random.randint(1,1024))) for x in range(20)]
"""

# test harness
# create tree
foo = BSTNode(500)
In [425]: type(foo)
Out[425]: <class '__main__.BSTNode'>

In [426]: foo.val
Out[426]: 500

[insert(foo, BSTNode(random.randint(1,1024))) for x in range(20)]
print("printlevels")
printlevel(foo)

# Traversing
print("Traversing Utils")
print("DFS traversing")
print("inorder traverse")
inorder(foo)
print("preorder traverse")
preorder(foo)
print("postorder traverse")
postorder(foo)
print("BFS traversing")
levelorder(foo)
# Balancing
print("is balanced?")
isbalanced(foo)
foo = balance(foo)
isbalanced(foo)
print("inorder - balanced")
inorder(foo)
print(aslist((foo)))

# Deletes
print("show bst as a list")
print(aslist(foo))
randvalue = randomval(foo)
print(f'grabbing random value <<{randvalue}>> from the bst for deletion')
print('verify value from search')
print(search(foo, randvalue))
print("Delete the value from the bst")
foo = delete(foo, randvalue)
print(f'search for value >>{randvalue}<< in bst')
print(search(foo, randvalue))
print(aslist(foo))
print('is the new tree balanced?')
print(isbalanced(foo))
