class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = []
        for i in range(1, int(n/2)+1):
            if n%i == 0:
                ans.append(i)
        ans.append(n)

        if len(ans) < k:
            return -1
        else:
            return ans[k-1]
        