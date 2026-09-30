class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        l, r = 0, len(nums) - 1



        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[(mid - 1) % size] and nums[mid] < nums[(mid + 1) % size]:
                return nums[mid]
            # [5,1,2,3,4]
            # [3,4,5,6,1,2]
            # [4,5,6,7]
            if nums[l] < nums[mid]:
                # left side is sorted
                if nums[l] < nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                # right side is sorted
                if nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return nums[mid]   