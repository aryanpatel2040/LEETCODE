class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0

        for num in list(count):
            complement = k - num
            if complement in count:
                if num == complement:
                    # Choose pairs from the same number
                    pairs = count[num] // 2
                else:
                    # Choose min(count[num], count[complement]) pairs
                    pairs = min(count[num], count[complement])
                operations += pairs
                # Remove used elements from count
                count[num] -= pairs
                count[complement] -= pairs

        return operations