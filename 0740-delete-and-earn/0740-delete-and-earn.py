class Solution(object):
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        a, b = 0, 0
        for x in range(min(nums), max(nums)+1):
            a, b = b, max(count[x] * x + a, b)
        return b
        