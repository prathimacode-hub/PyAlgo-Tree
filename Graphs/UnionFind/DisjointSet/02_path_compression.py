
class UnionFind: 
    def __init__(self,size): 
        self.root = [i for i in range(size)]

    def find(self, n): 
        if self.root[n] == n: 
            return n
        
        self.root[n] = self.find(self.root[n])
        return self.root[n]
    # quick union 
    def union(self, a, b): 
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb: 
            self.root[fa] = fb 
            
    def connected(self, x, y): 
        return self.find(x) == self.find(y)
# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true