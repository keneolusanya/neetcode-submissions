class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        prev = None

        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for l in s:
            if (prev == "I" and l == "V" or
                prev == "I" and l == "X" or
                prev == "X" and l == "L" or
                prev == "X" and l == "C" or
                prev == "C" and l == "D" or
                prev == "C" and l == "M"):
                    print(prev, l)
                    res += (roman[l] - (2 *roman[prev]))
            
            else:
                res += roman[l]
            prev = l
        
        return res



    

       

                