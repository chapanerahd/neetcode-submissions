class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return
        mapper = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr = stack.pop()
            for neigh in curr.neighbors:
                if neigh not in mapper:
                    mapper[neigh] = Node(neigh.val)
                    stack.append(neigh)
                mapper[curr].neighbors.append(mapper[neigh])
        
        return mapper[node]