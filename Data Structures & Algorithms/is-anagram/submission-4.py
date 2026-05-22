from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict1 = defaultdict(int)
        mydict2 = defaultdict(int)
        
        for l in s:
            mydict1[l] += 1
        
        for l in t:
            mydict2[l] += 1

        if mydict1 == mydict2:
            return True
        return False

        