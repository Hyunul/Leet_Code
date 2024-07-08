class Solution:
    def scoreOfString(self, s: str) -> int:
        str_list = list(s)
        result = 0
        for i in range(0, len(str_list)-1):
            result += (abs(ord(str_list[i]) - ord(str_list[i+1])))
        return result