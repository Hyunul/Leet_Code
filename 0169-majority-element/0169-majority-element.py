class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for value in nums:
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1
        temp = set(nums)
        for i in temp:
            if counter[i] > (len(nums)//2):
                return i