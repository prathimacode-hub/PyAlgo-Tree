"""
Segment trees are special kind of trees that allows answering range queries and updating values in an array effectively (both in O(logn)), 
For an array, its segment tree will have as leaf nodes = the elements of the array,
and its internal nodes store the value of a preprocessed value, like the sum of all its children

eg arr : [1,2,3,4]
parent node of (1,2) = 3, parent node of (3,4) = 7
parent node of (3,7) = 10 (this will also be the root node)

We are using an array approach to store the tree, so in above example :
tree = [0, 10, 3, 7, 1, 2, 3, 4]
index= [0,  1, 2, 3, 4, 5, 6, 7]
0 has been added as first element to ease the calculations
we can see the the array elements (leaf nodes) are stored as the second half of array
and the parent node of any index is such that index_of_parent = index_of_node / 2
like elements 1 and 2 at index 4 and 5, have their parent 3 at index 2 (4/2=2, 5/2=2.5=2)

"""

from math import ceil, log2

def segment_tree_creation (arr):
    """The function creates a segment tree in O(n) time
        arguments : array, whose corresponding segment tree is to be made
        returns : the correspoding segment tree in a list format
    """
    n = len(arr)

    # for n leaf nodes, there are maximum double of 2**max_height-1 nodes, adding extra 0th elem for ease of calculations 
    height = ceil(log2(n))
    m = 2*(2**height)
    tree = [0]*m        

    # filling the second half of the tree list (leaf nodes) with the array elements
    for i in range(n):
        index = i+int(m/2)
        tree[index] = arr[i]

    # creating the internal nodes, calculating the from leaf to the root
    for i in range(int(m/2)-1,0,-1):
        tree[i] = tree[2*i] + tree[2*i+1]
    
    return tree




# DRIVER CODE
if __name__ == '__main__':
    
    arr = [5, 8, 6, 3, 2, 7, 4, 6]
    print("\nOriginal array : ", arr)
    
    seg_tree = segment_tree_creation(arr)
    print("\nSegment tree : ", seg_tree, "\n")

    # input : [5, 8, 6, 3, 2, 7, 4, 6]
    # output: [0, 41, 22, 19, 13, 9, 9, 10, 5, 8, 6, 3, 2, 7, 4, 6]

    # input : [1,2,3,4]
    # output: [0, 10, 3, 7, 1, 2, 3, 4]

    # input : [-2, 5, 7, 1, 10]
    # output: [0, 21, 11, 10, 3, 8, 10, 0, -2, 5, 7, 1, 10, 0, 0, 0]

    