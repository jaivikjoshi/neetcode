class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        multi = 1 
        output = [0] * len(nums)

        if zero_count > 1:
            return output
        

        for num in nums:
            if num != 0:
                multi *= num
            
        for i in range(len(output)):
            if zero_count == 1:
                if nums[i] == 0:
                    output[i] = multi
                else:
                    output[i] = 0
            else: 
                output[i] = multi // nums[i]
        

        return output
        