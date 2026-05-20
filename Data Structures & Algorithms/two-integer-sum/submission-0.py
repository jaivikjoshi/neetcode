class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = [(0,0)]
        count = {}


        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and j > i:
                    count[(i,j)] = j - i
                    print(count)
        least_key = min(count, key = count.get)
        arr = list(least_key)       
        return arr
            
