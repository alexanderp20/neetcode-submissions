class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max = height[l]
        r_max = height[r]
        max_area = 0

        while l < r:
            if r_max < l_max:
                r -= 1
                if height[r] > r_max:
                    r_max = height[r]
                max_area += (r_max - height[r])
            elif l_max <= r_max:
                l += 1
                if height[l] > l_max:
                    l_max = height[l]
                max_area += (l_max - height[l])

        return max_area