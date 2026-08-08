class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            newRes = ""
            for i in range(min(len(res), len(s))):
                if res[i] != s[i]:
                    res = newRes
                    break
                else:
                    newRes += s[i]
            res = newRes

            if newRes == "":
                return ""

        return res

