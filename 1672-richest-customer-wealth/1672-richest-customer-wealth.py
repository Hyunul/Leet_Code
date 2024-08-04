class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = []
        temp = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                temp += accounts[i][j]
            result.append(temp)
            temp = 0
        print(result)
        # return max(result)