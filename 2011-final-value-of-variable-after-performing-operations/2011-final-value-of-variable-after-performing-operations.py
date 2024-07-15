class Solution(object):
    def finalValueAfterOperations(self, operations):
        temp = 0
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                temp -= 1
            else:
                temp += 1

        return temp