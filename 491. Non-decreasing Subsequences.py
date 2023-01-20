class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        s = {()}
        for x in nums:
            s |= {a + (x,) for a in s if not a or a[-1] <= x}
        return [a for a in s if len(a) >= 2]


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        return (s := {()}, [s := s | ({a+(x,) for a in s if not a or a[-1] <= x}) for x in nums], [a for a in s if len(a) > 1])[-1]
