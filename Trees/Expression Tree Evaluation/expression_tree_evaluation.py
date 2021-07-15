# The expression tree is a binary tree in which each internal node corresponds to the operator like +,-,*,/,^ and 
# each leaf node corresponds to the operand so for example expression tree for 3 + ((5+9)*2) - 3,5,9,2 will be leaf nodes
# and +,+,* will be internal and root nodes. It can be used to represent an expression.
# It can be calculated to a single value, by performing the operator in the node on its children operands.
# for example, a node (*) having two children nodes (4) and (5), can be evaluated as 4*5 = 20, so,
# the subtree with (*) as root node, can be replaced with a single node (20)


# Here we have followed a recursive approach to first evaluate the left and right child of an operator to a single value as in the above example,
# and then evaluate that operation itself, finally returning the evaluated value calculated with the eval() function of python.

class Node :
    """Class to define tree nodes, 
        this has a value attribute to store the value, and 
        left and right attributes to point to the left and right child respectively"""
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
def expression_tree_evaluation (node):
    """A recursive function which evaluates the expression subtree passed to it
        and returns the evaluated value"""
    if node == None:    # Node doesn't exist
        return 0
    if node.left == None and node.right == None:    # leaf node containing an operand
        return node.value
    
    # node is an operator
    left_child = expression_tree_evaluation(node.left)
    right_child = expression_tree_evaluation (node.right)

    return eval(str(left_child)+node.value+str(right_child))


# DRIVER CODE

if __name__ == '__main__':
    # Expression in the example : (5*4)+(100-2)
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('20')
    print("\nExpression :  (5*4)+(100-2)" )
    print ("\nEvaluation : ", expression_tree_evaluation(root), "\n")
    
    # Other examples which can be similarly created and tested :-
    #  3 + ((5+9)*2) = 31
    """ 
    root = Node('+')
    root.left = Node('3')
    root.right = Node('*')
    root.right.right = Node('2')
    root.right.left = Node('+')
    root.right.left.left = Node('5')
    root.right.left.right = Node('9')
    """
    #  3 + (2 * 6) + 5 * (4 + 8) = 75
    
    
    
    
    
