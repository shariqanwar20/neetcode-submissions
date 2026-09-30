class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # construct a max heap
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -n)

        # pop elements until k
        count = 0
        while count < k:
            node = -1 * heapq.heappop(maxHeap)
            count += 1
        
        # return the kth popped element
        return node