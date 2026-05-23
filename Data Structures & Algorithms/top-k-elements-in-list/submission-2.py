from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(int)
        res = []
        run = k

        for i in nums:
            myMap[i] += 1

        mapItems = myMap.items()
        
        while run > 0:
            maxNum = 0
            for key in myMap:
                if myMap[key] > maxNum:
                    maxNum = myMap[key]
            for key in myMap:
                if myMap[key] == maxNum:
                    res.append(key)
                    myMap[key] = 0
                    break
            run -= 1

        return res

            
        