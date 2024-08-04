class Solution(object):
    def shuffle(self, nums, n):
        x = []
        y = []
        result = []
        for i in range(len(nums)):
            if i < n:
                x.append(nums[i])
            else:
                y.append(nums[i])

        for j in range(n):
            result.append(x[j])
            result.append(y[j])
        
        return result