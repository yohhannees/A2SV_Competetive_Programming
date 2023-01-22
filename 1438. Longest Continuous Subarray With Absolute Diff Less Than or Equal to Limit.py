class Solution:
    def longestSubarray(self, nums: [int], limit: int) -> int:
        res, i, minq, maxq = 0, 0, [], []
        for j, n in enumerate(nums):
            heapq.heappush(minq, (n, j))
            heapq.heappush(maxq, (-n, j))
            if -maxq[0][0] - minq[0][0] > limit:
                i = min(minq[0][1], maxq[0][1]) + 1
                while minq[0][1] < i:
                    heapq.heappop(minq)
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
            res = max(res, j-i+1)
        return res
