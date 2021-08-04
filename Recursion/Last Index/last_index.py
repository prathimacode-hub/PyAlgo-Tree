#Program to find last index of an element in array.
def lastIndex(arr, si, x):
    l = len(arr)
    if si == l: #if the start index is greater than size of array.
        return -1
    smallerListOutput = lastIndex(arr, si+1, x) #recirsion
    if smallerListOutput != -1:
        return smallerListOutput # if the element is found in the second part of array return index+1
    else:
        if arr[si] == x:#if element is not found in second part of array check for 1st element 
            return si
        else:
            return -1
            
n=int(input("Enter size of array : "))
a=[]
for i in range(n):
  ele=int(input())
  a.append(ele)
x=int(input("Enter element whose last index is to be found : "))
print(lastIndex(a,0,x))

#Example
#Input 5
# 2 1 2 1 3
#1
#Output 
#3