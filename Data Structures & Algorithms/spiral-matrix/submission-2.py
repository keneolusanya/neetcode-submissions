class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t = l = 0
        b = len(matrix)
        r = len(matrix[0])
        res = []

        while True:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            if t >= b:
                return res
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            if r <= l:
                return res
            for i in range(r - 1, l - 1, - 1):
                res.append(matrix[b - 1][i])
            b -= 1
            if b <= t:
                return res
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l >= r:
                return res
                



            
            

