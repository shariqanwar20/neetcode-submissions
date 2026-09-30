class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        freq_to_num = [[] for _ in range(len(nums) + 1)]

        for key, val in count_map.items():
            freq_to_num[val].append(key)
                
        res = []
        c = 0
        for i in range(len(nums), -1, -1):
            for val in freq_to_num[i]:
                if c < k:
                    res.append(val)
                    c += 1
        return res