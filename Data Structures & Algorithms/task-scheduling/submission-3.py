class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks.sort()

        unique = set(tasks)
        size = len(tasks)
        idx = 0
        curr = idx

        min_heap = [(0, tasks[0])]

        for i in range(1, len(tasks)):
            if tasks[i] == tasks[i-1]:
                curr = curr + n + 1
                heapq.heappush(min_heap, (curr, tasks[i]))
            else:
                idx += 1
                curr = idx
                heapq.heappush(min_heap, (curr, tasks[i]))
        print(min_heap)
        time = 0

        last = None
        while min_heap:
            time += 1

            if min_heap[0][0] <= time:
                last, _ = heapq.heappop(min_heap)
        return time + 1 if last == time else time
            



            
        
