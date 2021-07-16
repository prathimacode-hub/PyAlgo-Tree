"""
Here we are updating, such that the segment tree internal nodes, store the sum of the children.

Segment trees are special kind of trees that allows answering range queries and updating values in an array effectively (both in O(logn)), 
For an array, its segment tree will have as leaf nodes = the elements of the array,
and its internal nodes store the value of a preprocessed value, like the sum of all its children.

eg arr : [1,2,3,4] can be converted to a segment tree : [0, 10, 3, 7, 1, 2, 3, 4]
where 0 has been added as first element to ease the calculations

On updating, say changing 1 -> -1 on index 0
arr becomes = [-1, 2, 3, 4]
we need to only update the parent nodes (which are at index/2 of a node). So, no of queries = height of tree O(log(n)), 
instead of updating boxes in sqrt decomposition O(sqrt(n)), and all the sums in dp approach O(n)
so updated tree = [0, 8, 1, 7, -1, 2, 3, 4]

"""

from math import ceil, log2


def segment_tree_update_query (arr, tree, index, value):
    """The function updates the node in array (leaf node) and all its parent nodes till root node, complexity = O(log(n))
        input: array to be updated, tree to be updated, index of array, new value
        returns : updated array and the tree
    """
    arr[index] = value
    m = len(tree)
    i = m//2 + index        # getting the index according to the tree from array index
    change = value - tree[i]
    while i>0 :
        tree[i] += change   # updating the current nodes
        i = i//2        # going to update the parent 
    return arr, tree
    
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
    print("\nOriginal Segment tree : ", seg_tree, "\n")

    arr, seg_tree = segment_tree_update_query(arr, seg_tree, 2, 5)       # changing to 6 -> 5 at index 2
    print("\nUpdated array tree : ", arr)
    print("Updated Segment tree : ", seg_tree, "\n")
    
    arr, seg_tree = segment_tree_update_query(arr, seg_tree, 0, 10)       # changing to 5 -> 10 at index 0
    print("\nUpdated array tree : ", arr)
    print("Updated Segment tree : ", seg_tree, "\n")
    
    arr, seg_tree = segment_tree_update_query(arr, seg_tree, 6, -5)       # changing to 4 -> -5 at index 6
    print("\nUpdated array tree : ", arr)
    print("Updated Segment tree : ", seg_tree, "\n")



"""
    arr = [-2, 5, 7, 1, 10]
    print("\nOriginal array : ", arr)
    
    seg_tree = segment_tree_creation(arr)
    print("\nOriginal Segment tree : ", seg_tree, "\n")

    arr, seg_tree = segment_tree_update_query(arr, seg_tree, 2, 5)       
    print("\nUpdated array tree : ", arr)
    print("Updated Segment tree : ", seg_tree, "\n")
    
    arr, seg_tree = segment_tree_update_query(arr, seg_tree, 0, 10)      
    print("\nUpdated array tree : ", arr)
    print("Updated Segment tree : ", seg_tree, "\n")
    
    arr, seg_tree = segment_tree_update_query(arr, seg_tree, 1, 6)   
    print("\nUpdated array tree : ", arr)
    print("Updated Segment tree : ", seg_tree, "\n")


"""

    # arrays for test input. Can further try with different index
    # input : [5, 8, 6, 3, 2, 7, 4, 6]
    # input : [1,2,3,4]
    # input : [-2, 5, 7, 1, 10]
    
