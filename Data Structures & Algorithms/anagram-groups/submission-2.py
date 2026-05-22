from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        my_dict = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            my_dict[sorted_word].append(word)
        print(my_dict)

        for items in my_dict.values():
            res.append(items)

        return res
        

