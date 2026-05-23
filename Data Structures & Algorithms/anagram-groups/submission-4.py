from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        myMap = defaultdict(list)
        
        for myStr in strs:
            myMap[tuple(sorted(myStr))].append(myStr)

        for value in myMap.values():
            res.append(value)

        return res

        

                
                
            