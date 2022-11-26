class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dis = []
        for i in range(0,n):
            a = (0-nums[i])**2
            dis.append(a)

        min = dis[0]
        index = 0
        for j in enumerate(dis):
            if j[1] == min:
                t = j[0]
                if nums[t] > nums[index]:
                    min = j[1]
                    index = j[0]
            elif j[1] < min:
                min = j[1]
                index = j[0]
        return nums[index]
        