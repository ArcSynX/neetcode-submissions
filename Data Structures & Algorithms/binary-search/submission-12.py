class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we are given a sorted arrray in ascending order
        # the time complex is O(logn)

        # initiate the index
        left = 0
        right = len(nums) - 1
        mid = len(nums) //2
        
        while left <= right:

            if nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
            elif  nums[mid] == target:
                return mid
        return -1
        