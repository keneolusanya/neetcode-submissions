class Solution:
    def longestPalindrome(self, s: str) -> str:
        # you can go through the centers?
        res = ""
        maxLen = 0

        for i in range(len(s)):
            l = r = i
            while (l > -1 and r < len(s) and s[l] == s[r]):
                currLen = r - l + 1
                if currLen > maxLen:
                    res = s[l:r + 1]
                    maxLen = currLen
                l -= 1
                r += 1

        for i in range(len(s) - 1):
            l = i
            r = i + 1
            while (l > -1 and r < len(s) and s[l] == s[r]):
                currLen = r - l + 1
                if currLen > maxLen:
                    res = s[l:r + 1]
                    maxLen = currLen
                l -= 1
                r += 1
        
        return res    

    
        
                
                