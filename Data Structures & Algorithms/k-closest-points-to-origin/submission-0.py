class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # constrcut a minHeap with distances of all points from (0,0)

        def calc_dist(p1, p2) -> float:
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        min_heap = [(calc_dist((0, 0), p), tuple(p)) for p in points]
        heapq.heapify(min_heap)

        res = []
        for i in range(k):
            res.append(list(heapq.heappop(min_heap)[1]))
        
        return res
        