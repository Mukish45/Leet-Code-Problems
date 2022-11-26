class Solution:
    def isPalindrome(self, x: int) -> bool:
            t = str(x)
            t2 = [*t]
            fin = []
            for i in range(len(t),0,-1):
                ans = (t2[i-1])
                fin.extend(ans)
            ans = False
            if fin == t2:
                ans = True
            return ans