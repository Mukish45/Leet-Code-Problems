class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = [*jewels]
        sto = [*stones]
        count = 0
        for i in range(0, len(jew)):
            for j in range(0, len(sto)):
                if jew[i] == sto[j]:
                    count+=1
                    
        return count