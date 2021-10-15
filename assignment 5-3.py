class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for m in range(len(nums)):
            for n in range(m):
                if nums[m] == nums[n]:
                    count += 1
        return count
    