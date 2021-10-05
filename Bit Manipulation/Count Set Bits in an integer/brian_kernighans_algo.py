# Brian Kernighan's algorithm to count the total number of set bits in `n`
def countSetBits(n):
 
    count = 0
    while (n):

        print("{:032b}".format(n))
        n = n&(n-1)
        count+= 1
     
    return count
 
if __name__ == '__main__':
    n = int(input("n = "))
    print("Set Bits :",countSetBits(n))