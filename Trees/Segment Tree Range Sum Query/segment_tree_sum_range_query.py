"""
Sum range query is the sum of all elements in an array over a given range (l, r) both included, where l and r are the indicies.
eg for arr = [1,2,3,4], sum_range(0,2) = 1+2+3 = 6
The above approach has time complexity : O(n) 
It can be improved by using the segment trees.

Segment trees are special kind of trees that allows answering range queries and updating values in an array effectively (both in O(logn)), 
For an array, its segment tree will have as leaf nodes = the elements of the array,
and its internal nodes store the value of a preprocessed value, like the sum of all its children.

eg arr : [1,2,3,4] can be converted to a segment tree : [0, 10, 3, 7, 1, 2, 3, 4]
where 0 has been added as first element to ease the calculations

For sum range query, the internal nodes store the sum of their children nodes.
With segment trees, instead of going to every element, we already have the sum calculated in the parent node, so we just need to get that.
to get above example of sum_range(0,2) = 1+2+3 :-
tree : [0, 10, 3, 7, 1, 2, 3, 4]
index: [0,  1, 2, 3, 4, 5, 6, 7]
l = 4, r = 6 are the tree indices
elem 1 and 2 have a common parent, where elem 3 has no common parent with others, so we add tree[r] = 3 to range_sum and shift r left, 
that is, we move r to left if it is even. Similarly, l will have to be moved forward if it is odd.
now l = 4, r = 5, range_sum=3, and we move to parent of both l and r
l = 2, r = 2, now r is even, so tree[r]=tree[2]=3 is added to range_sum. range_sum = 3+3 = 6, r = 1
so we stop, range_sum is our answer

"""

from math import ceil, log2


def segment_tree_range_sum_query (tree, l, r):
    """The function tells the sum of elements in a given range using the segment tree in O(log(n))
        input : segment tree, array starting and ending index of range
        returns the sum of elements of array in that range"""

    m = len(tree)
    l,r = l+m//2, r+m//2    # converting array index to segment tree index
    rsum = 0
    while (l<=r) :          # while the lower and upper limit do not cross each other
        if l%2 == 1:        # if lower range index is a right child, add that and jump to next index (towards right)
            rsum += tree[l]
            l += 1
        if r%2 == 0:        # if upper range index is a left child, add that and jump to next index (towards left)
            rsum += tree[r]
            r -= 1

        l, r = l//2, r//2       # both the indices are have a common ancestor in tree, so move up, till that ancestor
        

    return rsum

    
    
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
    print("\nSegment tree : ", seg_tree)

    range_sum = segment_tree_range_sum_query(seg_tree, 1, 7)    # 8 + 6 + 3 + 2 + 7 + 4 + 6 = 36
    print("\nRange sum index 1-7 = ", range_sum)

    range_sum = segment_tree_range_sum_query(seg_tree, 2, 4)    # 6 + 3 + 2 = 11
    print("\nRange sum index 2-4 = ", range_sum)
 
    range_sum = segment_tree_range_sum_query(seg_tree, 5, 5)    # 7
    print("\nRange sum index 5-5 = ", range_sum)

    print()


"""
    arr = [-2, 5, 7, 1, 10]
    print("\nOriginal array : ", arr)    
    seg_tree = segment_tree_creation(arr)
    print("\nSegment tree : ", seg_tree)

    range_sum = segment_tree_range_sum_query(seg_tree, 0, 0)    # -2
    print("\nRange sum index 0-0 = ", range_sum)

    range_sum = segment_tree_range_sum_query(seg_tree, 0, 4)    # -2 + 5 + 7 + 1 + 10 = 21
    print("\nRange sum index 0-4 = ", range_sum)
 
    range_sum = segment_tree_range_sum_query(seg_tree, 3, 4)    # 1 + 10 = 11
    print("\nRange sum index 3-4 = ", range_sum)

    print()
"""



    # arrays for test input. Can further try with different index
    # input : [5, 8, 6, 3, 2, 7, 4, 6]
    # input : [1,2,3,4]
    # input : [-2, 5, 7, 1, 10]
    