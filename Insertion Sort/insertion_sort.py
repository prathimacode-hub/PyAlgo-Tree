a=[66, 45, 34, 6]
swaps=0
comp=0
for i in range(1,len(a)):
    val=a[i]
    j=i-1 # left elememt to val
    while j >= 0 and val< a[j] :        
        a[j+1]=a[j]  # right element getting val of left
        j=j-1
        swaps=swaps+1
        comp=comp +1

    a[j+1]=val
    if (val>a[j]):
        comp=comp+1
    
print('No. of swaps= %d'%swaps)
print('No. of comparisions=%d'% comp)
print("Sorted Array is: ")
for i in range(len(a)):
    print ("% d" % a[i],end=' ')