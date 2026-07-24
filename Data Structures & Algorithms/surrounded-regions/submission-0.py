class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # scan border and look for any O's
        # change those O's to T's
        # recursively change any neighbors found to T's (I think)
        # then when you go through the board change any O to an X
        # I would say probably still use a seens set
        # then change back T's to O's
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def mark(row, col):
            board[row][col] = "T"
            seen.add((row, col))
            if col + 1 in range(cols) and (row, col + 1) not in seen:
                if board[row][col + 1] == "O":
                    mark(row, col + 1)
            if row - 1 in range(rows) and (row - 1, col) not in seen:
                if board[row - 1][col] == "O":
                    mark(row - 1, col)
            if col - 1 in range(cols) and (row, col - 1) not in seen:
                if board[row][col - 1] == "O":
                    mark(row, col - 1)
            if row + 1 in range(rows) and (row + 1, col) not in seen:
                if board[row + 1][col] == "O":
                    mark(row + 1, col)
            

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0
                    or row == rows - 1 or col == cols - 1):
                        if board[row][col] == "O" and (row, col) not in seen:
                            mark(row, col)

        for row in range(rows):
            for col in range(cols):
                if not (row == 0 or col == 0
                    or row == rows - 1 or col == cols - 1):
                        if board[row][col] == "O":
                            board[row][col] = "X"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"