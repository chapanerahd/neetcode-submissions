"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return
        mapper = {node: Node(node.val)}
        stack = [node]
        visited = set()
        visited.add(node)
        while stack:
            curr = stack.pop()
            for neigh in curr.neighbors:
                if neigh not in mapper:
                    mapper[neigh] = Node(neigh.val)
                if neigh not in visited:
                    stack.append(neigh)
                    visited.add(neigh)
                mapper[curr].neighbors.append(mapper[neigh])
        
        return mapper[node]
