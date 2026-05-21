class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []

        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1
        

        while k > 0:
            output.append(max(count, key=count.get))
            k = k - 1
            del count[max(count, key=count.get)]





        return output 