from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # move right while valid

        # move left until no more repeating characters

        # check max
        if len(s) < 2:
            return len(s)

        hm = defaultdict(int)
        hm[s[0]] = 1

        l = r = 0
        res = 0

        while r < len(s): 
            while hm[s[r]] == 1:
                res = max(res, r - l + 1)
                r += 1
                if r  == len(s):
                    break
                hm[s[r]] += 1
            
            if r == len(s):
                break
            while not hm[s[r]] == 1:
                hm[s[l]] -= 1
                l += 1

        return res
