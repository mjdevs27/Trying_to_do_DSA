class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = i + 1 
        for k in range(len(nums)+1):
            if j < len(nums) and nums[i] == nums[j]:
                nums.remove(nums[j])
                j = i + 1
            else:
                i = i + 1
                j = i + 1

        return len(nums)
