class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[y].append(x)
            adj_list[x].append(y)
        
        visited = [False] * n
        def dfs(i):
            stack = [i]
            visited[i] = True
            while stack:
                curr = stack.pop()
                for neigh in adj_list[curr]:
                    if not visited[neigh]:
                        stack.append(neigh)
                        visited[neigh] = True
        
        res = 0
        for i in range(len(visited)):
            if not visited[i]:
                dfs(i)
                res += 1
        return res
        
        
