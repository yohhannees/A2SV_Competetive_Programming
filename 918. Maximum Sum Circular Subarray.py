class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        min_heap = [(0, -1)]
        max_so_far = 0
        max_ending_here = nums[0]
        for i in range(n*2):
            max_so_far += nums[i % n]
            while min_heap and i-min_heap[0][1] > n:
                heappop(min_heap)
            previous_max = min_heap[0][0]
            max_ending_here = max(max_ending_here, max_so_far - previous_max)
            heappush(min_heap, (max_so_far, i))
        return max_ending_here
