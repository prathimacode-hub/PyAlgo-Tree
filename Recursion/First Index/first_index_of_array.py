
def firstIndex(arr, si, x):
    l = len(arr)
    if l == 0:
        return -1 
    if arr[si] == x:
        return si
    return firstIndex(arr, si+1, x)

arr = []
n=int(input("Enter size of array : "))
for i in range(n):
  ele=int(input())
  arr.append(ele)
x=int(input("Enter element to be searched "))
print(firstIndex(arr, 0, x))
