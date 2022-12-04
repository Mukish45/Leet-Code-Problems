class Solution:
    def checkString(self, s: str) -> bool:
        x = [*s]
        for i in range(0,len(x)):
            if x[i] == 'b' and i+1<len(x):
                if x[i+1] == 'a':
                    return False

        return True
        