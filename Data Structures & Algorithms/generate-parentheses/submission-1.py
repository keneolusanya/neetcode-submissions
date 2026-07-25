class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # arr for each path
        # o, c represent options left
        def build(o, c, par):
            if o == 0 and c == 0:
                res.append(par)
                return
            
            if o <= c:
                par1, par2 = par, par
                if o > 0:
                    par1 += "("
                    build(o - 1, c, par1)
                if c > 0:
                    par2 += ")"
                    build(o, c - 1, par2)
        
        build(n, n, "")
        return res
