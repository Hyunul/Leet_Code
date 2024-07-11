class Solution(object):
    def convertTemperature(self, celsius):
        result = []
        result.append(celsius + 273.15)
        result.append(celsius * 1.8 + 32)

        return result