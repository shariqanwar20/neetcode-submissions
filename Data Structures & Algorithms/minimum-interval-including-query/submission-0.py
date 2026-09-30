class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # hashmap for each possible query i.e between 1 and n 

        intervals.sort()

        min_interval_map = defaultdict(int)

        for start, end in intervals:
            for query in queries:
                # if query > (end+1):
                #     break
                
                if query in range(start, end+1):
                    if query not in min_interval_map:
                        min_interval_map[query] = abs(end - start + 1)
                    else:
                        min_interval_map[query] = min(min_interval_map[query], abs(end - start + 1))
                   
                    
        print(min_interval_map)
        output = []
        for query in queries:
            if query in min_interval_map:
                output.append(min_interval_map[query])
            else:
                output.append(-1)
        return output
                        
                        