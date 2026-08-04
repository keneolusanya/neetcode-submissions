class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = {}
        # hashmap of sets? each row, each column, each block
        # sets
        # hash?

        for r in range(9):
            m[f"r{r}"] = set()

        for c in range(9):
            m[f"c{c}"] = set()

        for b in range(9):
            m[f"b{b}"] = set() 
                
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in m[f"r{r}"]:
                    print("here1")
                    print(r, c)
                    return False
                m[f"r{r}"].add(board[r][c])

                if board[r][c] in m[f"c{c}"]:
                    print("here2")
                    return False
                m[f"c{c}"].add(board[r][c])

                if r < 3 and c < 3:
                    if board[r][c] in m["b0"]:
                        print("here3")
                        return False
                    m["b0"].add(board[r][c])
                    continue

                if r < 3 and c < 6:
                    if board[r][c] in m["b1"]:
                        print("here4")
                        return False
                    m["b1"].add(board[r][c])
                    continue

                if r < 3 and c < 9:
                    if board[r][c] in m["b2"]:
                        print(b)
                        print(r, c)
                        print("here5")
                        return False
                    m["b2"].add(board[r][c])
                    continue

                if r < 6 and c < 3:
                    if board[r][c] in m["b3"]:
                        print("here6")
                        return False
                    m["b3"].add(board[r][c])
                    continue

                if r < 6 and c < 6:
                    if board[r][c] in m["b4"]:
                        print("here7")
                        return False
                    m["b4"].add(board[r][c])
                    continue

                if r < 6 and c < 9:
                    if board[r][c] in m["b5"]:
                        print("here8")
                        return False
                    m["b5"].add(board[r][c])
                    continue

                if r < 9 and c < 3:
                    if board[r][c] in m["b6"]:
                        print("here9")
                        return False
                    m["b6"].add(board[r][c])
                    continue

                if r < 9 and c < 6:
                    if board[r][c] in m["b7"]:
                        print("here10")
                        return False
                    m["b7"].add(board[r][c])
                    continue

                if r < 9 and c < 9:
                    if board[r][c] in m["b8"]:
                        print("here11")
                        return False
                    m["b8"].add(board[r][c])
                    continue

        return True