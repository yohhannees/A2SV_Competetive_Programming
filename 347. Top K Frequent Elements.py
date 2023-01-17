class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
nums = [1,1,1,2,2,3]  k = 2 
using a hashmap value:frequency
then sorting the hashmasp in decreasing order of frequency 
then changing them to a list
and slicing them upto the value of k
"""
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] = hashmap[num] + 1
        hashmap = dict(
            sorted(hashmap.items(), key=lambda x: x[-1], reverse=True))
        res = list(hashmap.keys())[:k]
        return res
