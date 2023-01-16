class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        nums = [3,5,2,3]
        sort-->[2,3,3,5]
        nums = [3,5,4,2,4,6]
        sort-->[2,3,4,4,5,6]
        
        
        """
        res = []
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            res.append(nums[l] + nums[r])
            l += 1
            r -= 1
        return max(res)
