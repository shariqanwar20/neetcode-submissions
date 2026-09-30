class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # construct a max heap
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -n)

        # pop elements until k
        for i in range(k - 1):
            heapq.heappop(maxHeap)
        
        # return the kth popped element
        return heapq.heappop(maxHeap) * -1