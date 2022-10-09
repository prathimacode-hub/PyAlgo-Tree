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
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    # takes in a node a and returns the root node of such
    def find(self, a): 
        while a != self.root[a]: 
            a = self.root[a]
        return a 

uu = UnionFind(6)

print(uu.root)
uu.union(0,1)
uu.union(4,5)
uu.union(1,4)

print(uu.root)
#print([i for i in range(6)])