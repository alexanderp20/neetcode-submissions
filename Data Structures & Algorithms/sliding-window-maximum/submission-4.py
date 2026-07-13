import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        res.append(-max_heap[0][0])

        l = 1
        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            popped = max_heap[0]
            if popped[1] >= l and popped[1] <= r:
                res.append(-popped[0])
            else:
                while max_heap[0][1] < l or max_heap[0][1] > r:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
            l+= 1

        return res