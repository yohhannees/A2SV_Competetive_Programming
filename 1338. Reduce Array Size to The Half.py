class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        n = len(arr)
        a = Counter(arr)
        N = 0
        count = 0
        for k, v in sorted(a.items(), key=lambda x: x[1], reverse=True):
            N += v
            count += 1
            if N >= (n//2):
                break
        return(count)