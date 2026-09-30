class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # create a max heap that stores the current max
        maxHeap = []
        temp = []

        res = []
        start = 0

        # add to heap and check for current max
        for end in range(len(nums)):
            heapq.heappush(maxHeap, -1 * nums[end]) 
            while (end-start+1) >= k:
                res.append(maxHeap[0] * -1)
                # remove element at start
                while maxHeap[0] * -1 != nums[start]:
                    heapq.heappush(temp, heapq.heappop(maxHeap))
                heapq.heappop(maxHeap)

                # reinsert
                while len(temp) > 0:
                    heapq.heappush(maxHeap, heapq.heappop(temp))
                start += 1

            
        return res