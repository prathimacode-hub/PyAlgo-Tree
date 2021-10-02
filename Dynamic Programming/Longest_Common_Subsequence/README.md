
# Longest Common Subsequence 
### Aim 
- The aim of the script is to find out the maximum length of the common sequence between two strings.

### Purpose
- The main purpose of this script is to show the implementaion of recursion to solve the Longest Common Subsequence.

### Description
Given two string and determine the length of the string which is common subsequence.

### Workflow
`Input:`
s1 = "ABCDEFG", 
s2 = "DEFGHI"

`output:`
Length of the LCS: 4

### Explanation
- Find the number of subsequences with lengths ranging from 1,2,..n-1. In Recursion we first passed the two string and length of the two string as parameters.
- We first find the size of the both string if they are both empty string then we return 0.
- And if we matching the charcter of two string and those two charcters are matched then we add one.
- Otherwise we check, if next charcter is match to the this charcter than we go to that side and decrease the size of the string and add one to our answer.
- At the last we get the length of the longest common subsequence.

### Time and Space Complexity
- Time Complexity: `O(len_of_string1*len_of_string2)`
- Space Complexity:`O(len_of_the_lcs)` 


