class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        li = list(map(int, nums))
        li.sort()
        b = list(map(str, li))
        return (b[-k])
