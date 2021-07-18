# Sorting an array of numbers using Insertion sort and counting no. of swaps and comparisons made suring the process
a=[66, 45, 34, 6]
swaps=0
comp=0
for i in range(1,len(a)):
    val=a[i]  #assigning it to variable val
    j=i-1 # left elememt to val
    while j >= 0 and val< a[j] :        
        a[j+1]=a[j]  # right element getting val of left
        j=j-1
        swaps=swaps+1  #increments swaps var
        comp=comp +1

    a[j+1]=val   #replaces the swapped number into its sorted location
    if (val>a[j]):  #increments comparisions for case when no swaps are made
        comp=comp+1
    
print('No. of swaps= %d'%swaps)
print('No. of comparisions=%d'% comp)
print("Sorted Array is: ")
for i in range(len(a)):
    print ("% d" % a[i],end=' ')

    
    # Test cases"
'''input:
a = [34,5,77,33] 

output 

5, 33, 34, 77 along with 
no. of swaps = 3 
no. of comparisons=5

### Test case 2
input
a=[90,8,11,3,2000,700,478]

Output:

No. of swaps= 8 
No. of comparisions=12 
Sorted Array is:
 3  8  11  90  478  700  2000
 
 ### Test case 3
 input
 a=[0,33,7000,344,-88,2000]
 
 output:

No. of swaps= 6
No. of comparisions=10
Sorted Array is:
-88  0  33  344  2000  7000'''
