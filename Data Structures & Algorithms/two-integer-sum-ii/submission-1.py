class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1

        while True:
            add = numbers[s] + numbers[e]
            if add == target:
                return [s + 1, e + 1]
            elif add > target:
                e -= 1
            else:
                s += 1
        
    