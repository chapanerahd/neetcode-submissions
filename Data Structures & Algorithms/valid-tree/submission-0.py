class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.connected_components = n
    
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        self.connected_components -= 1
        return True

    # @property
    def get_num_nodes_not_connected(self):
        return self.connected_components

            

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):
                return False
        return uf.get_num_nodes_not_connected() == 1

