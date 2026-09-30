class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1

        tasks_with_freq = []
        for key, val in freq.items():
            tasks_with_freq.append((-1 * val, key))

        heapq.heapify(tasks_with_freq) # (-1, A)
        cooldown = deque() # (A, -1, 6)

        time = 0 # 1 2 3 4 6
        while tasks_with_freq or cooldown:
            while cooldown and cooldown[0][2] <= time:
                tasks_left, task, insert_time = cooldown.popleft()
                heapq.heappush(tasks_with_freq, (tasks_left, task))
            
            if not tasks_with_freq:
                time = cooldown[0][2]
            else:
                count, task = heapq.heappop(tasks_with_freq) # (-1, A)
                if (count + 1) < 0:
                    cooldown.append((count + 1, task, time + n + 1))
                time += 1

        return time




            



            
        
