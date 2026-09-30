class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hashmap solution -> O(n^2) O(n)
        # res = set()
        # for i in range(len(nums)):
        #     map = defaultdict(int)

        #     for j in range(i+1, len(nums)):
        #         k = -1 * (nums[i]+nums[j])
                
        #         if k in map:
        #             res.add(tuple(sorted([nums[i], nums[j], k])))
        #         map[nums[j]] = j
        
        # return [list(triplet) for triplet in res]
                    

        # Two pointers solution
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == -1 * nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total < -1 * nums[i]:
                    l += 1
                else:
                    r -= 1
        return res
