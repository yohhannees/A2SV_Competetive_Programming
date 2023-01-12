class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import Counter
        changed.sort()
        n = len(changed)
        count = Counter(changed)
        ans = []
        if n % 2 != 0:
            return []
        for i in changed:
            if i == 0 and count[i] >= 2:
                count[i] -= 2
                ans.append(i)
            if i > 0 and count[i] and count[i * 2]:
                count[i] -= 1
                count[i * 2] -= 1
                ans.append(i)
        return ans if len(ans) == n//2 else []
