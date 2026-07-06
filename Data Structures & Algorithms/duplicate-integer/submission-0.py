class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(nums[i], 0) > 0: 
                return True
            nums_dict[nums[i]] = 1
        
        return False