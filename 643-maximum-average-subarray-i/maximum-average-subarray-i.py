class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=sum(nums[:k])/k
        sm=sum(nums[:k])
        mx=l
        left=0
        for right in range(k,len(nums)):
            sm-=nums[left]
            sm+=nums[right]
            left+=1
            mx=max(mx,sm/k)
        return mx