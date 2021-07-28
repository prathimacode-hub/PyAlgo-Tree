# Lowest Common Ancestor in Binary Search Tree
# Time Complexity : O(log(n)) , Space Complexity : O(1)

"""
Binary trees are trees where any node can have only 0, 1 or 2 children, which are sorted in any order.
Binary Search trees have elements such that for a node, all elements in its left subtree are smaller than it, and all elements in its right subtree are greater than it.
Lowest Common Ancestor (LCA) of two given nodes is the shared ancestor of n1 and n2 that is located farthest from the root
or the last common node that occurs on the paths from root node to those nodes.

Here, we first check if both numbers exist in tree or not, with exists_in_tree() function by recursively traversing the tree.
If yes then we find the LCA of both the elements with find_lca() function, which follows as :
    if LCA isnt found yet, but current node is one of the elements, then current node is the LCA
    else if both elements are smaller than current node, LCA lies in left subtree
    else if both elements are greater than current node, LCA lies in right subtree
    else if both elements are in different subtrees, then current node is the LCA.

"""



class Node :
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None



def find_lca(node, n1, n2):    
    """Finds LCA of 2 numbers by recursively searching in left and right subtree
    input args : current node, the numbers whose lca is to be found
    returns : lca if found else None    
    Time complexity : O(log(n)), Space complexity : O(1)
    """
    if node==None:
        return None

    # if one element is found in current node, we return it 
    # the case where one element is ancestor of another, which is handeled here, as this node is tha lca
    if node.data == n1:
        return node
    elif node.data == n2:
        return node

    # Recursive calls
    if node.data > n1 and node.data > n2:       # if both elements are smaller than current node, LCA lies in left subtree
        return find_lca(node.left, n1, n2)
    elif node.data < n1 and node.data < n2:     # if both elements are greater than current node, LCA lies in right subtree
        return find_lca(node.right, n1, n2)
    else:                                       # if both elements are in different subtrees, then current node is the LCA     
        return node




def exists_in_tree(node, n):
    """This function finds if an element exists in a BST or not by recursively traversing the tree
        input : current node and the element to be found
        output : returns True if it exists, False if not
        Time complexity : O(log(n)), Space complexity : O(1)
    """
    if node == None:
        return False
    if node.data == n:
        return True
    
    if node.data > n:
        return exists_in_tree(node.left, n)
    elif  node.data < n:
        return exists_in_tree(node.right, n)
    else:
        return False


def lowest_common_ancestor_binary_search_tree(root, n1, n2):
    """This function checks if both elements are present in binary search tree or not, and depending upon that returns proper value
        input : root node of the tree, elements whose lca is to be found
        output : returns calculated LCA, if both exist, else None
        Both Time and Space complexity are : O(1)        
    """
    if exists_in_tree(root,n1) and exists_in_tree(root,n2):     # if both the elements exist in the tree
        return find_lca(root, n1, n2)                           # then we calculate its LCA
    else :
        return None                 # otherwise we give answer None



def print_output(lca, n1, n2):
    """Prints LCA of two numbers with a proper message if it exists"""
    if lca == None:
        print("\nElement does not exist in tree.\n")
    else:
        print(f"\nlca({n1}, {n2}) = {lca.data}\n")




# =========================== DRIVER CODE =========================

if __name__ == "__main__":

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    """
            20
           /  \ 
          8    22
         / \   
        4  12
           / \ 
          10  14
    """

      
    lca = lowest_common_ancestor_binary_search_tree(root, 10, 14)
    print_output(lca, 10, 14)
    lca = lowest_common_ancestor_binary_search_tree(root, 10, 22)
    print_output(lca, 10, 22)
    lca = lowest_common_ancestor_binary_search_tree(root, 4, 14)
    print_output(lca, 4, 14)



    # Other examples
    """
    lca = lowest_common_ancestor_binary_search_tree(root, 4, 8)
    print_output(lca, 4, 8)
    lca = lowest_common_ancestor_binary_search_tree(root, 4, 20)
    print_output(lca, 4, 20)
    lca = lowest_common_ancestor_binary_search_tree(root, 8, 8)
    print_output(lca, 8, 8)
    """
    
    """
    lca = lowest_common_ancestor_binary_search_tree(root, 20, 20)
    print_output(lca, 20, 20)
    lca = lowest_common_ancestor_binary_search_tree(root, 10, 225)
    print_output(lca, 10, 225)
    lca = lowest_common_ancestor_binary_search_tree(root, 40, 0)
    print_output(lca, 40, 0)
    """
