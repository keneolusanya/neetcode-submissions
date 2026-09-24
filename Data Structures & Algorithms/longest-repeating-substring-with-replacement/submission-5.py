from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        l = r = 0
        charFreq[s[l]] += 1
        res = 0

        while r < len(s):
            while (r - l + 1) - max(charFreq.values()) <= k:
                res = max(res, r - l + 1)
                r += 1
                if r == len(s):
                    break
                charFreq[s[r]] += 1

            charFreq[s[l]] -= 1
            l += 1

        return res