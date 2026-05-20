class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        count = {} ##create a empty dictionary

        for charS in s:
            if charS in count:
                count[charS] += 1
            else:
                count[charS] = 1
        print(charS)

        for charT in t:
            if charT not in count:
                return False
            
            count[charT] -= 1

            if count[charT] < 0:
                return False
        return True
            


