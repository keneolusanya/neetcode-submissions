class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        gp = 0
        sp = 0

        while gp < len(g) and sp < len(s):
            if g[gp] > s[sp]:
                sp += 1

            else:
                res += 1
                sp += 1
                gp += 1
        
        return res
