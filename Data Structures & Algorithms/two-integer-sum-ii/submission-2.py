class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            while numbers[r] > target - numbers[l]:
                r -= 1
            while numbers[l] < target - numbers[r]:
                l += 1

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            # l += 1
            # r -= 1