class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # seen set for 2d indexes
        seen = set()
        islands = 0

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            seen.add((r, c))

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr in range(rows)
                    and c + dc in range(cols)
                    and grid[r + dr][c + dc] == "1"
                    and (r + dr, c + dc) not in seen):
                        q.append((r + dr, c + dc))
                        seen.add((r + dr,c + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1

        return islands
                    

        
        

