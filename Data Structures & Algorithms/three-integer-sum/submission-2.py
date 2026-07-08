class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:    
                two_sum = nums[l] + nums[r]
                if two_sum + nums[i] == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif two_sum > -nums[i]:
                    r -= 1
                elif two_sum < -nums[i]:
                    l += 1
        
        return output