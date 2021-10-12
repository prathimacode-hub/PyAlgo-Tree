'''
    Inorder Traversal of Binary Tree:
    In the Inorder Traversal first the left node of the tree will be printed, 
    than the root node, and at end right node will be printed for every Sub-tree,
    Just like: (A+B)

    Preorder Traversal of Binary Tree:
    In the Preorder Traversal first the left node of the tree will be printed, 
    than the right node, and at end root node will be printed for every Sub-tree,
    Just like: (AB+)

    Postorder Traversal of Binary Tree:
    In the Inorder Traversal first the root node of the tree will be printed, 
    than the left node, and at end right node will be printed for every Sub-tree,
    Just like: (+AB)
'''
# Defination of Class Node.
class Node:
    # Defination of Node class constructor.
    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.data = data
    
    # inorder() function defination,
    # that will print the Inorder Traversal of given tree.
    def inorder(self, root: object)->None:
        if(root):
            root.inorder(root.left)
            print("[", root.data,"]", end ="\t")
            root.inorder(root.right)
    
    # preorder() function defination,
    # that will print the Preorder Traversal of given tree.
    def preorder(self, root: object)->None:
        if(root):
            print("[", root.data,"]", end ="\t")
            root.preorder(root.left)
            root.preorder(root.right)
    
    # Postorder() function defination,
    # that will print the Postorder Traversal of given tree.
    def postorder(self, root: object)->None:
        if(root):
            root.postorder(root.left)
            root.postorder(root.right)
            print("[", root.data,"]", end ="\t")


'''
Structure of Tree:

Test Case 01: 
               11
            /      \
          9         15
        /  \       /  \
      7     10   13    20
    /  \
   5    8

Test Case 02: 
        10
      /    \
    20      30
           /   \
          40    50
               /  \
             60    70
'''
# main function or the driver function.
if __name__ == '__main__':
    '''
    Formation of tree,
    as per Test Case 01.
    '''
    root = Node(11)
    root.left = Node(9)
    root.right = Node(15)
    root.left.left = Node(7)
    root.left.right = Node(10)
    root.right.left = Node(13)
    root.right.right = Node(20)
    root.left.left.left = Node(5)
    root.left.left.right = Node(8)

    print("\n***Running Test Case 01***", end = " ")
    # Printing the Inorder Traversal for Test Case 01.
    print("\nInorder Traversal :")
    root.inorder(root)
    # Printing the Preorder Traversal for Test Case 01.
    print("\n\nPreorder Traversal :")
    root.preorder(root)
    # Printing the Postorder Traversal for Test Case 01.
    print("\n\nPostorder Traversal :")
    root.postorder(root)

    '''
    Formation of tree,
    as per Test Case 02.
    '''
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    root.right.right.left = Node(60)
    root.right.right.right = Node(70)

    print("\n\n***Running Test Case 02***", end = " ")
    # Printing the Inorder Traversal for Test Case 01.
    print("\nInorder Traversal :")
    root.inorder(root)
    # Printing the Preorder Traversal for Test Case 01.
    print("\n\nPreorder Traversal :")
    root.preorder(root)
    # Printing the Postorder Traversal for Test Case 01.
    print("\n\nPostorder Traversal :")
    root.postorder(root)

'''
Sample Output:

***Running Test Case 01***
Inorder Traversal :
[ 5 ]   [ 7 ]   [ 8 ]   [ 9 ]   [ 10 ]  [ 11 ]  [ 13 ]  [ 15 ]  [ 20 ]

Preorder Traversal :
[ 11 ]  [ 9 ]   [ 7 ]   [ 5 ]   [ 8 ]   [ 10 ]  [ 15 ]  [ 13 ]  [ 20 ]

Postorder Traversal :
[ 5 ]   [ 8 ]   [ 7 ]   [ 10 ]  [ 9 ]   [ 13 ]  [ 20 ]  [ 15 ]  [ 11 ]

***Running Test Case 02***
Inorder Traversal :
[ 20 ]  [ 10 ]  [ 40 ]  [ 30 ]  [ 60 ]  [ 50 ]  [ 70 ]

Preorder Traversal :
[ 10 ]  [ 20 ]  [ 30 ]  [ 40 ]  [ 50 ]  [ 60 ]  [ 70 ]

Postorder Traversal :
[ 20 ]  [ 40 ]  [ 60 ]  [ 70 ]  [ 50 ]  [ 30 ]  [ 10 ]
'''