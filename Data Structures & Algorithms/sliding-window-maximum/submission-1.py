class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # create a max heap that stores the current max
        maxHeap = []
        temp = []

        res = []
        start = 0

        # add to heap and check for current max
        for end in range(len(nums)):
            heapq.heappush(maxHeap, (-1 * nums[end], end)) 
            if (end-start+1) >= k:
                # remove element at start
                while maxHeap[0][1] <= end-k:
                    heapq.heappop(maxHeap)
                
                res.append(maxHeap[0][0] * -1)
                start += 1

            
        return res