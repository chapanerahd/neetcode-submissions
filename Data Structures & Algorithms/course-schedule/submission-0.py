from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegrees[crs] += 1
        
        q = deque()
        for crs in range(len(indegrees)):
            if indegrees[crs] == 0:
                q.append(crs)
        
        finished = 0
        while q:
            curr = q.popleft()
            finished += 1
            for crs in adj[curr]:
                indegrees[crs] -= 1
                if indegrees[crs] == 0:
                    q.append(crs)
        
        return finished == numCourses




