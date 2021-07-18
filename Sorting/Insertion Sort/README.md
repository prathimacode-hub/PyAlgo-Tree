# Insertion Sort

## Aim

The main aim of the script is to sort numbers in list using insertion sort.


## Purpose

The main purpose is to sort list of any numbers in O(n) or O(n^2) time complexity.

## Short description of package/script

Takes in an array. <br>
Sorts the array and prints sorted array along with the number of swaps and comparisions made.
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

## Detailed explanation of script, if needed
To sort an array of size n in ascending order: <br>
1: Iterate from a[1] to a[n] over the array.  <br>
2: Compare the current element (val) to its predecessor.  <br>
3: If the val is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element. <br>

## Setup instructions

Download code and run it in any python editor. Latest version is always better.

## Compilation Steps

1.Edit array a and enter your array/list you want to sort.
2. Run the code

## Sample Test Cases
### Test case 1:  
input:<br>
a = [34,5,77,33] <br>

output :<br>

5, 33, 34, 77 along with <br>
no. of swaps = 3 <br>
no. of comparisons=5<br>

### Test case 2
input<br>
a=[90,8,11,3,2000,700,478] <br>

Output:<br>

No. of swaps= 8 <br>
No. of comparisions=12 <br>
Sorted Array is: <br>
 3  8  11  90  478  700  2000<br>
 
 ### Test case 3
 input<br>
 a=[0,33,7000,344,-88,2000]<br>
 
 output:<br>
 
No. of swaps= 6<br>
No. of comparisions=10<br>
Sorted Array is:<br>
-88  0  33  344  2000  7000<br>

## Output
<img width = 221 height = 27 src="../Insertion Sort/Images/input.png">
<img width = 385 height = 188 src="../Insertion Sort/Images/sort_output1.png">


## Author(s)

[Ritika Chand](https://github.com/RC2208)
