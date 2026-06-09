from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # main validity condition is number of characters in window MINUS
        # frequency of most frequent characters <= k (we can replace enough
        # charcters, don't wanna replace most freqquent character )

        # take window, slide to right as long as condition is valid

        # if becomes invalid, slide to left till it becomes valid again 

        # update hash map as you go through the window

        # update result on a valid window

        # how to find most frequent character? worst case just iterate

        # can stop if res is more than can be optained
        # like right pointer is at the end )
        
        # instead of iterating through the hashmap, you can also just keep
        # track of a maxf variable, and it's okay to not reduce the variable
        # because the result will only change when the maxf increases
        
        l, r = 0, 1
        myMap = defaultdict(int)
        res = 0

        myMap[s[l]] += 1
        myMap[s[r]] += 1 

        while r < len(s):
            # first check hashmap
            maxf = 0
            for elem in myMap.values():
                maxf = max(maxf, elem)
            
            numChars = r - l + 1
            if numChars - maxf <= k:
                res = max(res, numChars)
                # move right pointer
                r += 1
                # update hashmap
                if (r < len(s)):
                    myMap[s[r]] += 1
            else:
                # update hashmap
                myMap[s[l]] -= 1
                # move left pointer
                l += 1   
        
        return res