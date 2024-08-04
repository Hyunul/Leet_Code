class Solution(object):
    def shuffle(self, nums, n):
        x = []
        y = []
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+3])

        return result