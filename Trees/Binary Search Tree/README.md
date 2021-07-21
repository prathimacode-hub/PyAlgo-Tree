### Script Name
Binary Search Tree.

### Aim
To write a program for Binary Search Tree.

### Purpose
To get a understanding about different operations performed in Binary Search Tree.
This program contains the menu-based implementation of the basic operations on a BST:
1. Insert Node into BST
2. Search Node in BST
3. Delete Node in BST
4. Print BST (inorder way)

### Short description of package/script
It is a python program of Binary Search Tree.
It is written in a way that it takes user input.

### Workflow of the Project
First the function are written to perform different operations in Binary Search Tree.
Then outside the function user input is taken.

### Detailed explanation of script, if needed
IMPLEMENTATION OF BINARY SEARCH TREE (BST)
Binary Search Tree is a special type of binary tree where:
1. The value of all the nodes in the left sub-tree is less than or equal to the value of the root.
2. The value of all the nodes in the right sub-tree is greater than value of the root.
3. This rule will be recursively applied to all the left and right sub-trees of the root.

Illustration to insert in below tree: 
1. Start from the root. 
2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for right. 
3. After reaching the end, just insert that node at left(if less than current) else right. 

         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500 
     /  \                              /  \  
    10   30                           10   30
                                              \   
                                              40

llustration to search in tree: 
1. Start from the root. 
2. Compare the searching element with root, if less than root, then recurse for left, else recurse for right. 
3. If the element to search is found anywhere, retun the element else print element not found. 

         100                               
        /   \        search 20            
      20     500    --------->      Found 20     
     /  \                               
    10   30 

llustration to delete in below tree: 
1. Start from the root. 
2. Compare the deleting element with root, if less than root, then recurse for left, else recurse for right. 
3. If the element to delete is found anywhere, delete the element else print element not found. 

        
              50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70 
                 /  \                            \ 
                60   80                           80

### Setup instructions
Just clone the repository .

### Output
<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/9606669f3d21028f99850fd311850341526ecec3/Trees/Binary%20Search%20Tree/Images/output1.png">

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/9606669f3d21028f99850fd311850341526ecec3/Trees/Binary%20Search%20Tree/Images/output2.png">

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/9606669f3d21028f99850fd311850341526ecec3/Trees/Binary%20Search%20Tree/Images/output3.png">

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/9606669f3d21028f99850fd311850341526ecec3/Trees/Binary%20Search%20Tree/Images/output4.png">

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/9606669f3d21028f99850fd311850341526ecec3/Trees/Binary%20Search%20Tree/Images/output5.png">

### Author(s)
Neha Jha
