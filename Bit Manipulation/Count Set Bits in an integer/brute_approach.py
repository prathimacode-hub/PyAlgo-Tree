# Naive solution to count the total number of set bits in `n`
def countSetBits(N):
    count = 0
    
    for i in range(32):
        if(N & (1 << i)):
            count += 1
    return count
 
 
if __name__ == '__main__':
    n = int(input("n = "))
    print("Set Bits :",countSetBits(n))



