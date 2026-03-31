class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i  , n in enumerate(nums):
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        return  max(hashmap, key=hashmap.get)
