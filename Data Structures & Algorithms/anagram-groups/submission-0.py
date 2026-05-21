class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        temp = []
        i = 0

        for word in strs:
            check = {}
            for char in word:
                if char not in check:
                    check[char] = 1
                else:
                    check[char] += 1
            
            temp.append(check)
            
            key = tuple(sorted(check.items()))

            if key not in output:
                output[key] = []

            output[key].append(word)

            
        return list(output.values())


              
        


        return [[""]]      

