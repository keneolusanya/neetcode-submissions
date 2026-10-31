class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dr = {
            "N" : (0, 1),
            "S" : (0, -1),
            "E" : (1, 0),
            "W" : (-1, 0)
        }

        cord = (0, 0)
        seen = {cord}
        
        for p in path:
            cord = tuple(x + y for x, y in zip(cord, dr[p]))
            if cord in seen:
                return True
            seen.add(cord)

        return False


