class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_numbers = {}

        greatest_length = 0
        for num in nums:
            consecutive_numbers[num] = num + 1

        for num in nums:
            if self.consecutive(num, consecutive_numbers) > greatest_length:
                greatest_length = self.consecutive(num, consecutive_numbers)
        
        return greatest_length

    
    def consecutive(self, num, consecutive_numbers):
        if (num + 1) not in consecutive_numbers:
            return 1
        else:
            return self.consecutive(num + 1, consecutive_numbers) + 1

