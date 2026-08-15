class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right to down
        # down to left
        # left to up
        # up to right

        ROWS, COLS = len(matrix), len(matrix[0])
        seen = set()
        res = []

        r, c = 0, 0 
        while True:
            while True:
                res.append(matrix[r][c])
                seen.add((r, c))
                # seen or border
                if c + 1 >= len(matrix[0]) or (r, c + 1) in seen:
                    break
                else:
                    c += 1
            
            if r + 1 < len(matrix):
                r += 1
            else:
                break

            if len(seen) >= (ROWS * COLS):
                break

            while True:
                res.append(matrix[r][c])
                seen.add((r, c))
                if r + 1 >= len(matrix) or (r + 1, c) in seen:
                    break
                else:
                    r += 1
            
            if len(seen) >= (ROWS * COLS):
                break

            c -= 1
            while True:
                res.append(matrix[r][c])
                seen.add((r, c))
                if c - 1 < 0 or (r, c - 1) in seen:
                    break
                else: 
                    c -= 1
            
            if len(seen) >= (ROWS * COLS):
                break

            r -= 1
            while True:
                res.append(matrix[r][c])
                seen.add((r, c))
                if r - 1 < 0 or (r - 1, c) in seen:
                    break
                else: 
                    r -= 1
            
            if len(seen) >= (ROWS * COLS):
                break

            c += 1

        return res

            

