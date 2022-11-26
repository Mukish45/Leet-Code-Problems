class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        op=[]
        sum=0
        for x in range(0, len(nums)):
            sum = sum + nums[x]
            op.append(sum)
        return op