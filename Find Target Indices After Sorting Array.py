class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        a = 0
        b = 0
        for i in nums:
            a += 1
            if i == target:
                
                b = a - 1
                ans.append(b)
        return (ans)
