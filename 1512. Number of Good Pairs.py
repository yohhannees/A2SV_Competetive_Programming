class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    count += 1
                j += 1
        return (count)
