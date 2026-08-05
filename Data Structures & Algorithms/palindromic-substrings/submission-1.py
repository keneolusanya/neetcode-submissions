class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += 1
            l, r = i - 1, i + 1
            while True:
                if l == -1 or r == len(s):
                    break
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break

        for i in range(len(s) - 1):
            l, r = i, i + 1
            while True:
                if l == -1 or r == len(s):
                    break
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break

        return res

               


