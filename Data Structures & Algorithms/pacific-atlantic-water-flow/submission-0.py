class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        visitedP = set()
        visitedA = set()

        def dfs(r, c, pac):
            if pac:
                visitedP.add((r, c))
                s = visitedP
            else:   
                visitedA.add((r, c))
                s = visitedA
            
            # up
            if r > 0:
                if (heights[r - 1][c] >= heights[r][c] and 
                    (r - 1, c) not in s):
                    dfs(r - 1, c, pac)
            # down
            if r < rows - 1:
                if (heights[r + 1][c] >= heights[r][c] and
                    (r + 1, c) not in s):
                    dfs(r + 1, c, pac)
            # left
            if c > 0:
                if (heights[r][c - 1] >= heights[r][c] and
                    (r, c - 1) not in s):
                    dfs(r, c - 1, pac)
            # right
            if c < cols - 1:
                if (heights[r][c + 1] >= heights[r][c] and
                    (r, c + 1) not in s):
                    dfs(r, c + 1, pac)
            
        # pacific run
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, True)

        # atlantic run
        for r in range(rows):
            for c in range(cols):
                if r == rows - 1 or c == cols - 1:
                    dfs(r, c, False)

        print(f"visitedP: {visitedP}")
        print(f"visitedA: {visitedA}")
        setRes = visitedP.intersection(visitedA)
        res = []
        for s in setRes:
            res.append(list(s))

        return list(res)

