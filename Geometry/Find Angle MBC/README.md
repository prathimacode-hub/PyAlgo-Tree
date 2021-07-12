# Find Angle MBC

## Aim
![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-3/Geometry/Find%20Angle%20MBC/Images/mbc6.png)

`ABC` is a right triangle with `90°` at `B`
Therefore `∠ABC = 90°`
Point `M` is the midpoint of hypotenuse .
You are given the lengths `AB` and `BC`.
The task is to find `∠MBC`  (angle `θ°`, as shown in the figure) in degrees.

The problem is taken from the HackerRank website, you can check out the problem [here](https://www.hackerrank.com/challenges/find-angle/problem)

*************************************
## Purpose
Understanding how we can implement classic geometry questions using the Python 3.7 language or, programming!
*************************************
## Short Description of the script
- This script will help you how can we use Python programming to solve the typical geometry questions.
- This script will also provide you the basic idea of `math` package in the code.
- Implementation of `cosine` function is also shown in the code but using Python here.
- To implement this whole script the codebase needs to have an in built package is called `math`.
***************************************
## Workflow of the codebase
- Firstly, import all the packages, as mentioned earlier.
- Take inputs from the user. User given input is more acceptable because it provides the interaction between the learner and developer.
- Process the user given data through some operations before implementing the final function.
- Set the functions to find out the desired the angle.
- Make the output as print ready before the final declaration.
***************************************
## Detailed Explanation of the script
**Input Format**

The first line contains the length of side `AB`.
The second line contains the length of side `BC`.


**Output Format**

Output `∠MBC` in degrees.

_Note_: Round the angle to the nearest integer.

### Explanation

Let's find out the detailed explanation of this script here!

User Input :

```
Enter the value of AB : 
35
Enter the value of BC : 
45
```
Steps for the model -
1. Firstly the model imported the `math` package, which will provide the luxury to do the following steps without any hesitation.
2. Taking all the required inputs, here we are taking the lengths of the two sides as `AB` and `BC`.
3. After that, find out the hypotenuse by the theorm of Pythagorus.
4. As the hypotenuse is calculated the two sides of the desired angle is exposed.
5. Using the cosine function find out the desired angle in `radian`.
6. After that, changing that angle's unit into `degree`.
7. Tada! The problem is solved and we get our desired output!

************************************************************************
## Setup Instructions
- Open any Python editor, I have used Jupyter Notebook here.
- Python version 3.7 must be installed in your device.
- Your system must have the Python package called `math`, without that this script will not be run!

************************************************************************
## Compilation Steps
- Importing the packages and libraries.
- Take all the user given data.
  1. Enter the length of AB.
  2. Enter the length of BC.
- Processing the data collected from the user.
- Find out the hypotenuse.
- Finding out the desired angle in radian using cosine function.
- Change the unit into degree.
- Print the output!
************************************************************************
## Output
- Test Case #1

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-3/Geometry/Find%20Angle%20MBC/Images/mbc1.png)

- Test Case #2

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-3/Geometry/Find%20Angle%20MBC/Images/mbc2.png)

- Test Case #3

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-3/Geometry/Find%20Angle%20MBC/Images/mbc3.png)

- Test Case #4

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-3/Geometry/Find%20Angle%20MBC/Images/mbc4.png)

- Test Case #5

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-3/Geometry/Find%20Angle%20MBC/Images/mbc5.png)

------------------------------------------------

## Author
Code Contributed by, Abhishek Sharma, DCP21, [abhisheks008](https://github.com/abhisheks008) 
<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
