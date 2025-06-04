class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for x in arr:
            if x % 2 != 0:
                count +=1
                if count == 3:
                    return True
            else:
                count = 0
        return False
        