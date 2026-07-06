class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            differences[target - nums[i]] = i

        for j in range(len(nums)):
            if differences.get(nums[j], j) != j:
                return [j, differences[nums[j]]]