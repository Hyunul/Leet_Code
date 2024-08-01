class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                cnt += 1
        return cnt