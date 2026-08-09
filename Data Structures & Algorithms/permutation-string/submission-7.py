import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        if s1 == s2:
            return True

        map1 = {i : 0 for i in string.ascii_lowercase}
        map2 = {i : 0 for i in string.ascii_lowercase}
        for s in s1:
            map1[s] += 1

        l, r = 0, len(s1) - 1

        for s in s2[l:r + 1]:
            map2[s] += 1

        matches = 0
        for k in map1.keys():
            if map1[k] == map2[k]:
                matches += 1

        while True:
            if map1 == map2:
                return True
            # matches == 26:
            #     return True
            
            if map2[s2[l]] + 1 == map1[s2[l]]:
                matches += 1
            elif map2[s2[l]] == map1[s2[l]]:
                matches -= 1
            map2[s2[l]] -= 1
            l += 1

            if map2[s2[r]] == map1[s2[r]]:
                matches -= 1

            r += 1
            if r == len(s2):
                return False

            map2[s2[r]] += 1

            if map2[s2[r]] == map1[s2[r]]:
                matches += 1
        





