class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        c = Counter(nums)
        seen = set()
        res = 0
        for x in c:
            if x not in seen and (k - x) in c:
                if x == (k - x):
                    res += c[x]//2
                else:
                    res += min(c[x], c[k-x])
                seen.add(x)
                seen.add(k - x)
        return (res)
