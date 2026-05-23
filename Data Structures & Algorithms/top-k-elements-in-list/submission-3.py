from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(int)
        res = []
        run = k
        arr = [[] for i in range(len(nums) + 1)]
        print(len(arr))

        for i in nums:
            myMap[i] += 1

        for key, value in myMap.items():
            arr[value].append(key)

        for myList in reversed(arr):
            while len(myList) != 0:
                res.append(myList[0])
                myList.pop(0)
                if len(res) == k:
                    return res


        return res

            
        