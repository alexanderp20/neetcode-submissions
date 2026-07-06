import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        
        nums_heap = []
        for key, v in nums_dict.items():
            heapq.heappush(nums_heap, [v, key])

        return [value[1] for value in heapq.nlargest(k, nums_heap)]