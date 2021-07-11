# Determining DNA Health

## Aim
The aim of this codebase is to find out the solution of the given problem statement, 
- Given an array of beneficial gene strings `genes = [g0, g1,...,gn-1]`. Note that these gene sequences are not guaranteed to be distinct.
- An array of gene health values, `health = [h0,h1,...,hn-1]` , where each **_h<sub>i</sub>_**  is the health value for gene .
- A set of **_s_**  DNA strands where the definition of each strand has three components, **_start_** ,**_end_** , and **_d_**, where **_d_** string  is a DNA for which **_g<sub>start</sub>_**,....,**_g<sub>end</sub>_** genes  are healthy.

Find and print the respective total healths of the unhealthiest (minimum total health) and healthiest (maximum total health) strands of DNA as two space-separated values on a single line.

*************************************
## Purpose
Understanding implementations of Strings Data Structure using Interview like problems.
*************************************
## Short Description of the script
- The script will help to understand the string data structure at real life problems.
- The script will also help the students about the approach of a problem which is asked in job interviews.
- The packages used here are, `math`, `bisect` and `collections`. These are the basic packages of Python programming!
***************************************
## Workflow of the codebase
- Firstly, import all the packages, as mentioned earlier.
- Take inputs from the user. User given input is more acceptable because it provides the interaction between the learner and developer.
- Process the user given data through some operations before implementing the final function.
- Implement the `GetHealth` function, which will find out the output for this script.
- Tada! The output is generated!!
***************************************
## Detailed Explanation of the script
**Input Format**
- The first line contains an integer, n, denoting the total number of genes.
- The second line contains n space-separated strings describing the respective values of `[g0, g1,...,gn-1]`(i.e., the elements of `genes`).
- The third line contains n space-separated integers describing the respective values of `[h0,h1,...,hn-1]` (i.e., the elements of `health`).
- The fourth line contains an integer, s , denoting the number of strands of DNA to process.
- Each of the s subsequent lines describes a DNA strand in the form `start end d`, denoting that the healthy genes for DNA strand d are **_g<sub>start</sub>_**,....,**_g<sub>end</sub>_** and their respective correlated health values are **_h<sub>start</sub>_**,....,**_h<sub>end</sub>_** .

**Constraints**


**Output Format**

Print two space-separated integers describing the respective total health of the unhealthiest and the healthiest strands of DNA.

### Explanation
Taking a sample input, it will be easier to understand with it!

User Input :
```
Enter the number of the genes : 
6
Enter the values of the genes in a space separated manner : 
a b c aa d b
Enter the values of the health in a space seprated manner :
1 2 3 4 5 6
Enter the number of strands of DNA to process : 
3
Enter DNA strands : 
1 5 caaab
0 4 xyz
2 4 bcdybc
```
Let's visualize it -

The ranges of beneficial genes for a specific DNA on the left are highlighed in green and individual instances of beneficial genes on the right are bolded. The total healths of the `s = 3` strands are:

1. Taking the first DNA strand,
d = caaab
first = 1
last = 5

|genes |   `c`aaab |   c`aa`ab   | ca`aa`b  |  caaa`b` |  caaa`b`|
|:---:|:---:|:---:|:---:|:---:|:-:|
|values |      3    |     4      |    4      |   2     |    6|

Hence, the total health of `caaab` is `3 + 4 + 4 + 2 + 6 = 19`

2. Taking the second DNA strand,
d = xyz
first = 0
last = 4

genes | xyz |
|:-:|:-:|
|values|0|

Hence, the total health of `xyz` is `0`

3. Taking the third DNA strand,
d = bcdybc
first = 2
last = 4

genes | b`c`dybc |bc`d`ybc|bcdyb`c`|
|:-:|:-:|:-:|:-:|
|values|3|5|3|

Hence, the total health of `bcdybc` is `3 + 5 + 3 = 11`

The unhealthiest DNA strand is xyz with a total health of `0`, and the healthiest DNA strand is caaab with a total health of `19` . Thus, we print `0 19` as our answer.

- Time Complexity :  **_O(L<sub>g</sub> . s . d + n<sup>(1/d)</sup> . L<sub>q </sub>)_**


************************************************************************
## Setup Instructions
- Open any Python editor, I have used Jupyter Notebook here.
- Python version 3.7 must be installed in your device

************************************************************************
## Compilation Steps
- Importing the packages.
- Take all the user given data.
  1. Enter the number of the genes.
  2. Enter the values of the genes in a space separated manner.
  3. Enter the values of the health in a space seprated manner.
  4. Enter the number of strands of DNA to process.
  5. Enter DNA strands.
- Processing and finding out the maximum data point.
- Deploying the main function, `GetHealth`.
- The main function `GetHealth` returns outputs after successful compilation.
- Print the output!
************************************************************************
## Output
- Test Case #1

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-1/Strings/Determining%20DNA%20Health/Images/dna1.png)

- Test Case #2

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-1/Strings/Determining%20DNA%20Health/Images/dna2.png)

- Test Case #3

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-1/Strings/Determining%20DNA%20Health/Images/dna3.png)

- Test Case #4

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-1/Strings/Determining%20DNA%20Health/Images/dna4.png)

- Test Case #5

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-1/Strings/Determining%20DNA%20Health/Images/dna5.png)

------------------------------------------------
## Resources


The algorithm used here is named as `Knuth–Morris–Pratt algorithm`. If you want to learn more about the algorithm and implement it other problems, then visit [here](https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/). You'll get all the details!

------------------------------------------------
## Author
Code Contributed by, Abhishek Sharma, DCP21, [abhisheks008](https://github.com/abhisheks008) 
<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
