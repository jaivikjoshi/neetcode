class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        previous = set()
        for x in nums:
            if x in previous:
                return True
            previous.add(x)
        return False
