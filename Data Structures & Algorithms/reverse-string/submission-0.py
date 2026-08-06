class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            templ = s[l]
            tempr = s[r]
            s[l] = tempr
            s[r] = templ
            l += 1
            r -= 1

        