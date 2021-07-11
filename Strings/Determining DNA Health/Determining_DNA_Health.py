# Determining DNA Health

# Category of the problem : Strings
# Difficulty : Hard
# Challenge taken from HackerRank
# Language used Python 3

'''
Problem Statement : Find and print the respective total healths of the unhealthiest
                    (minimum total health) and healthiest (maximum total health) 
                    strands of DNA as two space-separated values on a single line
'''


# Importing the required libraries and packages
from math import inf
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict

# Algorithm used here, Knuth–Morris–Pratt algorithm
# to know more about the algorithm check out the README.md file.

print ('Determining DNA Health Problem')
print ('-----------------------------')

# Creating the function called getHealth which will determine the health of the DNA
def getHealth(seq, first, last, largest):
  h, ls = 0, len(seq)
  for f in range(ls):
    for j in range(1, largest+1):
      if f+j > ls: break
      sub = seq[f:f+j]
      if sub not in subs: break
      if sub not in gMap: continue
      ids, hs = gMap[sub]
      h += hs[bRight(ids, last)]-hs[bLeft(ids, first)]
  return h

# Taking all the inputs

# 1. Enter the number of genes
print ('Enter the number of the genes : ')
howGenes = int(input())

# 2. Enter the values of the genes in a space separated manner
print ('Enter the values of the genes in a space separated manner : ')
genes = input().rstrip().split()

# 3. Enter the values of the health in a space seprated manner 
print('Enter the values of the health in a space seprated manner :')
healths = list(map(int, input().rstrip().split()))

# 4. Enter the number of strands of DNA to process
print ('Enter the number of strands of DNA to process : ')
howStrands = int(input())

# 5. Entering the DNA strands
print ('Enter DNA strands : ')
gMap = defaultdict(lambda: [[], [0]])
subs = set()
for id, gene in enumerate(genes):
  gMap[gene][0].append(id)
  for j in range(1, min(len(gene), 500)+1): subs.add(gene[:j])
for v in gMap.values():
  for i, ix in enumerate(v[0]): v[1].append(v[1][i]+healths[ix])

# finding out the largest spread gene using the 'max' function
largest = max(list(map(len, genes)))
hMin, hMax = inf, 0

# Processing the input data bedore going to the getHealth Function
for _ in range(howStrands):
  firstLastd = input().split()
  first = int(firstLastd[0])
  last = int(firstLastd[1])
  strand = firstLastd[2]
  
  # calling the function
  h = getHealth(strand, first, last, largest)
  hMin, hMax = min(hMin, h), max(hMax, h)

# print out the final output

print ('Health of the unhealthiest and the healthiest strands of DNA : ')
print(hMin, hMax)

'''
---------------------------------------------------------------------------------
Test Case #1

User Input :
Enter the number of the genes : 
4
Enter the values of the genes in a space separated manner : 
a b c d
Enter the values of the health in a space seprated manner :
1 2 3 4
Enter the number of strands of DNA to process : 
3
Enter DNA strands : 
1 5 caaab
2 0 xgf
3 1 cab

--------------------------------------------------------------------------------

Output :
Health of the unhealthiest and the healthiest strands of DNA : 
-3 5

--------------------------------------------------------------------------------

Test Case #2

User Input :
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

------------------------------------------------------------------------------

Output :
Health of the unhealthiest and the healthiest strands of DNA : 
0 19

------------------------------------------------------------------------------

More Test cases are mentioned in the Images folder. Check out there!
'''

# --------------------------------------------------------------------------------
# This codebase will solve the problem named, 'Determining DNA Health'
# All the explanations are done in the README.md folder with proper visualization

# Hope this problem will find you interesting enough
# Author : Abhishek Sharma, DCP21
