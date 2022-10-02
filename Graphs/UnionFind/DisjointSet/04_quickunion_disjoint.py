# The vey basics of union find and disjoint sets 
# Basically an array and within that array lies a disjoint set 


# There are two functions when discussing disjoint sets 

# find(a) which takes in a single argument and returns the root of 
# that particular node 

# union(a,b) which takes in two arguments and combines them together 
# let's watch a quick video on how this works and then implement from there 

# First lets implement UnionFind as an object and instantiate it with an array 

class UnionFind: 
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    # union connects two nodes with a left bias meaning that b will always 
    # connect to a 
    def union(self,a,b): 
        # Basically we want to take the parent node of the given thing
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb: 
            self.root[fa] = fb

    # takes in a node a and returns the root node of such
    def find(self, a): 
        while a != self.root[a]: 
            a = self.root[a]
        return a 

uu = UnionFind(10)

print(uu.root)
uu.union(0,1)
uu.union(0,2)
uu.union(1,3)
uu.union(4,8)
uu.union(5,6)
uu.union(5,7)
print(uu.root)
print([i for i in range(10)])