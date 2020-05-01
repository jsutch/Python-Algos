

Creating the Node class

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

insert(root, node):
"""
insert a new node with a given key
"""
    if root is None:
        root = node
    else:
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
    # if root is none or key is present in root
    if root is None or root.val == key:
        return root
    # key greater then root
    if root.val < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


"""
Traversals:
In-order, Pre-order, and Post-order traversals are Depth-First traversals.

For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.

Since a Binary Tree is also a Graph, the same applies here. The complexity of each of these Depth-first traversals is O(n+m).

Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree, the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.

The complexity then becomes O(n + n-1), which is O(n).

O(n), because you traverse each node once. Or rather - the amount of work you do for each node is constant (does not depend on the rest of the nodes).
"""

inorder(root):
"""
inorder traversal
In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
"""
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

preorder(root):
"""
Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree.
"""
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


postorder(root):
"""
Postorder traversal is used to delete the tree. 
"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


harness to create a tree
import random
def randint():
    return random.randint(1,4096)

root = Node(randint())
[insert(Node(randint)) for x in 100]


# Breadth First Traversals
"""
Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n) time where n is the number of nodes in the skewed tree. So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).
Space Complexity: O(n) in worst case. For a skewed tree, printGivenLevel() uses O(n) space for call stack. For a Balanced tree, call stack uses O(log n) space, (i.e., height of the balanced tree).
"""

def levelorder(root):
    h = height(root)
    for i in range(1, h + 1):
        givenlevel(root, i)

def height(node):
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
    if root is None:
        return
    if level == 1:
        print(root.val)
    elif level > 1:
        givenlevel(root.left, level -1)
        givenlevel(root.right, level -1)


"""
Show the levels of the tree:
What's the root node?

bar.val

what's the height?
In [228]: height(bar)
Out[228]: 6

In [227]: [(print("=== Level", x, "==="), givenlevel(bar, x)) for x in range(1,height(bar))]
=== Level 1 ===
785
=== Level 2 ===
387
961
=== Level 3 ===
113
697
904
=== Level 4 ===
46
147
647
=== Level 5 ===
17
=== Level 6 ===
42

"""


def delete(root, key):
    """
     currently borked
    """
    if root is None:
        return root
    # if the key is smaller, then left subtree
    if key < root.key:
        root.left = delete(root.left, key)
    # otherwise it's in the right subtree
    elif key > root.key:
        root.right = delete(root.right, key)
    # deleting the root node
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children. get the inorder successor
        temp = minimumvalue(root.right)
        # Copy inorder successor's content to this node
        root.key = temp.key
        # delete the inorder successor
        root.right = delete(root.right, temp.key)
        #
    return root


def minimumvalue(node):
    """
    Given a non-empty binary search tree, return the node
    with min key value found in that tree. Note that the
    entire tree does not need to be searched
    """
    current = node
    while(current.left is not None):
        current = current.left
    return current

"""
printing the miniumvalue of a tree:
In [240]: minimumvalue(bar).val
Out[240]: 17
"""


