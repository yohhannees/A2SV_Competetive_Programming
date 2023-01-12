class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        a = 0
        b = len(nums) - 1
        while len(nums) != len(ans):
            ans.append(nums[a])
            a += 1
            if a <= b:
                ans.append(nums[b])
                b -= 1
        return (ans)
