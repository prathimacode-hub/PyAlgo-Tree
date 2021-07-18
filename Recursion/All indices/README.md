# All indices of an element in an array.  

## Aim

The aim is to create a python code to get all indices of an element in an array.

## Purpose

The purpose is to come up with an efficient solution while implementing recursion.

## Short description of project
The program takes 3 inputs.
1.size of array.
2.Array elements.
3.Elements whose occurrence is to be found.

## Workflow of the Project
* We will divide the array into 2 parts.
1.The first element.
2. THE remaining elements.
*We will work on first element and recursion will work on rest.
* First we define the base case which will be if start=end  return empty array.
* Then we will call recursion on other part of array.
* Now we will check if our first element is equal to the element whose occurrence is to be checked.
* If yes then we will insert 0 in our output array and shift other elements of array to right.
* If no then we will return our Output array.


## Required libraries

None

## Compilation Steps
Run the script, after that :
  
 1. User is prompted to enter size of array followed by array elements and number whose occurrence is to be checked.
 2. All the indices on which the element occurred is printed.


# Output
![](Images/Output-img.jpg)


## Author
[Siddhi Bhanushali](https://github.com/siddhi-244)
