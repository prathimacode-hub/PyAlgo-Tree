# Problem name: Huffman Coding
# Approach: Greedy Method

# -----------------------------------------------------------------------------------------------

# Problem Statement: Huffman coding is a lossless data compression algorithm. 
#                    The idea is to assign variable-length codes to input 
#                    characters, lengths of the assigned codes are based on the 
#                    frequencies of corresponding characters. The most frequent 
#                    character gets the smallest code and the least frequent 
#                    character gets the largest code.

# -----------------------------------------------------------------------------------------------

# Constraints:
# chars[] -> set of characters/array of characters.
# freq[] -> frequency of each of the characters in the given set.

# -----------------------------------------------------------------------------------------------

# importing the library named as heapq for the implementation of the huffman tree.
import heapq

# class node defined as the back bone of the node class 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
         
    def __lt__(self, nxt):
        return self.freq < nxt.freq
         
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):
     
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print("     {0}      ->        {1}".format(node.symbol, newVal))
 
 
# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']
 
# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]

print ("-- Huffman Coding using Greedy Method --")
print ()
print ("Provided input for implementing the Huffman Tree...")
print ("Characters        Frequency")
print ("---------------------------")
for k in range (0, len(chars)):
    print ("     {0}      ->        {1}".format(chars[k],freq[k]))
print ()

 
# list containing unused nodes
nodes = []
 
# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))
 
while len(nodes) > 1:
     
    # sort all the nodes in ascending order
    # based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
 
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
 
    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    heapq.heappush(nodes, newNode)
 
# Huffman Tree is ready!
print ("Creating Huffman Tree...\n")
print ("Your Huffman Tree is ready! Here you go...")
print ()
print ("Characters       Huffman Code")
print ("-----------------------------")
printNodes(nodes[0])


# -----------------------------------------------------------------------------------------------

# Output:
# -- Huffman Coding using Greedy Method --

# Provided input for implementing the Huffman Tree...
# Characters        Frequency
# ---------------------------
#      a      ->        5
#      b      ->        9
#      c      ->        12
#      d      ->        13
#      e      ->        16
#      f      ->        45

# Creating Huffman Tree...

# Your Huffman Tree is ready! Here you go...

# Characters       Huffman Code
# -----------------------------
#      f      ->        0
#      c      ->        100
#      d      ->        101
#      a      ->        1100
#      b      ->        1101
#      e      ->        111

# -----------------------------------------------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2022

# -----------------------------------------------------------------------------------------------
