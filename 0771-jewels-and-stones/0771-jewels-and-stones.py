class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_list = list(jewels)
        stones_list = list(stones)
        jewel_cnt = 0

        for i in range(len(stones_list)):
            for j in range(len(jewels_list)):
                if jewels_list[j] == stones_list[i]:
                    jewel_cnt += 1
        
        return jewel_cnt