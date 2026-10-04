from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def is_valid_row_col(nr, nc):
            return 0 <= nr < len(heights) and 0 <= nc < len(heights[0])
        
        def bfs(queue):
            visited = set()
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                for dr, dc in [(-1,0), (1, 0), (0,1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if is_valid_row_col(nr, nc) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))
            return visited

        pacific_points = deque()
        atlantic_points = deque()
        for r in range(len(heights)):
            pacific_points.append((r, 0))
            atlantic_points.append((r, len(heights[0])-1))
        
        for c in range(len(heights[0])):
            pacific_points.append((0, c))
            atlantic_points.append((len(heights) - 1, c))

        pacific_visited = bfs(pacific_points)
        atlantic_visited = bfs(atlantic_points)

        return list(pacific_visited.intersection(atlantic_visited))

    