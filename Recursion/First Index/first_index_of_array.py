#To find first index of an element in an array.
def firstIndex(arr, si, x):
    l = len(arr) #length of array.
    if l == 0:  #base case 
        return -1 
    if arr[si] == x: #if element is found at start index of an array then return that index.
        return si
    return firstIndex(arr, si+1, x) #recursive call.

arr = [] #initialised array.
n=int(input("Enter size of array : "))
for i in range(n): #input array.
  ele=int(input())
  arr.append(ele)
x=int(input("Enter element to be searched ")) #element to be searched
print(firstIndex(arr, 0, x))
