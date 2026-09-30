class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # n = 2
        # (10, 0), (10, 1)
        # t = 2
        
        # {0: 1, 1: 1}
        count_map = defaultdict(int)

        meetings.sort(key=lambda x:x[0])
        min_heap = []
        available = [i for i in range(n)]

        t = 0


        def find_next():
            found = False
            for i in range(n):
                if not rooms[i]:
                    found = True
                    return i

            if not found:
                return n

        for meeting in meetings:

            while min_heap and min_heap[0][0] <= meeting[0]:
                end, room = heapq.heappop(min_heap)
                heapq.heappush(available, room)

            duration = meeting[1] - meeting[0]
            actual_end, actual_start = 0, 0

            if not available:
                # wait
                end, room = heapq.heappop(min_heap)
                heapq.heappush(available, room)
                actual_start = end
            else:
                actual_start = meeting[0]
            
            curr_room = heapq.heappop(available)
            actual_end = actual_start + duration

            heapq.heappush(min_heap, (actual_end, curr_room))
            count_map[curr_room] += 1
            

        res, curr_max = 0, 0
        for key, val in count_map.items():
            if val > curr_max:
                curr_max = val
                res = key
        return res


                

