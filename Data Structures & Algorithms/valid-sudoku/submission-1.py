class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}
        blocks = {(i, j) : set() for j in range(3) for i in range(3)}
        # hashmap of sets? each row, each column, each block
        # sets
        # hash?

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue

                if (n in rows[r] or n in cols[c] or
                    n in blocks[(r // 3, c // 3)]):
                        return False
                
                rows[r].add(n)
                cols[c].add(n)
                blocks[(r // 3, c // 3)].add(n)

        return True