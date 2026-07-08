class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_left[0] = height[0]
        max_right = [0] * len(height)
        max_right[len(height) - 1] = height[len(height) - 1]
        s = 0

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])

            j = len(height) - i - 1
            max_right[j] = max(max_right[j + 1], height[j])
        
        for i in range(len(height)):
            s += min(max_left[i], max_right[i]) - height[i]
        
        return s
            