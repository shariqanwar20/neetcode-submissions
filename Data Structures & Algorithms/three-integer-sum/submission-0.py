class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hashmap solution -> O(n^2) O(n)
        res = set()
        for i in range(len(nums)):
            map = defaultdict(int)

            for j in range(i+1, len(nums)):
                k = -1 * (nums[i]+nums[j])
                
                if k in map:
                    res.add(tuple(sorted([nums[i], nums[j], k])))
                map[nums[j]] = j
        
        return [list(triplet) for triplet in res]
                    

        # Two pointers solution