from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # go go go and remove until valid again
        if len(s) == 0:
            return 0

        l, r = 0, 1
        myMap = defaultdict(int)
        currLen = 1
        res = 1

        # initial map setup
        myMap[s[l]] += 1

        while  r < len(s):
            # update hashmap then move pointer 
            if myMap[s[r]] == 0:
                myMap[s[r]] += 1
                currLen = r - l + 1
                res = max(res, currLen)
                r += 1

            else:
                myMap[s[l]] -= 1
                currLen = r - l + 1
                l += 1
                
        return res