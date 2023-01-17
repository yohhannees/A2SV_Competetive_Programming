class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k = []
        for idx in range(len(arr)):
            max1 = max(arr[:n-idx])
            max_idx = arr.index(max1) + 1
            arr[:max_idx] = reversed(arr[:max_idx])
            k.append(max_idx)
            arr[:n-idx] = reversed(arr[:n-idx])
            k.append(n-idx)
        return k
