class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        t = [["X" for _ in range(m)] for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                t[c][r] = matrix[r][c]

        return t
