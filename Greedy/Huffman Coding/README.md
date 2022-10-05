# Huffman Coding using Greedy Approach
🔴 Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the huffman code of each characters presented in the list in an ascending order.

## 👉 Purpose
The main purpose of this script is to show the implementation of Greedy Approach to find out the the huffman code of each characters presented in the list in an ascending order.

## 📄 Description
Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. The most frequent character gets the smallest code and the least frequent character gets the largest code.

The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream. 

🔴 Examples: 

```
Constraints:
chars[] -> an array of characters.
freq[] -> an array of frequencies of the respective characters.

Input:
character   Frequency
    a           5
    b           9
    c           12
    d           13
    e           16
    f           45
    
After processing through the algorithm, it will generate the Huffman codes 
for each of the characters presented in an ascending order.

The output will be like this,
character   Huffman Code
    f          0
    c          100
    d          101
    a          1100
    b          1101
    e          111
```

## 🧮 Workflow & Algorithm
Let's discuss the workflow and the algorithm with the above mentioned example.
- Build a min heap that contains 6 nodes where each node represents root of a tree with single node.
- Extract two minimum frequency nodes from min heap. Add a new internal node with frequency `5 + 9 = 14.`
```
                14
              /    \
             /      \
         a -> 5    b -> 9

Now min heap contains 5 nodes where 4 nodes are roots of trees with single element each, 
and one heap node is root of tree with 3 elements

The tree will be now,
  character         Frequency
       c               12
       d               13
 Internal Node         14
       e               16
       f               45
```
- Step 3: Extract two minimum frequency nodes from heap. Add a new internal node with frequency `12 + 13 = 25`
```
                25
              /    \
             /      \
        c -> 12    d -> 13
        
Now min heap contains 4 nodes where 2 nodes are roots of trees with single element each, 
and two heap nodes are root of tree with more than one nodes

   character       Frequency
Internal Node          14
       e               16
Internal Node          25
       f               45        
```
- Extract two minimum frequency nodes. Add a new internal node with frequency `14 + 16 = 30`
```
                       30
                     /    \
                    14   e -> 16
                   /  \
                  /    \
               a -> 5  b -> 9

Now min heap contains 3 nodes.

   character       Frequency
Internal Node         25
Internal Node         30
      f               45 
```
- Extract two minimum frequency nodes. Add a new internal node with frequency `25 + 30 = 55`
```
                    55
                  /    \
                 /      30
                /      /   \
               25     14    e -> 16
             /    \  /  \
            c     d  a   b
           12    13  5   9

Now min heap contains 2 nodes.

character     Frequency
       f         45
Internal Node    55
```
- Extract two minimum frequency nodes. Add a new internal node with frequency `45 + 55 = 100`
```
                100
               /   \ 
            f->45   \
                    55
                  /    \
                 /      30
                /      /   \
               25     14    e -> 16
             /    \  /  \
            c     d  a   b
           12    13  5   9
           
Now min heap contains only one node.

character      Frequency
Internal Node    100           
```
- Since the heap contains only one node, the algorithm stops here.
- **Steps to print codes from Huffman Tree:** Traverse the tree formed starting from the root. Maintain an auxiliary array. While moving to the left child, write 0 to the array. While moving to the right child, write 1 to the array. Print the array when a leaf node is encountered.
```
          (0)   100   (1)
               /   \ 
            f->45   \
                    55
                  /    \   (1)
          (0)    /      30
                /  (0) /   \  (1)
               25     14    e -> 16
             /    \  /  \
            c     d  a   b
           12    13  5   9
          (0)   (1) (0) (1)
```
- The codes are as follows:
```
character   code-word
    f          0
    c          100
    d          101
    a          1100
    b          1101
    e          111
```

## 💻 Input and Output 
- **Test Case 1 :**
```python
Input Given :
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [ 5, 9, 12, 13, 16, 45]
```

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Huffman%20Coding/Images/hc-1.png)

- **Test Case 2 :**
```python
Input Given :
chars = ['a', 'b', 'c', 'd']
freq = [ 5, 1, 6, 3]
```
![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Huffman%20Coding/Images/hc-2.png)

## ⏰ Time and Space complexity
- **Time Complexity :** `O(n*log n)`.
- **Space Complexity :** `O(n*log n)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2022 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
