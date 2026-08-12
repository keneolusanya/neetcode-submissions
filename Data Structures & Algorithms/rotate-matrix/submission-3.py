class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 7 2' 1 a
        # 4 5 6 b' 
        # 9' 8 3 c
        # d e f' g
        

        l = t = 0
        r = b = len(matrix) - 1

        # n - 1 per level
        while l < r:
            print(t, l,  b, r)
            for i in range(r - t):
                temp = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = temp
            t += 1
            l += 1
            b -= 1
            r -= 1
    

    