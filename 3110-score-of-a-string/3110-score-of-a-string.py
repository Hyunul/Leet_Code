class Solution:
    def scoreOfString(self, s: str) -> int:
        str_list = list(s)
        result = 0
        for i in range(0, len(str_list)-1):
            print(i)
            temp = abs(ord(str_list[i]) - ord(str_list[i+1]))
            result += temp
        return result